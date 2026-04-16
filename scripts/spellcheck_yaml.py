#!/usr/bin/env python3
r"""
Spellcheck YAML files in the repository.

Usage:
    python scripts/spellcheck_yaml.py [--words PATH] [--add-word WORD] [--report FILE]

Note: This tool is forced to only scan the repository's `scripts/data` directory.
It resolves the directory relative to the script location so it works on any clone.

Examples:
    python scripts/spellcheck_yaml.py
    python scripts/spellcheck_yaml.py --words scripts/spellcheck_words.txt
    python scripts/spellcheck_yaml.py --add-word MyCustomWord
"""
import argparse
import os
import re
import sys
from pathlib import Path

import yaml
from spellchecker import SpellChecker

WORD_RE = re.compile(r"[A-Za-z']{2,}")

# Divider used between files in reports
DIVIDER = '=' * 50


def load_custom_words(path: Path):
    words = set()
    if path and path.exists():
        for line in path.read_text(encoding='utf-8').splitlines():
            w = line.strip()
            if not w or w.startswith('#'):
                continue
            words.add(w)
    return words


def extract_strings(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from extract_strings(v)
    elif isinstance(obj, list):
        for item in obj:
            yield from extract_strings(item)
    elif isinstance(obj, str):
        yield obj


def tokenize(text: str):
    return WORD_RE.findall(text)


def is_skip(word: str):
    # Skip words that look like acronyms or numerics
    if word.isdigit():
        return True
    if word.isupper() and len(word) <= 4:
        return True
    return False


def find_yaml_files(root: Path):
    for p in root.rglob('*.yml'):
        yield p
    for p in root.rglob('*.yaml'):
        yield p


def main():
    p = argparse.ArgumentParser()
    # --path is accepted for compatibility but ignored to enforce allowed directory
    p.add_argument('--path', help='(ignored) root path to search for YAML files', default=None)
    p.add_argument('--words', help='custom wordlist path', default=None)
    p.add_argument('--add-word', help='append a word to default wordlist', default=None)
    p.add_argument('--report', help='write report to file', default=None)
    args = p.parse_args()

    repo_root = Path('.').resolve()
    # Force the allowed directory inside the repository (script-relative, portable)
    allowed_root = Path(__file__).resolve().parent.joinpath('data').resolve()
    default_words = Path(__file__).with_name('spellcheck_words.txt')

    if args.add_word:
        default_words.parent.mkdir(parents=True, exist_ok=True)
        with default_words.open('a', encoding='utf-8') as fh:
            fh.write(args.add_word.strip() + '\n')
        print(f"Added '{args.add_word}' to {default_words}")
        return 0

    custom_path = Path(args.words) if args.words else default_words
    custom_words = load_custom_words(custom_path)

    spell = SpellChecker()
    if custom_words:
        spell.word_frequency.load_words(custom_words)

    # Always search only inside the allowed_root to avoid scanning other locations.
    files = list(find_yaml_files(allowed_root))
    problems = []

    for f in sorted(files):
        try:
            text = f.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Could not read {f}: {e}")
            continue

        try:
            docs = list(yaml.safe_load_all(text))
        except Exception as e:
            print(f"YAML parse error in {f}: {e}")
            continue

        for doc in docs:
            if doc is None:
                continue
            for s in extract_strings(doc):
                words = tokenize(s)
                candidates = [w for w in words if not is_skip(w)]
                lower_candidates = [w.lower() for w in candidates]
                miss = spell.unknown(lower_candidates)
                if miss:
                    # Map back to original-casing words for readability
                    miss_original = sorted({w for w in candidates if w.lower() in miss})
                    problems.append({'file': str(f), 'text': s, 'miss': miss_original})

    out_lines = []
    report_path = Path(args.report) if args.report else None

    if not problems:
        msg = 'No misspellings found.'
        print(msg)
        out_lines.append(msg)
        if report_path and report_path.suffix.lower() in ('.yml', '.yaml'):
            report_obj = {'summary': msg, 'entries': []}
            report_path.write_text(yaml.safe_dump(report_obj, sort_keys=False), encoding='utf-8')
        elif args.report:
            Path(args.report).write_text('\n'.join(out_lines), encoding='utf-8')
        return 0

    header = f'Found {len(problems)} entries with potential misspellings.'
    print(header)
    out_lines.append(header)
    # Group problems by file so we can emit a single divider between files
    from collections import OrderedDict

    grouped = OrderedDict()
    for pbl in problems:
        try:
            file_rel = Path(pbl['file']).resolve().relative_to(allowed_root)
            file_display = str(file_rel)
        except Exception:
            file_display = Path(pbl['file']).name
        grouped.setdefault(file_display, []).append({'text': pbl['text'], 'miss': pbl['miss']})

    # Build human-readable lines grouped by file
    for file_display, items in grouped.items():
        file_line = f"File: {file_display}"
        out_lines.append(file_line)
        print(file_line)
        for it in items:
            txt = f"  Text: {it['text']}"
            out_lines.append(txt)
            print(txt)
            miss = f"  Misspelled: {', '.join(it['miss'])}"
            out_lines.append(miss)
            print(miss)
            print('')
        # divider between files
        out_lines.append(DIVIDER)
        print(DIVIDER)

    # If writing YAML report, emit structured data instead of text lines
    if report_path and report_path.suffix.lower() in ('.yml', '.yaml'):
        # Create YAML structure grouped by file, with a divider marker after each file
        y_entries = []
        for file_display, items in grouped.items():
            issues = []
            for it in items:
                issues.append({'text': it['text'], 'misspelled': it['miss']})
            y_entries.append({'file': file_display, 'issues': issues, 'divider': DIVIDER})
        report_obj = {'summary': f'Found {sum(len(items) for items in grouped.values())} entries with potential misspellings.', 'entries': y_entries}
        report_path.write_text(yaml.safe_dump(report_obj, sort_keys=False), encoding='utf-8')
        print(f'Report written to {args.report}')
        return 2

    if args.report:
        # fallback to plain text output if not YAML
        Path(args.report).write_text('\n'.join(out_lines), encoding='utf-8')
        print(f'Report written to {args.report}')

    return 2


if __name__ == '__main__':
    sys.exit(main())
