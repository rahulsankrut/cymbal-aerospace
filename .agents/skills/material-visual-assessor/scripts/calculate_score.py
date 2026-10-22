"""Dynamic rubric validator and score calculator for Material Assessor."""

from __future__ import annotations

import argparse
import dataclasses
import functools
import glob
import json
import os
import re
import sys
import types
from typing import Any, Sequence


def _normalize_identifier(text: str) -> str:
  """Normalizes strings to lowercase alphanumeric characters."""
  return re.sub(r'[^a-z0-9]', '', text.lower())


def _normalize_answer(value: Any) -> str:
  """Normalizes answer values from strings, booleans, or Enum instances."""
  if value is None:
    return ''
  if hasattr(value, 'value'):
    value = value.value
  normalized_text = str(value).strip().lower()
  if normalized_text.startswith('answer.'):
    normalized_text = normalized_text[len('answer.') :]
  return normalized_text


def _get_field(target_object: Any, field_name: str, default: Any = None) -> Any:
  """Safely retrieves a field from a dict or an object attribute."""
  if isinstance(target_object, dict):
    return target_object.get(field_name, default)
  return getattr(target_object, field_name, default)


def _extract_component_name(component: Any) -> str:
  """Extracts primary structural component name from str, dict, or model.

  Intentionally reads ONLY `mappedComponent` / `mapped_component` (falling back
  to `name` for legacy payloads) and ignores `functionalAliases` /
  `functional_aliases` so secondary semantic roles do not activate
  false-positive component rubrics during Phase 2 scoring.

  Args:
    component: A component string, dict, or model instance.

  Returns:
    The extracted primary structural component name string, or empty string.
  """
  if isinstance(component, str):
    return component
  for field_name in ('mappedComponent', 'mapped_component', 'name'):
    value = _get_field(component, field_name)
    if value is not None:
      return str(getattr(value, 'value', value))
  return ''


def _extract_answer(item: Any) -> str:
  """Extracts normalized answer from scalar, dict, or Pydantic model."""
  if item is None:
    return ''
  if isinstance(item, dict) or hasattr(item, 'answer'):
    raw_answer = _get_field(item, 'answer')
  else:
    raw_answer = item
  return _normalize_answer(raw_answer)


def _format_percentage(percentage_value: Any) -> str:
  """Formats a numeric percentage score or returns 'N/A'."""
  return 'N/A' if percentage_value == 'N/A' else f'{percentage_value}%'


def find_references_dir(explicit_directory: str | None = None) -> str:
  """Finds references/ directory relative to script, google3, or runfiles."""
  if explicit_directory:
    if os.path.isdir(explicit_directory):
      return os.path.abspath(explicit_directory)
    raise FileNotFoundError(
        f'Explicit references directory not found: {explicit_directory}'
    )

  script_directory = os.path.dirname(os.path.abspath(__file__))
  candidates = [
      os.path.join(os.path.dirname(script_directory), 'references'),
      os.path.abspath('ux/gdp/ai/skills/material_visual_assessor/references'),
  ]
  runfiles = os.environ.get('RUNFILES_DIR') or os.environ.get('TEST_SRCDIR')
  if runfiles:
    candidates.extend([
        os.path.join(
            runfiles,
            'google3/ux/gdp/ai/skills/material_visual_assessor/references',
        ),
        os.path.join(
            runfiles,
            '__main__/ux/gdp/ai/skills/material_visual_assessor/references',
        ),
    ])

  for candidate_path in candidates:
    if os.path.isdir(candidate_path) and os.path.exists(
        os.path.join(candidate_path, 'rubric.md')
    ):
      return candidate_path

  for candidate_path in candidates:
    if os.path.isdir(candidate_path):
      return candidate_path

  raise FileNotFoundError(
      'Could not locate Material Visual Assessor references/ directory. '
      f'Checked paths: {candidates}'
  )


# A top-level Markdown list item ("- ..." at column 0) plus any indented
# continuation lines (mdformat wraps long items), ending in
# "-> `references/rubrics/<slug>.md`". Anchoring to line starts keeps a match
# from spanning HTML comments, headings, or horizontal rules.
_COMPONENT_MAPPING_PATTERN = re.compile(
    r'^-[ \t]+((?:[^\n]|\n[ \t]+)*?)'
    r'\s+->\s+`references/rubrics/([a-zA-Z0-9_\-]+)\.md`',
    re.MULTILINE,
)


def _parse_component_mappings(content: str) -> list[tuple[str, str]]:
  """Parses component-to-rubric list items from assessment_instruction.md.

  Args:
    content: Markdown text of assessment_instruction.md.

  Returns:
    One `(component_name, rubric_slug)` pair per component, in document order.
  """
  mappings: list[tuple[str, str]] = []
  for components_text, rubric_slug in _COMPONENT_MAPPING_PATTERN.findall(
      content
  ):
    names = re.findall(r'`([^`]+)`', components_text) or (
        components_text.split(',')
    )
    for name in names:
      component_name = ' '.join(name.split())
      if component_name:
        mappings.append((component_name, rubric_slug))
  return mappings


_DEFAULT_SUBCATEGORIES: types.MappingProxyType[str, tuple[str, ...]] = (
    types.MappingProxyType({
        'app_bar_score': ('app-bars', 'app_bar', 'appbar'),
        'aurora_score': ('aurora',),
        'bottom_sheet_score': ('bottom-sheet', 'bottom_sheet', 'bottomsheet'),
        'button_score': ('button', 'buttons'),
        'color_score': ('color',),
        'fab_score': ('fab', 'fabs'),
        'layout_score': ('layout',),
        'navigation_bar_score': (
            'nav_bar',
            'navbar',
            'navigation-bars',
            'navigation_bar',
        ),
        'typography_score': ('typography',),
    })
)


@dataclasses.dataclass(frozen=True)
class RubricConfig:
  """Encapsulates dynamically parsed scoring and rubric rules from Markdown references."""

  weight_to_tier: dict[int, int]
  pass_threshold: int
  subcategories: dict[str, tuple[str, ...]]
  questions: dict[str, dict[str, Any]]
  foundational_ids: frozenset[str]
  component_questions: dict[str, list[str]]
  component_to_slug: dict[str, str]

  @classmethod
  @functools.lru_cache(maxsize=4)
  def load(cls, references_directory: str | None = None) -> RubricConfig:
    """Parses markdown references and returns a cached RubricConfig."""
    resolved_directory = find_references_dir(references_directory)
    component_to_slug: dict[str, str] = {}

    # 1. Parse component-to-rubric mappings from assessment_instruction.md
    instruction_path = os.path.join(
        resolved_directory, 'assessment_instruction.md'
    )
    if os.path.exists(instruction_path):
      with open(instruction_path, 'r', encoding='utf-8') as instruction_file:
        instruction_content = instruction_file.read()
      for component_name, rubric_slug in _parse_component_mappings(
          instruction_content
      ):
        component_to_slug[_normalize_identifier(component_name)] = rubric_slug

    # 2. Parse scoring instructions (tiers, threshold, subcategory definitions)
    weight_to_tier: dict[int, int] = {}
    pass_threshold = 85
    subcategories: dict[str, tuple[str, ...]] = dict(_DEFAULT_SUBCATEGORIES)

    scoring_path = os.path.join(resolved_directory, 'scoring_instruction.md')
    if os.path.exists(scoring_path):
      with open(scoring_path, 'r', encoding='utf-8') as scoring_file:
        scoring_content = scoring_file.read()

      for tier, weight in re.findall(
          r'Tier\s+(\d+)[^:\n]*?Weight\s*=\s*(\d+)', scoring_content, re.I
      ):
        weight_to_tier[int(weight)] = int(tier)

      match_pass = re.search(
          r'(\d+)%\s*–\s*100%\s*\([^)]*PASSED', scoring_content
      )
      if match_pass:
        pass_threshold = int(match_pass.group(1))

      # Each subcategory covers only the rubric files in its "Applicable
      # Sources" column, plus its stem and criteria prefixes for matching
      # foundational question IDs. Sibling components with their own rubric
      # files (e.g. Icon button vs. Button) are not folded in.
      for field_name, prefixes, sources in re.findall(
          r'\|\s*\*\*`([a-zA-Z0-9_]+)`\*\*\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|',
          scoring_content,
      ):
        snake_case_field = re.sub(r'(?<!^)(?=[A-Z])', '_', field_name).lower()
        stem = snake_case_field.replace('_score', '')
        matched_slugs = set(
            re.findall(r'rubrics/([a-zA-Z0-9_\-]+)\.md', sources)
        )
        matched_slugs.add(stem)
        for prefix in re.findall(r'\[(.*?)\]', prefixes):
          matched_slugs.add(_normalize_identifier(prefix).rstrip('s'))

        subcategories[snake_case_field] = tuple(sorted(matched_slugs))

    # 3. Parse rubric questions from rubric.md, quality.md, and rubrics/*.md
    questions: dict[str, dict[str, Any]] = {}
    foundational_ids: set[str] = set()
    component_questions: dict[str, list[str]] = {}

    markdown_files = [
        os.path.join(resolved_directory, 'rubric.md'),
        os.path.join(resolved_directory, 'quality.md'),
    ] + sorted(glob.glob(os.path.join(resolved_directory, 'rubrics', '*.md')))
    for file_path in markdown_files:
      if not os.path.exists(file_path):
        continue
      rubric_slug = os.path.splitext(os.path.basename(file_path))[0]
      is_foundational = rubric_slug == 'rubric'
      is_supplemental = rubric_slug == 'quality'

      with open(file_path, 'r', encoding='utf-8') as markdown_file:
        file_text = markdown_file.read()

      match_header = re.search(r'^#\s+(.+)', file_text, re.MULTILINE)
      if match_header and not is_foundational and not is_supplemental:
        component_to_slug.setdefault(
            _normalize_identifier(match_header.group(1)), rubric_slug
        )

      for block in re.split(r'\[ID:\s*', file_text)[1:]:
        match_id = re.search(r'^([a-zA-Z0-9_]+)\]', block)
        if not match_id:
          continue
        question_id = match_id.group(1)

        match_metric = re.search(r'\[Metric\s+type:\s*([^\]]+)\]', block, re.I)
        metric = (
            'Adherence'
            if match_metric and 'adherence' in match_metric.group(1).lower()
            else 'Hygiene'
        )
        match_weight = re.search(r'\[Weight:\s*(\d+)\s*\]', block)
        weight = int(match_weight.group(1)) if match_weight else 3

        questions[question_id] = {
            'id': question_id,
            'metric': metric,
            'weight': weight,
            'slug': rubric_slug,
        }
        if is_foundational:
          foundational_ids.add(question_id)
        elif not is_supplemental:
          component_questions.setdefault(rubric_slug, []).append(question_id)
          component_to_slug.setdefault(
              _normalize_identifier(rubric_slug), rubric_slug
          )
          component_to_slug.setdefault(
              _normalize_identifier(rubric_slug).rstrip('s'), rubric_slug
          )

    return cls(
        weight_to_tier=weight_to_tier,
        pass_threshold=pass_threshold,
        subcategories=subcategories,
        questions=questions,
        foundational_ids=frozenset(foundational_ids),
        component_questions=component_questions,
        component_to_slug=component_to_slug,
    )

  def get_expected_question_ids(
      self, components: Sequence[Any] | None = None
  ) -> set[str]:
    """Returns expected question IDs for detected components."""
    expected_ids = set(self.foundational_ids)

    def _visit_components(items: Sequence[Any] | None) -> None:
      for component in items or []:
        component_name = _extract_component_name(component)
        rubric_slug = self.component_to_slug.get(
            _normalize_identifier(component_name)
        )
        if rubric_slug and rubric_slug in self.component_questions:
          expected_ids.update(self.component_questions[rubric_slug])
        subcomponents = _get_field(component, 'subcomponents')
        if subcomponents:
          _visit_components(subcomponents)

    _visit_components(components)
    return expected_ids

  def evaluate(
      self,
      data: dict[str, Any] | str | Any,
      strict: bool = False,
  ) -> dict[str, Any]:
    """Validates rubric completeness and computes M3 compliance scores."""
    if isinstance(data, str):
      if os.path.exists(data):
        with open(data, 'r', encoding='utf-8') as data_file:
          data = json.load(data_file)
      else:
        data = json.loads(data)
    elif hasattr(data, 'model_dump'):
      data = data.model_dump()
    elif hasattr(data, 'dict') and callable(getattr(data, 'dict')):
      data = data.dict()

    raw_components = (
        _get_field(data, 'components')
        or _get_field(data, 'detected_components')
        or _get_field(data, 'detectedComponents')
        or []
    )
    rubric = (
        _get_field(data, 'rubric')
        or _get_field(data, 'criteria_status')
        or _get_field(data, 'criteriaStatus')
    )
    if rubric is None:
      if isinstance(data, dict) and any(key in self.questions for key in data):
        rubric = data
      else:
        rubric = {}

    expected_ids = self.get_expected_question_ids(raw_components)
    missing_questions = [
        question_id
        for question_id in sorted(expected_ids)
        if _extract_answer(rubric.get(question_id))
        not in ('yes', 'no', 'true', 'false', 'n/a', 'na')
    ]

    warnings: list[str] = []
    if missing_questions:
      warnings.append(
          f'⚠️ INCOMPLETE RUBRIC WARNING: {len(missing_questions)} expected'
          f' rubric question(s) were NOT evaluated: {missing_questions}'
      )
      if strict:
        raise ValueError(
            f'Incomplete rubric: {len(missing_questions)} questions missing.'
        )

    scores = {'hygiene': [0, 0], 'adherence': [0, 0]}
    subcategory_points = {
        subcategory: [0, 0] for subcategory in self.subcategories
    }

    for question_id, evaluation_item in rubric.items():
      answer = _extract_answer(evaluation_item)
      question_definition = self.questions.get(
          question_id, {'metric': 'Hygiene', 'weight': 3, 'slug': ''}
      )

      if isinstance(evaluation_item, dict):
        evaluation_item.setdefault('metric_type', question_definition['metric'])
        evaluation_item.setdefault(
            'tier',
            self.weight_to_tier.get(question_definition['weight'], 2),
        )

      if answer not in ('yes', 'no', 'true', 'false'):
        continue
      passed = answer in ('yes', 'true')
      weight = question_definition['weight']
      score_bucket = (
          scores['adherence']
          if question_definition['metric'] == 'Adherence'
          else scores['hygiene']
      )
      score_bucket[1] += weight
      if passed:
        score_bucket[0] += weight

      # Component-rubric questions count only toward the subcategory that lists
      # their rubric file. Question-ID prefixes (e.g. `color_`) are a fallback
      # for foundational and unknown questions, which have no per-subcategory
      # file; applying them to component questions would leak `button_group_*`
      # into `button_score`.
      question_slug = question_definition['slug']
      match_by_prefix = question_slug not in self.component_questions
      for subcategory_name, rubric_slugs in self.subcategories.items():
        if any(
            question_slug == rubric_slug
            or (
                match_by_prefix
                and question_id.startswith(rubric_slug.rstrip('s'))
            )
            for rubric_slug in rubric_slugs
        ):
          subcategory_points[subcategory_name][1] += weight
          if passed:
            subcategory_points[subcategory_name][0] += weight

    hygiene_score = (
        round(100 * scores['hygiene'][0] / scores['hygiene'][1])
        if scores['hygiene'][1] > 0
        else 'N/A'
    )
    adherence_score = (
        round(100 * scores['adherence'][0] / scores['adherence'][1])
        if scores['adherence'][1] > 0
        else 'N/A'
    )
    if isinstance(hygiene_score, int):
      adherence_multiplier = (
          adherence_score / 100.0 if isinstance(adherence_score, int) else 1.0
      )
      final_score: int | str = round(hygiene_score * adherence_multiplier)
    else:
      final_score = 'N/A'

    if (
        isinstance(final_score, int)
        and final_score >= self.pass_threshold
        and isinstance(hygiene_score, int)
        and hygiene_score >= self.pass_threshold
        and (
            adherence_score == 'N/A'
            or (
                isinstance(adherence_score, int)
                and adherence_score >= self.pass_threshold
            )
        )
    ):
      compliance_status = 'PASSED'
    else:
      compliance_status = 'NEEDS_REFINEMENT'

    report_lines = [
        '=' * 60,
        'Material Design 3 Compliance Report',
        '=' * 60,
        f'Status:          [{compliance_status}]',
        f'Final Score:     {_format_percentage(final_score)}',
        f'UI Hygiene:      {_format_percentage(hygiene_score)}',
        f'M3 Adherence:    {_format_percentage(adherence_score)}',
    ]

    result: dict[str, Any] = {
        'status': compliance_status,
        'score': final_score,
        'final_score': final_score,
        'hygiene_score': hygiene_score,
        'adherence_score': adherence_score,
        'valid': len(missing_questions) == 0,
        'warnings': warnings,
        'missing_questions': missing_questions,
        'report': '\n'.join(report_lines),
    }
    for subcategory_name, (
        points_earned,
        points_total,
    ) in subcategory_points.items():
      result[subcategory_name] = (
          round(100 * points_earned / points_total)
          if points_total > 0
          else 'N/A'
      )

    return result


def calculate(
    data: dict[str, Any] | str | Any,
    references_directory: str | None = None,
    strict: bool = False,
) -> dict[str, Any]:
  """Validates rubric completeness and computes M3 compliance scores."""
  return RubricConfig.load(references_directory).evaluate(data, strict=strict)


def calculate_m3_score(
    rubric: dict[str, Any],
    components: Sequence[Any] | None = None,
) -> dict[str, Any]:
  """Validates rubric completeness and calculates deterministic M3 compliance scores."""
  return calculate({'components': list(components or []), 'rubric': rubric})


def get_expected_question_ids(
    components: Sequence[Any] | None = None,
    references_directory: str | None = None,
) -> set[str]:
  """Returns expected question IDs for detected components."""
  return RubricConfig.load(references_directory).get_expected_question_ids(
      components
  )


def main(argv: Sequence[str] | None = None) -> int:
  """CLI entrypoint."""
  parser = argparse.ArgumentParser(
      description='Validate rubric completeness and calculate M3 scores.'
  )
  parser.add_argument('-i', '--input', help='Path to assessment JSON file.')
  parser.add_argument('-j', '--json', help='Raw assessment JSON string.')
  parser.add_argument('-o', '--output', help='Optional path to write output.')
  parser.add_argument(
      '--strict',
      action='store_true',
      help='Exit with code 1 if rubric is incomplete.',
  )
  parser.add_argument(
      '-q', '--quiet', action='store_true', help='Output JSON only.'
  )

  arguments = parser.parse_args(argv)
  raw_input_data = arguments.json or arguments.input
  if not raw_input_data and not sys.stdin.isatty():
    raw_input_data = sys.stdin.read()
  if not raw_input_data:
    parser.print_help()
    return 1

  try:
    assessment_result = calculate(raw_input_data, strict=arguments.strict)
  except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
    sys.stderr.write(f'Error: {error}\n')
    return 1

  if not arguments.quiet:
    if assessment_result['warnings']:
      for warning_message in assessment_result['warnings']:
        print(warning_message)
      print('-' * 60)
    print(f"Compliance Status:       [{assessment_result['status']}]")
    print(
        '  • Final Score:         '
        f" {_format_percentage(assessment_result['final_score'])}"
    )
    print(
        '  • UI Hygiene:          '
        f" {_format_percentage(assessment_result['hygiene_score'])}"
    )
    print(
        '  • M3 Adherence:        '
        f" {_format_percentage(assessment_result['adherence_score'])}"
    )
    print('Subcategory Scores:')
    subcategory_keys = [
        key
        for key in assessment_result
        if key.endswith('_score')
        and key not in ('hygiene_score', 'adherence_score', 'final_score')
    ]
    for subcategory in sorted(subcategory_keys):
      subcategory_display_name = (
          subcategory.replace('_score', '').replace('_', ' ').title()
      )
      score_value = assessment_result[subcategory]
      print(
          f'  • {subcategory_display_name:<18}:'
          f' {_format_percentage(score_value)}'
      )

  if arguments.output:
    with open(arguments.output, 'w', encoding='utf-8') as output_file:
      json.dump(assessment_result, output_file, indent=2)

  return 2 if arguments.strict and not assessment_result['valid'] else 0
