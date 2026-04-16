"""Convert existing *Formatted.py data files to YAML files.

Usage: run this script from the repo root (project root). It will write YAML files
into `scripts/data/`.

This script imports the formatted modules (same as the current batch scripts do)
to obtain the in-memory data structures, then dumps them to YAML. It prefers
module-level variables named like `*_cards` or `leaders`.
"""
import importlib.util
import os
import sys

import yaml

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")
OUT_DIR = os.path.join(SCRIPTS_DIR, "data")

MAPPINGS = {
    "guildCardsFormatted.py": ("guild.yml", ["guild_cards"]),
    "loreCardsFormatted.py": ("lore.yml", ["lore_cards"]),
    "voxCardsFormatted.py": ("vox.yml", ["vox_cards"]),
    # btrFormatted contains BTR-specific leaders; write to btr.yml
    "btrFormatted.py": ("btr.yml", ["leaders"]),
    # leadersFormatted.py (if present) should populate leaders.yml
    "leadersFormatted.py": ("leaders.yml", ["leaders"]),
    "edificeFormatted.py": ("edifice.yml", ["lore_cards"]),
}


def import_module_from_path(path):
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_data(module, candidate_names):
    for n in candidate_names:
        if hasattr(module, n):
            return getattr(module, n)
    # fallback: find first top-level list or dict-like
    for k, v in vars(module).items():
        if k.startswith("__"):
            continue
        if isinstance(v, (list, dict)):
            return v
    return None


def ensure_out_dir():
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)


def main():
    ensure_out_dir()
    for src, (out_name, candidates) in MAPPINGS.items():
        src_path = os.path.join(SCRIPTS_DIR, src)
        # If the formatted file was moved to scripts/legacy, allow that location.
        if not os.path.exists(src_path):
            alt = os.path.join(SCRIPTS_DIR, "legacy", src)
            if os.path.exists(alt):
                src_path = alt
            else:
                print(f"Skipping missing: {src}")
                continue
        print(f"Processing {src} -> {out_name}")
        module = import_module_from_path(src_path)
        data = find_data(module, candidates)
        if data is None:
            print(f"  Warning: no suitable data found in {src}; skipping.")
            continue
        out_path = os.path.join(OUT_DIR, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
        print(f"  Written {out_path}")


if __name__ == "__main__":
    main()
