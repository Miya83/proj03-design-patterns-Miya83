#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Project 3: Design Patterns
"""
import json
from pathlib import Path


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Replace placeholders with proj03 variant keys
    domain = variant["domain"]
    variant_patterns = variant["variant_patterns"]

    assignment = template
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])
    assignment = assignment.replace("{{DOMAIN_NAME}}", domain["name"])
    assignment = assignment.replace("{{DOMAIN_CONTEXT}}", domain["context"])
    assignment = assignment.replace("{{DOMAIN_EXAMPLES}}", ", ".join(domain["examples"]))
    
    # Variant patterns
    assignment = assignment.replace("{{VARIANT_PATTERN_1}}", variant_patterns[0]["name"])
    assignment = assignment.replace("{{VARIANT_PATTERN_1_DESC}}", variant_patterns[0]["description"])
    assignment = assignment.replace("{{VARIANT_PATTERN_1_CATEGORY}}", variant_patterns[0]["category"])
    assignment = assignment.replace("{{VARIANT_PATTERN_2}}", variant_patterns[1]["name"])
    assignment = assignment.replace("{{VARIANT_PATTERN_2_DESC}}", variant_patterns[1]["description"])
    assignment = assignment.replace("{{VARIANT_PATTERN_2_CATEGORY}}", variant_patterns[1]["category"])
    
    # All patterns list
    assignment = assignment.replace("{{ALL_PATTERNS}}", ", ".join(variant["all_patterns"]))
    assignment = assignment.replace("{{TOTAL_PATTERNS}}", str(variant["total_patterns"]))

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
