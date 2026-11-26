#!/usr/bin/env python3
"""Build the browsable rule index from the rule files."""

import argparse
import difflib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "rules"
INDEX = RULES / "README.md"
RULE_ID = re.compile(r"[A-Z]+-[0-9]+")
FIELD_BREAK = re.compile(r"\n[ \t]*\n|\n(?=\*\*[A-Za-z ]+:\*\*)")


def field(blocks: list[str], name: str, path: Path) -> str:
    label = f"**{name}:**"
    matches = [block[len(label):] for block in blocks if block.startswith(label)]
    if len(matches) == 1:
        value = " ".join(line.strip() for line in matches[0].splitlines()).strip()
        if value:
            return value
    raise ValueError(f"{path.relative_to(ROOT)}: expected one non-empty {name} field")


def render() -> str:
    lines = [
        "# Rule index",
        "",
        "Search this page by rule ID or description. Each ID links to the full rule",
        "and its criteria.",
        "",
        "To regenerate this index, run `python3 scripts/generate_rule_index.py` from",
        "the repository root.",
        "",
    ]
    files = sorted(
        path for path in RULES.glob("*.md") if path.name not in {INDEX.name, "_template.md"}
    )
    if not files:
        raise ValueError("no rule files found")

    previous_prefix = None
    for path in files:
        # Rule fields are paragraphs, so descriptions can wrap onto multiple lines.
        blocks = FIELD_BREAK.split(path.read_text(encoding="utf-8"))
        rule_id = field(blocks, "Rule ID", path)
        if not RULE_ID.fullmatch(rule_id):
            raise ValueError(f"{path.relative_to(ROOT)}: invalid Rule ID {rule_id!r}")
        if rule_id != path.stem:
            raise ValueError(
                f"{path.relative_to(ROOT)}: Rule ID {rule_id!r} does not match filename"
            )
        description = field(blocks, "Description", path)
        prefix = rule_id.split("-", 1)[0]
        if prefix != previous_prefix:
            if previous_prefix is not None:
                lines.append("")
            lines.extend([f"## {prefix}", ""])
            previous_prefix = prefix
        lines.append(f"- [{rule_id}]({path.name}): {description}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the committed index is out of date")
    args = parser.parse_args()
    try:
        expected = render()
        if not args.check:
            INDEX.write_text(expected, encoding="utf-8")
            print(f"Updated {INDEX.relative_to(ROOT)}")
            return 0

        try:
            actual = INDEX.read_text(encoding="utf-8")
        except FileNotFoundError:
            actual = ""
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    if actual == expected:
        return 0

    sys.stderr.writelines(difflib.unified_diff(
        actual.splitlines(keepends=True),
        expected.splitlines(keepends=True),
        fromfile=str(INDEX.relative_to(ROOT)),
        tofile="generated index",
    ))
    print(
        "Run python3 scripts/generate_rule_index.py from the repository root to update the index.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
