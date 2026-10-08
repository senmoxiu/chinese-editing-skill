"""Validate packaging and reference integrity; does not score model behavior."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "chinese-editing"


def validate(root=ROOT):
    errors = []
    skill = root / "skills" / "chinese-editing"

    def require(condition, message):
        if not condition:
            errors.append(message)

    entry = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", entry, re.S)
    require(match is not None, "SKILL.md: missing YAML frontmatter")
    if match:
        meta = yaml.safe_load(match.group(1))
        require(isinstance(meta, dict), "Frontmatter must be a mapping")
        if isinstance(meta, dict):
            require(meta.get("name") == skill.name, "Skill name and directory differ")
            desc = meta.get("description")
            require(isinstance(desc, str) and 0 < len(desc) <= 1024,
                    "Description must be a nonempty string <= 1024 characters")
            require(set(meta) <= {"name", "description", "license", "metadata", "allowed-tools"},
                    "Unsupported frontmatter field")

    ui = yaml.safe_load((skill / "agents" / "openai.yaml").read_text(encoding="utf-8"))
    require("$chinese-editing" in ui["interface"]["default_prompt"],
            "Default prompt must name the skill")
    require(25 <= len(ui["interface"]["short_description"]) <= 64,
            "UI description must contain 25-64 characters")

    # Validate local file links; strip fenced/inline examples so illustrative
    # example links are not mistaken for repository references.
    markdown = list(root.rglob("*.md"))
    for path in markdown:
        if ".git" in path.relative_to(root).parts:
            continue
        raw = path.read_bytes()
        require(not raw.startswith(b"\xef\xbb\xbf"), f"{path.name}: unexpected UTF-8 BOM")
        text = raw.decode("utf-8")
        text = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)
        text = re.sub(r"`+[^`\n]*`+", "", text)
        for link in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
            parsed = urlsplit(link)
            if parsed.scheme or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            require(target.is_relative_to(root.resolve()), f"{path.name}: link escapes repository: {link}")
            require(target.exists(), f"{path.name}: missing link target: {link}")

    sources = (skill / "references" / "sources.md").read_text(encoding="utf-8")
    pins = re.findall(r"github\.com/[^/]+/[^/]+/tree/([0-9a-f]{40})", sources)
    require(len(set(pins)) == 4, "Expected four pinned reference projects")

    notes = root / ".agents" / "notes"
    allowed_states = {"proposed", "implemented", "rejected", "archived"}
    allowed_classes = {"feature", "bug-fix", "simplification", "architecture", "process", "testing"}
    for path in notes.rglob("*.md"):
        parts = path.relative_to(notes).parts
        require(len(parts) == 3 and parts[0] in allowed_states and parts[1] in allowed_classes,
                f"Invalid note path: {path.name}")
        text = path.read_text(encoding="utf-8")
        state = parts[0]
        require(text.startswith("# Agent Note: "), f"Missing note title: {path.name}")
        lines = text.splitlines()
        require(len(lines) > 2 and lines[1] == "" and lines[2].startswith(f"Status: {state}"),
                f"Invalid note header: {path.name}")
        for section in ["## Problem", "## Alternatives considered"]:
            require(section in text, f"Missing {section}: {path.name}")
        if state == "implemented":
            require("## Decision" in text and "## Consequences" in text, f"Incomplete implemented note: {path.name}")
            require(not any(h in text for h in ["## Proposal", "## Acceptance criteria", "## Migration plan"]),
                    f"Implemented note still contains proposal sections: {path.name}")

    return errors, len(markdown)


if __name__ == "__main__":
    try:
        problems, files = validate()
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(f"Validation error: {exc}", file=sys.stderr)
        sys.exit(1)
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    if problems:
        sys.exit(1)
    print(f"PASS: package metadata, local file links, source pins, notes; {files} Markdown files")
    print("Not checked: model behavior, remote link availability, rendered document layout")
