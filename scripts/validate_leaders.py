#!/usr/bin/env python3
"""Validate the leaders data in leadersFormatted.py.

Checks performed:
- required fields and types
- resource normalization and allowed resource names
- setup structure and values
- presence of asset image file in cardAssets/leaderImages

This script also provides helpers to:
- write a normalized copy of the leaders list (`--fix-resources`)
- suggest or apply safe asset renames to match leader names
- write a JSON report of findings

Exit code: 0 = success (no errors), 2 = errors found
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEADERS_PY = ROOT / "scripts" / "legacy" / "leadersFormatted.py"
ASSET_DIR = ROOT / "cardAssets" / "leaderImages"

# Allowed resource literals (empty string currently used for intentionally-blank slots)
ALLOWED_RESOURCES = {"Fuel", "Material", "Psionic", "Relic", "Weapon", ""}

# Words to ignore in spell/grammar checks (lowercase)
IGNORE_WORDS = {"city", "starport", "starports", "none"}


def load_leaders():
    # Import dynamically from scripts.legacy package path
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        from scripts.legacy.leadersFormatted import leaders
    except Exception as e:
        print(f"Error importing legacy leadersFormatted.py: {e}")
        raise
    return leaders


def canonical_resource(r):
    # Normalize empty/none-like values to the canonical string "None"
    if not r or (isinstance(r, str) and r.strip().lower() in {"", "none"}):
        return "None"
    return r.strip()


def validate_leader(leader):
    errors = []
    name = leader.get("name")
    if not name or not isinstance(name, str):
        errors.append("missing or invalid 'name'")

    # abilities may be a tuple of strings or a single string
    abilities = leader.get("abilities")
    if not abilities or not isinstance(abilities, (str, tuple, list)):
        errors.append("missing or invalid 'abilities' (expect str or tuple/list of strings)")

    # resources: expect list/tuple of length 2
    resources = leader.get("resources")
    if not isinstance(resources, (list, tuple)) or len(resources) != 2:
        errors.append("'resources' must be a list/tuple of length 2")
    else:
        for r in resources:
            if not isinstance(r, str):
                errors.append(f"resource not a string: {r!r}")
            elif r not in ALLOWED_RESOURCES:
                errors.append(f"unknown resource value: {r!r}")

    # setup
    setup = leader.get("setup")
    if not isinstance(setup, dict) or set(setup.keys()) != {"A", "B", "C"}:
        errors.append("'setup' must be a dict with keys A, B, C")
    else:
        for slot in ("A", "B", "C"):
            s = setup.get(slot)
            if not isinstance(s, dict):
                errors.append(f"setup[{slot}] must be a dict")
                continue
            ships = s.get("ships")
            if not isinstance(ships, int) or ships < 0:
                errors.append(f"setup[{slot}]['ships'] must be a non-negative int")
            building = s.get("building")
            if not isinstance(building, str):
                errors.append(f"setup[{slot}]['building'] must be a string")

    # body_font_size
    if "body_font_size" not in leader:
        errors.append("missing 'body_font_size'")
    else:
        if not isinstance(leader.get("body_font_size"), int):
            errors.append("'body_font_size' must be an int")

    # optional numeric fields
    for fld in ("zoom", "boundary_shift"):
        if fld in leader:
            v = leader[fld]
            if not isinstance(v, (int, float)):
                errors.append(f"'{fld}' must be numeric")

    # asset file exists (case-sensitive match)
    if isinstance(name, str):
        expected = ASSET_DIR / f"{name}.png"
        if not expected.exists():
            # try tolerant variants and case-insensitive search
            candidates = []
            candidates.append(ASSET_DIR / f"{name.replace(' ', '-')}.png")
            candidates.append(ASSET_DIR / f"{name.replace(' ', '_')}.png")
            # case-insensitive search
            found_ci = None
            for p in ASSET_DIR.iterdir():
                if p.is_file() and p.suffix.lower() == ".png" and p.name.lower() == f"{name}.png".lower():
                    found_ci = p
                    break

            if not any(c.exists() for c in candidates) and not found_ci:
                errors.append(f"missing image asset: {expected.relative_to(ROOT)}")
            else:
                # If found case-insensitively, warn rather than error
                if found_ci and not expected.exists():
                    errors.append(f"image exists with different case/name: {found_ci.name} (expected {expected.name})")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate leadersFormatted.py contents and assets")
    parser.add_argument("--fix-resources", action="store_true", help="Write a normalized leaders file to scripts/leadersFormatted.normalized.py (does not overwrite original)")
    parser.add_argument("--suggest-asset-renames", action="store_true", help="Suggest asset filename renames to match leader names")
    parser.add_argument("--apply-asset-renames", action="store_true", help="Apply safe asset renames (may rename files in cardAssets/leaderImages)")
    parser.add_argument("--report", type=str, default=None, help="Write a JSON report of findings to this path")
    parser.add_argument("--spell-check", action="store_true", help="Run a spelling check on textual fields (requires pyenchant)")
    parser.add_argument("--grammar-check", action="store_true", help="Run grammar/grammar+spelling checks via LanguageTool (requires language-tool-python)")
    parser.add_argument("--check-all", action="store_true", help="Run both spelling and grammar checks (if available)")
    args = parser.parse_args()

    leaders = load_leaders()
    total = len(leaders)
    print(f"Validating {total} leaders from {LEADERS_PY}")

    all_errors = {}
    normalized = []
    asset_renames = []
    asset_map = {}
    spelling_issues = {}
    grammar_issues = {}

    # Build a case-insensitive map of existing asset filenames
    existing_assets = {p.name: p for p in ASSET_DIR.iterdir() if p.is_file()}
    existing_assets_ci = {p.name.lower(): p for p in existing_assets.values()}

    for idx, leader in enumerate(leaders, start=1):
        errs = validate_leader(leader)
        if errs:
            all_errors[leader.get("name", f"<index {idx}>")] = errs

        # build normalized copy
        copy = dict(leader)
        res = copy.get("resources")
        if isinstance(res, (list, tuple)) and len(res) == 2:
            copy["resources"] = [canonical_resource(r) for r in res]
        normalized.append(copy)

        # asset matching suggestions
        name = leader.get("name")
        if isinstance(name, str):
            expected = f"{name}.png"
            if expected in existing_assets:
                asset_map[name] = expected
                continue
            # try variants
            candidates = [f"{name.replace(' ', '-')}.png", f"{name.replace(' ', '_')}.png", expected.lower()]
            found = None
            for c in candidates:
                # case-insensitive
                p = existing_assets_ci.get(c.lower())
                if p:
                    found = p
                    break
            if found:
                asset_map[name] = found.name
                if found.name != expected:
                    asset_renames.append((found.name, expected))
            else:
                asset_map[name] = None

    # report
    if not all_errors:
        print("OK: no validation errors found.")
    else:
        print(f"Found validation issues in {len(all_errors)} leaders:\n")
        for name, errs in sorted(all_errors.items()):
            print(f"- {name}:")
            for e in errs:
                print(f"    - {e}")

    # --- Spell and grammar checks ---
    # Try to import optional libraries lazily and run checks only when requested
    do_spell = args.spell_check or args.check_all
    do_grammar = args.grammar_check or args.check_all
    if do_spell or do_grammar:
        # collect textual fields to check per leader (name + abilities + setup.building)
        texts_by_leader = {}
        for leader in leaders:
            name = leader.get("name", "<unnamed>")
            pieces = []
            if isinstance(leader.get("abilities"), str):
                pieces.append(leader.get("abilities"))
            elif isinstance(leader.get("abilities"), (list, tuple)):
                pieces.extend([a for a in leader.get("abilities") if isinstance(a, str)])
            # include building names from setup
            s = leader.get("setup")
            if isinstance(s, dict):
                for slot in ("A", "B", "C"):
                    b = s.get(slot, {}).get("building")
                    if isinstance(b, str):
                        pieces.append(b)
            texts_by_leader[name] = "\n".join(pieces)

    if do_spell:
        try:
            import enchant
            ENCHANT_AVAILABLE = True
        except Exception:
            ENCHANT_AVAILABLE = False
            print("Spell-check requested but 'pyenchant' not available. Install with: pip install pyenchant")

        if ENCHANT_AVAILABLE:
            try:
                d = enchant.Dict("en_US")
            except Exception:
                d = None
            if d is None:
                print("pyenchant installed but no dictionary found for 'en_US'.")
            else:
                word_re = re.compile(r"[A-Za-z']{2,}")
                for name, text in texts_by_leader.items():
                    bad = []
                    for w in word_re.findall(text):
                        # skip ALL-CAPS (likely acronyms) and proper nouns (Capitalized tokens)
                        if w.isupper():
                            continue
                        if w[0].isupper():
                            # allow some short proper nouns by heuristics
                            if len(w) <= 3:
                                continue
                        # ignore domain-specific tokens
                        if w.lower() in IGNORE_WORDS:
                            continue
                        if not d.check(w):
                            # suggestions limited to top 3
                            sug = d.suggest(w)[:3]
                            bad.append({"word": w, "suggestions": sug})
                    if bad:
                        spelling_issues[name] = bad

    if do_grammar:
        try:
            import language_tool_python
            LT_AVAILABLE = True
        except Exception:
            LT_AVAILABLE = False
            print("Grammar-check requested but 'language-tool-python' not available. Install with: pip install language-tool-python")

        if LT_AVAILABLE:
            tool = language_tool_python.LanguageTool('en-US')
            for name, text in texts_by_leader.items():
                if not text.strip():
                    continue
                matches = tool.check(text)
                if matches:
                    # limit details to a few matches per leader
                    issues = []
                    for m in matches[:10]:
                                length = getattr(m, "errorLength", None)
                                if length is None:
                                    length = getattr(m, "error_length", None)
                                offset = getattr(m, "offset", None)
                                # try to extract offending text to allow ignores
                                offending = None
                                if offset is not None and length is not None:
                                    try:
                                        offending = text[offset: offset + length]
                                    except Exception:
                                        offending = None
                                if offending:
                                    low = offending.lower()
                                    if any(iw in low for iw in IGNORE_WORDS):
                                        continue
                                replacements = getattr(m, "replacements", None)
                                if replacements is None:
                                    replacements = getattr(m, "replacements", [])
                                issues.append({
                                    "message": getattr(m, "message", ""),
                                    "offset": offset,
                                    "length": length,
                                    "suggestions": (replacements or [])[:5]
                                })
                    grammar_issues[name] = issues

    # Print brief spell/grammar summaries
    if spelling_issues:
        print(f"\nSpelling issues found in {len(spelling_issues)} leaders (use --report to see details):")
        for name, issues in sorted(spelling_issues.items()):
            print(f"- {name}: {len(issues)} possible misspellings")

    if grammar_issues:
        print(f"\nGrammar issues found in {len(grammar_issues)} leaders (use --report to see details):")
        for name, issues in sorted(grammar_issues.items()):
            print(f"- {name}: {len(issues)} possible grammar suggestions")

    if args.suggest_asset_renames or args.apply_asset_renames:
        if asset_renames:
            print("\nSuggested asset renames:")
            for src, dst in asset_renames:
                print(f"  {src} -> {dst}")
        else:
            print("\nNo asset rename suggestions; assets match leader names (case-insensitive).")

    if args.apply_asset_renames:
        # apply safe renames (only when source exists and destination does not)
        for src_name, dst_name in asset_renames:
            src = ASSET_DIR / src_name
            dst = ASSET_DIR / dst_name
            if not src.exists():
                print(f"Skipping missing source {src_name}")
                continue
            if dst.exists():
                print(f"Skipping rename {src_name} -> {dst_name}: destination exists")
                continue
            print(f"Renaming {src_name} -> {dst_name}")
            shutil.move(str(src), str(dst))

    if args.fix_resources:
        out = Path(__file__).resolve().parents[0] / "leadersFormatted.normalized.py"
        print(f"Writing normalized leaders to {out}")
        with out.open("w", encoding="utf-8") as f:
            f.write("# Auto-generated normalized leaders (do not edit)\n")
            f.write("leaders = ")
            f.write(repr(normalized))
            f.write("\n")

    if args.report:
        rpt = Path(args.report)
        print(f"Writing JSON report to {rpt}")
        rpt.write_text(json.dumps({
            "errors": all_errors,
            "asset_renames": asset_renames,
            "asset_map": asset_map,
            "spelling": spelling_issues,
            "grammar": grammar_issues,
        }, indent=2), encoding="utf-8")

    # exit code
    return 0 if not all_errors else 2


if __name__ == "__main__":
    rc = main()
    raise SystemExit(rc)
