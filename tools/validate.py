#!/usr/bin/env python3
"""Validate a BringMeBack Markdown corpus, optionally against the common/public corpus.

Usage:
  pip install -r requirements.txt
  python tools/validate.py ../bringmeback-content --mode public
  python tools/validate.py ../bringmeback-private --mode private --public-dir ../bringmeback-content

The validator checks file metadata, basic access boundaries and duplicate IDs. For
cross-repository relationships pass --public-dir; private relations otherwise may
point to external public IDs not present in the private repository.
"""
import argparse
import pathlib
import re
import sys
import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = __import__("json").loads((ROOT / "schemas/record.schema.json").read_text(encoding="utf-8"))

def records(repo):
    for path in sorted((repo / "content").rglob("*.md")):
        raw = path.read_text(encoding="utf-8")
        if not raw.startswith("---\n") or "\n---\n" not in raw[4:]:
            yield path, None, "missing YAML frontmatter"
            continue
        head = raw[4:].split("\n---\n", 1)[0]
        try:
            value = yaml.safe_load(head)
            if not isinstance(value, dict):
                raise ValueError("frontmatter is not a mapping")
            yield path, value, None
        except (yaml.YAMLError, ValueError) as exc:
            yield path, None, str(exc)

def validate(repo, mode, public_dir=None):
    errors = []
    entries = {}
    for path, data, err in records(repo):
        if err:
            errors.append(f"{path}: {err}")
            continue
        for issue in Draft202012Validator(SCHEMA).iter_errors(data):
            errors.append(f"{path}: {issue.message}")
        identity = data.get("id")
        if identity in entries:
            errors.append(f"{path}: duplicate ID {identity} (previously {entries[identity]})")
        entries[identity] = path
        if mode == "public" and (data.get("access") != "public" or data.get("sensitivity") != "ordinary" or data.get("publication") == "internal"):
            errors.append(f"{path}: unsafe metadata for public corpus")
        if mode == "public" and data.get("extends"):
            errors.append(f"{path}: public corpus must never reference private overlays")
        if mode == "private" and (data.get("access") != "private" or data.get("publication") != "internal"):
            errors.append(f"{path}: unsafe metadata for private corpus")
        if mode == "private" and data.get("sensitivity") != "intimate":
            errors.append(f"{path}: private records must declare sensitivity: intimate")
    public_ids = set()
    if public_dir:
        for path, data, err in records(public_dir):
            if not err and isinstance(data, dict):
                public_ids.add(data.get("id"))
    known = set(entries) | public_ids
    for path, data, err in records(repo):
        if err or not data:
            continue
        links = data.get("related_ids", []) + ([data["extends"]] if data.get("extends") else [])
        for target in links:
            if target not in known:
                if mode == "private" and not public_dir:
                    continue
                errors.append(f"{path}: missing related ID {target}")
        if mode == "public" and any(re.search(r"(private|intimate|overlay)", target, re.I) for target in links):
            errors.append(f"{path}: suspicious public cross-reference")
    return errors, len(entries)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=pathlib.Path)
    parser.add_argument("--mode", required=True, choices=["public", "private"])
    parser.add_argument("--public-dir", type=pathlib.Path)
    a = parser.parse_args()
    problems, total = validate(a.repo.resolve(), a.mode, a.public_dir.resolve() if a.public_dir else None)
    for problem in problems:
        print("ERROR:", problem)
    print(f"Validated {total} records, {len(problems)} error(s)")
    sys.exit(bool(problems))
