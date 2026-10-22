#!/usr/bin/env python3
"""CLI entry point for NotebookOS HTML Artifact Validator.

Usage:
    python3 validate_html_artifact.py <path_to_html> [--artifacts-dir DIR]

All check logic lives in validator.py; this file is only the CLI wrapper.
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_validator = importlib.import_module("validator")
validate_html_artifact = _validator.validate_html_artifact


def main() -> int:
  import argparse  # pylint: disable=g-import-not-at-top

  parser = argparse.ArgumentParser(
      description=(
          "Validate NotebookOS HTML Artifacts for structure, JS targets,"
          " JSON syntax, inline handler wiring, and visual rendering."
      )
  )
  parser.add_argument("html_file", help="Path to the HTML file to validate")
  parser.add_argument(
      "--artifacts-dir",
      help="Path to artifacts directory for checking relative resource files",
      default=None,
  )
  args = parser.parse_args()

  if not os.path.exists(args.html_file):
    print(f"FAILED: File not found: {args.html_file}", file=sys.stderr)
    return 1

  findings = validate_html_artifact(
      args.html_file,
      artifacts_dir=args.artifacts_dir,
  )

  if findings:
    errors = [f for f in findings if getattr(f, "severity", "ERROR") == "ERROR"]
    warnings = [
        f
        for f in findings
        if getattr(f, "severity", "ERROR") == "WARNING"
        and getattr(f, "category", "") != "VALIDATOR_ENVIRONMENT_WARNING"
    ]
    environment = [
        f
        for f in findings
        if getattr(f, "category", "") == "VALIDATOR_ENVIRONMENT_WARNING"
    ]
    cosmetics = [
        f for f in findings if getattr(f, "severity", "ERROR") == "COSMETIC"
    ]

    blocking = errors or warnings

    if blocking:
      print("=== HTML ARTIFACT VALIDATION FAILED ===")
    else:
      print("=== HTML ARTIFACT VALIDATION PASSED (with notes) ===")

    if errors:
      print("--- FUNCTIONAL & STRUCTURAL ERRORS (MUST FIX) ---")
      for i, f in enumerate(errors, 1):
        print(f"{i}. {f}")
    if warnings:
      if errors:
        print("")
      print("--- FUNCTIONAL WARNINGS (MUST FIX) ---")
      for i, f in enumerate(warnings, 1):
        print(f"{i}. {f}")
    if cosmetics:
      if errors or warnings:
        print("")
      print("--- COSMETIC & DESIGN ISSUES (STYLE / ANTI-PATTERNS) ---")
      for i, f in enumerate(cosmetics, 1):
        print(f"{i}. {f}")
    if environment:
      if errors or warnings or cosmetics:
        print("")
      print(
          "--- VALIDATOR ENVIRONMENT (CHECK DID NOT RUN; NOT AN ARTIFACT"
          " BUG) ---"
      )
      for i, f in enumerate(environment, 1):
        print(f"{i}. {f}")
    print("=======================================")
    return 1 if blocking else 0
  else:
    print("=== HTML ARTIFACT VALIDATION PASSED ===")
    return 0


if __name__ == "__main__":
  sys.exit(main())
