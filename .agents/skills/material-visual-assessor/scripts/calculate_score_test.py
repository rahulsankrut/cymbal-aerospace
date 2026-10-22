"""Unit tests for calculate_score.py script in material-visual-assessor skill."""

import json
import os
import shutil
import tempfile
from absl.testing import absltest
from google3.ux.gdp.ai.skills.material_visual_assessor.scripts import calculate_score


class CalculateScoreTest(absltest.TestCase):

  def test_foundational_question_ids(self):
    expected = calculate_score.get_expected_question_ids([])
    self.assertLen(expected, 65)
    self.assertIn('typography_sentence_case', expected)
    self.assertIn('color_surface_roles', expected)
    self.assertIn('layout_hardware_clipping', expected)

  def test_expected_question_ids_with_components(self):
    components = [
        {'name': 'Modal Sheet', 'mapped_component': 'Bottom sheet'},
        {'name': 'Action Button', 'mapped_component': 'Filled button'},
    ]
    expected = calculate_score.get_expected_question_ids(components)
    # Foundational 65 + bottom sheet questions + button questions
    self.assertGreater(len(expected), 65)
    self.assertIn('bottom_sheet_drag_handle', expected)
    self.assertIn('buttons_max_one_filled', expected)
    self.assertIn('buttons_labels_single_line', expected)

  def test_validate_rubric_missing_questions(self):
    # Empty rubric
    result = calculate_score.calculate({'rubric': {}, 'components': []})
    self.assertFalse(result['valid'])
    self.assertLen(result['missing_questions'], 65)
    self.assertNotEmpty(result['warnings'])
    self.assertTrue(
        any(
            'INCOMPLETE RUBRIC WARNING' in warning
            for warning in result['warnings']
        )
    )

  def test_validate_rubric_partial_questions(self):
    rubric = {
        'typography_sentence_case': {'answer': 'Yes'},
        'color_surface_roles': {'answer': 'No'},
    }
    result = calculate_score.calculate({'rubric': rubric, 'components': []})
    self.assertFalse(result['valid'])
    self.assertNotIn('typography_sentence_case', result['missing_questions'])
    self.assertIn('color_drop_shadows', result['missing_questions'])

  def test_compute_scores_formula(self):
    # Test Hygiene vs Adherence weighting
    rubric = {
        # Hygiene Tier 0 (weight 10): passed
        'color_drop_shadows': {'answer': 'Yes'},
        # Hygiene Tier 1 (weight 5): failed
        'layout_hardware_clipping': {'answer': 'No'},
        # Adherence Tier 0 (weight 10): passed
        'typography_sentence_case': {'answer': 'Yes'},
        # Adherence Tier 2 (weight 3): failed
        'typography_title_large': {'answer': 'No'},
    }
    # Hygiene: 10 passed / 15 total = 67%
    # Adherence: 10 passed / 13 total = 77%
    # Final Score: round(67 * (77 / 100.0)) = 52%
    scores = calculate_score.calculate({'rubric': rubric, 'components': []})
    self.assertEqual(scores['hygiene_score'], 67)
    self.assertEqual(scores['adherence_score'], 77)
    self.assertEqual(scores['final_score'], 52)
    self.assertEqual(scores['score'], 52)
    self.assertEqual(scores['status'], 'NEEDS_REFINEMENT')
    # Absent subcategories should be 'N/A'
    self.assertEqual(scores['bottom_sheet_score'], 'N/A')
    self.assertEqual(scores['fab_score'], 'N/A')

  def test_absent_components_score_na(self):
    rubric = {
        'typography_sentence_case': {'answer': 'Yes'},
    }
    scores = calculate_score.calculate({'rubric': rubric, 'components': []})
    subcategories = calculate_score.RubricConfig.load().subcategories
    for field in subcategories:
      if field == 'typography_score':
        self.assertEqual(scores[field], 100)
      else:
        self.assertEqual(scores[field], 'N/A')

  def test_calculate_dict_input(self):
    # Create a complete assessment for foundational questions
    foundational_ids = calculate_score.get_expected_question_ids([])
    rubric = {
        question_id: {'answer': 'Yes'} for question_id in foundational_ids
    }
    data = {
        'components': [],
        'rubric': rubric,
    }
    result = calculate_score.calculate(data)
    self.assertTrue(result['valid'])
    self.assertEqual(result['hygiene_score'], 100)
    self.assertEqual(result['adherence_score'], 100)
    self.assertEqual(result['final_score'], 100)
    self.assertEqual(result['score'], 100)
    self.assertEqual(result['status'], 'PASSED')
    self.assertEmpty(result['missing_questions'])
    self.assertIn('Report', result['report'])

  def test_calculate_json_string_input(self):
    data = {
        'components': ['Bottom sheet'],
        'rubric': {
            'bottom_sheet_drag_handle': {'answer': 'Yes'},
        },
    }
    json_str = json.dumps(data)
    result = calculate_score.calculate(json_str)
    self.assertFalse(result['valid'])
    self.assertNotEmpty(result['warnings'])
    self.assertIn('bottom_sheet_score', result)

  def test_calculate_m3_score_tool(self):
    rubric = {
        'typography_sentence_case': {'answer': 'Yes'},
        'bottom_sheet_drag_handle': {'answer': 'No'},
    }
    result = calculate_score.calculate_m3_score(
        rubric=rubric, components=['Bottom sheet']
    )
    self.assertIn('hygiene_score', result)
    self.assertIn('adherence_score', result)
    self.assertIn('final_score', result)
    self.assertFalse(result['valid'])
    self.assertIn('bottom_sheet_score', result)

  def test_object_and_enum_compatibility(self):
    class FakeEnum:

      def __init__(self, value: str):
        self.value = value

    class FakeComponent:

      def __init__(self, name: str, mapped_name: str):
        self.name = name
        self.mapped_component = FakeEnum(mapped_name)

    class FakeRubricItem:

      def __init__(self, answer: str):
        self.answer = FakeEnum(answer)

    components = [FakeComponent('My Sheet', 'Bottom sheet')]
    expected = calculate_score.get_expected_question_ids(components)
    self.assertIn('bottom_sheet_drag_handle', expected)

    data = {
        'components': components,
        'rubric': {
            'typography_sentence_case': FakeRubricItem('Yes'),
            'bottom_sheet_drag_handle': FakeRubricItem('No'),
        },
    }
    result = calculate_score.calculate(data)
    self.assertIn('bottom_sheet_score', result)
    self.assertEqual(result['typography_score'], 100)
    self.assertEqual(result['bottom_sheet_score'], 0)

  def test_na_scores_report_formatting(self):
    # Denominator = 0 produces N/A
    result = calculate_score.calculate({'components': [], 'rubric': {}})
    self.assertEqual(result['hygiene_score'], 'N/A')
    self.assertEqual(result['adherence_score'], 'N/A')
    self.assertEqual(result['final_score'], 'N/A')
    self.assertEqual(result['score'], 'N/A')
    self.assertNotIn('N/A%', result['report'])

  def test_quality_supplemental_questions_and_final_score(self):
    config = calculate_score.RubricConfig.load()
    quality_ids = [
        qid for qid in config.questions if qid.startswith('quality_')
    ]
    self.assertLen(config.foundational_ids, 65)
    self.assertLen(quality_ids, 28)
    self.assertLen(config.component_questions, 38)
    total_component_questions = sum(
        len(qids) for qids in config.component_questions.values()
    )
    self.assertEqual(total_component_questions, 199)
    self.assertLen(config.questions, 292)
    for qid in quality_ids:
      self.assertNotIn(qid, config.foundational_ids)
    self.assertNotIn('quality', config.component_questions)

    self.assertEqual(
        config.questions['quality_color_theme_consistency']['metric'],
        'Adherence',
    )
    self.assertEqual(
        config.questions['quality_color_theme_consistency']['weight'], 5
    )
    self.assertEqual(
        config.questions['quality_adaptive_window_size_classes']['weight'], 10
    )
    self.assertEqual(
        config.questions['quality_typography_no_clipping_wrapping']['metric'],
        'Hygiene',
    )

    # Verify final_score gate when hygiene_score and adherence_score are 90%
    # (90 * 90 / 100 = 81 < 85 -> NEEDS_REFINEMENT)
    rubric = {
        'color_drop_shadows': {'answer': 'Yes'},  # Hygiene weight 10
        'color_gm_primary': {'answer': 'Yes'},  # Hygiene weight 10
        'elevation_tonal_variations': {'answer': 'Yes'},  # Hygiene weight 10
        'elevation_avoid_inline_shadows': {
            'answer': 'Yes'
        },  # Hygiene weight 10
        'layout_portrait_pane': {'answer': 'Yes'},  # Hygiene weight 5
        'layout_landscape_max_panes': {'answer': 'No'},  # Hygiene weight 5
        'typography_sentence_case': {'answer': 'Yes'},  # Adherence weight 10
        'color_surface_roles': {'answer': 'Yes'},  # Adherence weight 10
        'quality_adaptive_window_size_classes': {
            'answer': 'Yes'
        },  # Adherence weight 10
        'quality_color_theme_consistency': {
            'answer': 'Yes'
        },  # Adherence weight 5
        'quality_accessibility_screen_reader_labels': {
            'answer': 'Yes'
        },  # Adherence weight 5
        'quality_accessibility_prefers_reduced_motion': {
            'answer': 'Yes'
        },  # Adherence weight 5
        'quality_adaptive_hinge_foldable_avoidance': {
            'answer': 'No'
        },  # Adherence weight 5
    }
    res = calculate_score.calculate({'components': [], 'rubric': rubric})
    # Hygiene: 45/50 = 90%; Adherence: 45/50 = 90%; Final: round(90*0.90) = 81%
    self.assertEqual(res['hygiene_score'], 90)
    self.assertEqual(res['adherence_score'], 90)
    self.assertEqual(res['final_score'], 81)
    self.assertEqual(res['score'], 81)
    self.assertEqual(res['status'], 'NEEDS_REFINEMENT')

  def test_dynamic_scoring_config(self):
    references_directory = calculate_score.find_references_dir()
    config = calculate_score.RubricConfig.load(references_directory)
    self.assertEqual(config.pass_threshold, 85)
    self.assertEqual(config.weight_to_tier[10], 0)
    self.assertEqual(config.weight_to_tier[5], 1)
    self.assertEqual(config.weight_to_tier[3], 2)
    self.assertEqual(config.weight_to_tier[1], 3)
    self.assertIn('button_score', config.subcategories)
    self.assertIn('typography_score', config.subcategories)
    self.assertIn('app_bar_score', config.subcategories)
    self.assertIn('aurora_score', config.subcategories)
    self.assertIn('bottom_sheet_score', config.subcategories)
    self.assertIn('bottom-sheet', config.subcategories['bottom_sheet_score'])
    self.assertIn('buttons', config.subcategories['button_score'])
    self.assertNotEmpty(config.foundational_ids)
    self.assertNotEmpty(config.questions)

  def test_aurora_score_deterministic_calculation(self):
    expected_default_subcategories = {
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
    }
    self.assertEqual(
        calculate_score._DEFAULT_SUBCATEGORIES, expected_default_subcategories
    )

    expected_ids = calculate_score.get_expected_question_ids(
        [{'name': 'AI Prompt', 'mapped_component': 'Aurora prompt field'}]
    )
    aurora_question_ids = (
        'aurora_energy_max_one',
        'aurora_energy_subtle',
        'aurora_energy_signal_ai',
        'aurora_small_container_tonal_fill',
        'aurora_large_container_sharp_edge',
        'aurora_energy_extend_edges',
        'aurora_4c_brand_ai_moments',
        'aurora_neural_gemini_only',
        'aurora_text_icon_contrast',
        'aurora_media_content_clear',
    )
    for qid in aurora_question_ids:
      self.assertIn(qid, expected_ids)

    evaluated_result = calculate_score.calculate({
        'components': [
            {'name': 'AI Prompt', 'mapped_component': 'Aurora prompt field'}
        ],
        'rubric': {
            'aurora_energy_max_one': {'answer': 'Yes'},
            'aurora_energy_subtle': {'answer': 'No'},
        },
    })
    self.assertEqual(evaluated_result['aurora_score'], 67)

    na_result = calculate_score.calculate({
        'components': [],
        'rubric': {
            'aurora_energy_max_one': {'answer': 'N/A'},
            'aurora_energy_subtle': {'answer': 'N/A'},
        },
    })
    self.assertEqual(na_result['aurora_score'], 'N/A')

    absent_result = calculate_score.calculate({'components': [], 'rubric': {}})
    self.assertEqual(absent_result['aurora_score'], 'N/A')

    references_directory = calculate_score.find_references_dir()
    with tempfile.TemporaryDirectory() as temp_dir:
      shutil.copy(
          os.path.join(references_directory, 'rubric.md'),
          os.path.join(temp_dir, 'rubric.md'),
      )
      os.makedirs(os.path.join(temp_dir, 'rubrics'), exist_ok=True)
      shutil.copy(
          os.path.join(references_directory, 'rubrics', 'aurora.md'),
          os.path.join(temp_dir, 'rubrics', 'aurora.md'),
      )
      fallback_config = calculate_score.RubricConfig.load(temp_dir)
      self.assertEqual(
          fallback_config.subcategories, expected_default_subcategories
      )
      fallback_result = calculate_score.calculate(
          {
              'components': [],
              'rubric': {
                  'aurora_energy_max_one': {'answer': 'Yes'},
                  'aurora_energy_subtle': {'answer': 'No'},
              },
          },
          references_directory=temp_dir,
      )
      self.assertEqual(fallback_result['aurora_score'], 67)

  def test_invalid_explicit_dir_raises(self):
    with self.assertRaises(FileNotFoundError):
      calculate_score.find_references_dir('/non/existent/path/for/test')

  def test_camel_case_mapped_component_and_alias_isolation(self):
    # Verify camelCase `mappedComponent` activates Toolbar rubric, while
    # `functionalAliases` (`Navigation bar`, `Chip`, `Tabs`) do NOT activate
    # false-positive component rubrics.
    components = [{
        'id': 'comp_01',
        'name': 'Bottom Floating Navigation Pill',
        'mappedComponent': 'Toolbar',
        'functionalAliases': ['Floating toolbar', 'Navigation bar', 'Tabs'],
        'subcomponents': [{
            'id': 'comp_01_sub_01',
            'name': 'Photos Destination Icon Button',
            'mappedComponent': 'Icon button',
            'functionalAliases': ['Icon'],
        }],
    }]
    expected = calculate_score.get_expected_question_ids(components)
    # Toolbar and Icon button rubrics should be included
    self.assertIn('toolbar_floating_shape_token', expected)
    self.assertIn('icon_button_usage', expected)
    # Navigation bar and Tabs rubrics must NOT be triggered by functionalAliases
    self.assertNotIn('nav_bars_bottom_location', expected)
    self.assertNotIn('tabs_active_indicator', expected)

  def test_foundational_subcategories_use_only_their_own_rubric(self):
    # Regression test for b/568561430: prose at the top of
    # assessment_instruction.md was parsed as App bar aliases, which folded
    # app-bars questions into the foundational subscores.
    subcategories = calculate_score.RubricConfig.load().subcategories
    self.assertEqual(subcategories['color_score'], ('color',))
    self.assertEqual(subcategories['layout_score'], ('layout',))
    self.assertEqual(subcategories['typography_score'], ('typography',))

  def test_document_prose_is_not_registered_as_component_alias(self):
    component_to_slug = calculate_score.RubricConfig.load().component_to_slug
    for prose_alias in ('color', 'elevation', 'layout', 'typography'):
      self.assertNotIn(prose_alias, component_to_slug)
    self.assertEmpty([alias for alias in component_to_slug if len(alias) > 40])

  def test_wrapped_component_mapping_items_register_every_alias(self):
    # mdformat wraps long mapping list items onto indented continuation lines;
    # every alias in those items must still route to its rubric.
    config = calculate_score.RubricConfig.load()
    for component_name, rubric_slug in (
        ('App bar', 'app-bars'),
        ('Large App Bar', 'app-bars'),
        ('Aurora response carousel', 'aurora'),
        ('Aurora suggestions', 'aurora'),
        ('Outlined button', 'buttons'),
        ('Text button', 'buttons'),
    ):
      with self.subTest(component_name=component_name):
        expected_ids = config.get_expected_question_ids(
            [{'mapped_component': component_name}]
        )
        self.assertContainsSubset(
            config.component_questions[rubric_slug], expected_ids
        )

  def test_app_bar_answers_do_not_affect_foundational_subscores(self):
    config = calculate_score.RubricConfig.load()
    rubric = {
        question_id: {'answer': 'Yes'}
        for question_id in config.foundational_ids
    }
    rubric.update({
        question_id: {'answer': 'No'}
        for question_id in config.component_questions['app-bars']
    })
    result = calculate_score.calculate(
        {'components': ['App bar'], 'rubric': rubric}
    )
    self.assertEqual(result['color_score'], 100)
    self.assertEqual(result['typography_score'], 100)
    self.assertEqual(result['layout_score'], 100)
    self.assertEqual(result['app_bar_score'], 0)

  def test_sibling_component_rubrics_do_not_feed_component_subscores(self):
    # Each component subscore covers only the rubric file listed for it in
    # scoring_instruction.md and is 'N/A' when that component is absent, as the
    # Design Auditor schema expects.
    config = calculate_score.RubricConfig.load()
    for component_name, rubric_slug, subcategory in (
        ('Bottom App Bar', 'bottom-app-bar', 'app_bar_score'),
        ('Button group', 'button-group', 'button_score'),
        ('Icon button', 'icon-button', 'button_score'),
        ('Radio button', 'radio-button', 'button_score'),
        ('Segmented button', 'segmented-button', 'button_score'),
        ('Split button', 'split-button', 'button_score'),
        ('Navigation drawer', 'navigation-drawer', 'navigation_bar_score'),
        ('Navigation rail', 'navigation-rail', 'navigation_bar_score'),
        ('Side sheet', 'side-sheet', 'bottom_sheet_score'),
    ):
      with self.subTest(component_name=component_name):
        rubric = {
            question_id: {'answer': 'No'}
            for question_id in config.component_questions[rubric_slug]
        }
        result = calculate_score.calculate(
            {'components': [component_name], 'rubric': rubric}
        )
        self.assertEqual(result[subcategory], 'N/A')

  def test_modular_token_references_and_no_legacy_carbon_bloat(self):
    references_directory = calculate_score.find_references_dir()
    skill_directory = os.path.dirname(references_directory)

    carbon_path = os.path.join(references_directory, 'carbon.md')
    self.assertFalse(os.path.exists(carbon_path))

    modular_files = (
        'tokens/color_and_contrast.md',
        'tokens/typography_and_shape.md',
        'tokens/spacing_elevation_and_states.md',
        'tokens/component_geometry_quickref.md',
    )
    for relative_path in modular_files:
      file_path = os.path.join(references_directory, relative_path)
      self.assertTrue(
          os.path.exists(file_path),
          f'Missing modular token reference file: {relative_path}',
      )
      file_size_bytes = os.path.getsize(file_path)
      self.assertGreater(file_size_bytes, 0)
      self.assertLess(file_size_bytes, 8000)
      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
      self.assertNotIn('{#isPasted}', content)

    skill_md_path = os.path.join(skill_directory, 'SKILL.md')
    with open(skill_md_path, 'r', encoding='utf-8') as f:
      skill_content = f.read()
    self.assertNotIn('carbon.md', skill_content)

    assessment_instruction_path = os.path.join(
        references_directory, 'assessment_instruction.md'
    )
    with open(assessment_instruction_path, 'r', encoding='utf-8') as f:
      assessment_content = f.read()
    self.assertNotIn('carbon.md', assessment_content)

  def test_no_benchmark_screenshot_filenames_in_skill_or_rubrics(self):
    references_directory = calculate_score.find_references_dir()
    skill_directory = os.path.dirname(references_directory)
    config = calculate_score.RubricConfig.load(references_directory)

    eval_files = (
        os.path.join(skill_directory, 'sample_evals', 'EVAL.txtpb'),
        os.path.join(skill_directory, 'detector', 'EVAL.txtpb'),
    )
    benchmark_pngs: set[str] = set()
    eval_case_ids: set[str] = set()
    for eval_path in eval_files:
      if os.path.exists(eval_path):
        with open(eval_path, 'r', encoding='utf-8') as f:
          eval_text = f.read()
          benchmark_pngs.update(
              calculate_score.re.findall(r'\b[a-zA-Z0-9_\-]+\.png\b', eval_text)
          )
          eval_case_ids.update(
              calculate_score.re.findall(r'name:\s*"([^"]+)"', eval_text)
          )
    eval_case_ids -= set(config.questions.keys())
    eval_case_ids.discard('material_visual_assessor_eval_sample')
    eval_case_ids.discard('ui_detector_eval')
    eval_case_ids.discard('ui-detector')
    eval_case_ids.discard('material-visual-assessor')
    self.assertNotEmpty(benchmark_pngs)

    markdown_paths = [
        os.path.join(skill_directory, 'SKILL.md'),
        os.path.join(skill_directory, 'detector', 'SKILL.md'),
    ]
    for pattern in (
        os.path.join(skill_directory, 'detector', 'references', '*.md'),
        os.path.join(references_directory, '*.md'),
        os.path.join(references_directory, 'tokens', '*.md'),
        os.path.join(references_directory, 'rubrics', '*.md'),
    ):
      markdown_paths.extend(sorted(calculate_score.glob.glob(pattern)))

    leaked_references: list[str] = []
    for md_path in markdown_paths:
      if not os.path.exists(md_path):
        continue
      with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
      rel_path = os.path.relpath(md_path, skill_directory)
      found_pngs = set(
          calculate_score.re.findall(r'\b[a-zA-Z0-9_\-]+\.png\b', content)
      )
      for png in sorted(found_pngs | (benchmark_pngs & found_pngs)):
        leaked_references.append(f'{rel_path}: {png}')
      for case_id in sorted(eval_case_ids):
        if case_id in content:
          leaked_references.append(f'{rel_path}: {case_id}')

    self.assertEmpty(
        leaked_references,
        'Benchmark screenshot filenames or eval case IDs must not appear in'
        f' skill or rubric markdown files: {leaked_references}',
    )


if __name__ == '__main__':
  absltest.main()
