#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0",
# ]
# requires-python = ">=3.9"
# ///
"""
Backlog Filter Batch Processor

Processes multiple backlog items from CSV/JSON files and generates prioritization reports.

Usage:
    uv run scripts/batch_filter.py --input backlog.csv --output analysis.md
    uv run scripts/batch_filter.py --input items.json --format json
    uv run scripts/batch_filter.py --help

Input Formats:
    CSV: Columns should include 'name', 'description', and optionally 'dependencies', 'size', 'priority'
    JSON: Array of objects with 'name', 'description', and optional fields

Output:
    Markdown report with clarity assessments, sequencing recommendations, and action plans
"""

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.table import Table


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze backlog items by clarity level and generate prioritization recommendations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --input sprint_backlog.csv --output analysis.md
  %(prog)s --input roadmap.json --format json
  %(prog)s --input items.csv --dry-run

Exit Codes:
  0 - Success
  1 - Input file not found or invalid format
  2 - Invalid arguments
  3 - Output write error
        """
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to input file (CSV or JSON)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Path to output markdown file (default: stdout)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["csv", "json", "auto"],
        default="auto",
        help="Input file format (default: auto-detect from extension)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate input and show summary without generating full report"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print progress messages to stderr"
    )
    return parser.parse_args()


def detect_format(file_path: Path, explicit_format: str) -> str:
    """Detect file format from extension or explicit parameter."""
    if explicit_format != "auto":
        return explicit_format
    
    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        return "csv"
    elif suffix in [".json", ".js"]:
        return "json"
    else:
        raise ValueError(
            f"Cannot auto-detect format for '{file_path}'. "
            f"Use --format csv or --format json explicitly."
        )


def load_csv_items(file_path: Path) -> list[dict[str, Any]]:
    """Load backlog items from CSV file."""
    items = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Normalize column names
                item = {k.strip().lower(): v.strip() if v else "" for k, v in row.items()}
                if "name" not in item or not item["name"]:
                    print(
                        f"Warning: Skipping row without 'name' field: {row}",
                        file=sys.stderr
                    )
                    continue
                items.append(item)
    except FileNotFoundError:
        print(f"Error: Input file not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except csv.Error as e:
        print(f"Error: Invalid CSV format: {e}", file=sys.stderr)
        sys.exit(1)
    
    if not items:
        print("Error: No valid items found in CSV file", file=sys.stderr)
        sys.exit(1)
    
    return items


def load_json_items(file_path: Path) -> list[dict[str, Any]]:
    """Load backlog items from JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}", file=sys.stderr)
        sys.exit(1)
    
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and "items" in data:
        items = data["items"]
    else:
        print(
            "Error: JSON must be an array of items or an object with 'items' key",
            file=sys.stderr
        )
        sys.exit(1)
    
    # Validate and normalize items
    normalized = []
    for item in items:
        if not isinstance(item, dict):
            print(f"Warning: Skipping non-object item: {item}", file=sys.stderr)
            continue
        if "name" not in item or not item.get("name"):
            print(f"Warning: Skipping item without 'name': {item}", file=sys.stderr)
            continue
        normalized.append({k.lower(): str(v) if v is not None else "" for k, v in item.items()})
    
    if not normalized:
        print("Error: No valid items found in JSON file", file=sys.stderr)
        sys.exit(1)
    
    return normalized


def assess_clarity(item: dict[str, Any]) -> str:
    """
    Assess clarity level based on item attributes.
    
    Heuristics:
    - LOW: Vague descriptions, no acceptance criteria, new domain
    - MEDIUM: Some details but missing key information
    - HIGH: Specific, testable, familiar domain
    """
    description = item.get("description", "").lower()
    name = item.get("name", "").lower()
    
    # Low clarity indicators
    low_indicators = [
        "investigate", "research", "explore", "spike", "prototype",
        "figure out", "understand", "look into", "maybe", "possibly",
        "tbd", "todo", "???", "..."
    ]
    
    # High clarity indicators
    high_indicators = [
        "implement", "add", "create", "build", "develop",
        "fix", "update", "migrate", "integrate",
        "given", "when", "then",  # Gherkin syntax
        "acceptance criteria", "definition of done"
    ]
    
    description_text = f"{name} {description}"
    
    low_count = sum(1 for indicator in low_indicators if indicator in description_text)
    high_count = sum(1 for indicator in high_indicators if indicator in description_text)
    
    # Check for specific details
    has_specifics = any([
        len(description) > 100,  # Detailed description
        "://" in description,     # URLs/references
        "#" in description,       # Issue references
        "@" in description,       # People assigned
        item.get("acceptance_criteria", ""),
        item.get("test_cases", ""),
    ])
    
    if low_count >= 2 or (low_count > high_count and not has_specifics):
        return "LOW"
    elif high_count >= 2 and has_specifics:
        return "HIGH"
    else:
        return "MEDIUM"


def generate_recommendation(clarity: str, item: dict[str, Any]) -> dict[str, str]:
    """Generate action recommendation based on clarity level."""
    recommendations = {
        "LOW": {
            "action": "Do not estimate; run timeboxed experiment or discovery spike",
            "estimation": "DO NOT ESTIMATE - insufficient understanding",
            "timeline": "1-3 day discovery sprint before commitment"
        },
        "MEDIUM": {
            "action": "Timebox refinement session to clarify requirements",
            "estimation": "Provide range estimate with explicit assumptions",
            "timeline": "Include 20-30% buffer for unknown factors"
        },
        "HIGH": {
            "action": "Proceed with implementation planning",
            "estimation": "Confident estimate; treat as commitment",
            "timeline": "Can be committed to current/next iteration"
        }
    }
    return recommendations.get(clarity, recommendations["MEDIUM"])


def generate_markdown_report(items: list[dict[str, Any]], dry_run: bool = False) -> str:
    """Generate markdown analysis report."""
    analyzed = []
    for item in items:
        clarity = assess_clarity(item)
        recommendation = generate_recommendation(clarity, item)
        analyzed.append({
            **item,
            "clarity": clarity,
            **recommendation
        })
    
    # Sort by clarity (LOW first for risk mitigation)
    clarity_order = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
    analyzed.sort(key=lambda x: (clarity_order[x["clarity"]], x.get("name", "")))
    
    # Count by clarity
    clarity_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
    for item in analyzed:
        clarity_counts[item["clarity"]] += 1
    
    if dry_run:
        # Summary only for dry run
        lines = [
            "## Backlog Filter Analysis (Dry Run)",
            "",
            "### Summary",
            f"- **Total Items:** {len(analyzed)}",
            f"- **Requires Discovery (LOW):** {clarity_counts['LOW']}",
            f"- **Needs Refinement (MEDIUM):** {clarity_counts['MEDIUM']}",
            f"- **Ready to Proceed (HIGH):** {clarity_counts['HIGH']}",
            "",
            "⚠️  This is a dry run. Remove --dry-run flag to generate full report."
        ]
        return "\n".join(lines)
    
    # Full report
    lines = [
        "## Backlog Filter Analysis",
        "",
        "### Summary",
        f"- **Total Items:** {len(analyzed)}",
        f"- **Ready to Proceed:** {clarity_counts['HIGH']} (High clarity)",
        f"- **Needs Refinement:** {clarity_counts['MEDIUM']} (Medium clarity)",
        f"- **Requires Discovery:** {clarity_counts['LOW']} (Low clarity)",
        "",
        "### Item Analysis",
        ""
    ]
    
    for idx, item in enumerate(analyzed, 1):
        lines.extend([
            f"#### {idx}. {item.get('name', 'Unnamed Item')}",
            f"- **Clarity Level:** {item['clarity']}",
            f"- **Rationale:** Assessed based on description specificity and known patterns",
            f"- **Dependencies:** {item.get('dependencies', 'Not specified')}",
            f"- **Recommended Action:** {item['action']}",
            f"- **Estimation Guidance:** {item['estimation']}",
            f"- **Timeline:** {item['timeline']}",
            ""
        ])
    
    # Sequencing recommendations
    lines.extend([
        "### Recommended Sequence",
        ""
    ])
    
    sequence_num = 1
    for item in analyzed:
        reason = ""
        if item["clarity"] == "LOW":
            reason = "Address first to expose risks early"
        elif item["clarity"] == "MEDIUM":
            reason = "Refine before high-clarity items to reduce uncertainty"
        else:
            reason = "Ready for immediate implementation"
        
        lines.append(f"{sequence_num}. **{item.get('name')}** - {reason}")
        sequence_num += 1
    
    lines.extend([
        "",
        "### Next Steps",
        "1. Review LOW clarity items and schedule discovery spikes",
        "2. Schedule refinement sessions for MEDIUM clarity items",
        "3. Commit HIGH clarity items to upcoming iteration",
        "4. Re-assess after discovery work completes",
        "",
        "---",
        "*Generated by Backlog Filter Skill*"
    ])
    
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    console = Console(stderr=True)
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    
    # Detect format and load items
    try:
        file_format = detect_format(input_path, args.format)
        if args.verbose:
            console.print(f"[dim]Detected format: {file_format}[/dim]")
        
        if file_format == "csv":
            items = load_csv_items(input_path)
        else:
            items = load_json_items(input_path)
        
        if args.verbose:
            console.print(f"[dim]Loaded {len(items)} items[/dim]")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
    
    # Generate report
    report = generate_markdown_report(items, dry_run=args.dry_run)
    
    # Output
    if args.output:
        try:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)
            if args.verbose:
                console.print(f"[green]Report written to {output_path}[/green]")
        except IOError as e:
            print(f"Error: Could not write output file: {e}", file=sys.stderr)
            sys.exit(3)
    else:
        print(report)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
