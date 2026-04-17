import argparse
import os
import subprocess
import sys


def _repo_root() -> str:
    return os.path.dirname(os.path.dirname(__file__))


def main(argv: list[str]) -> int:
    repo_root = _repo_root()

    generators: list[tuple[str, str]] = [
        ("guild", os.path.join(repo_root, "scripts", "batchGuildCards.py")),
        ("leader", os.path.join(repo_root, "scripts", "batchLeaderCards.py")),
        ("lore", os.path.join(repo_root, "scripts", "batchLoreCards.py")),
        ("vox", os.path.join(repo_root, "scripts", "batchVoxCards.py")),
    ]

    parser = argparse.ArgumentParser(
        description=(
            "Run all card generators (guild, leader, lore, vox). "
            "Optionally list types after the command to exclude them."
        )
    )

    parser.add_argument(
        "--last",
        type=int,
        dest="last",
        default=None,
        help="Only generate the last N cards in each generator's formatted list.",
    )
    parser.add_argument(
        "--source-module",
        dest="source_module",
        default=None,
        help="Optional Python module path to pass to each generator (applies to all unless per-type override).",
    )

    parser.add_argument(
        "--source-file",
        dest="source_file",
        default=None,
        help="Optional path to a .py file to pass to each generator (applies to all unless per-type override).",
    )

    parser.add_argument(
        "--yaml-file",
        dest="yaml_file",
        default=None,
        help="Optional path to a YAML file to pass to each generator (applies to all unless per-type override).",
    )

    # Per-type overrides (optional)
    parser.add_argument("--guild-source-module", dest="guild_source_module", default=None)
    parser.add_argument("--guild-source-file", dest="guild_source_file", default=None)
    parser.add_argument("--guild-yaml-file", dest="guild_yaml_file", default=None)
    parser.add_argument("--leader-source-module", dest="leader_source_module", default=None)
    parser.add_argument("--leader-source-file", dest="leader_source_file", default=None)
    parser.add_argument("--leader-yaml-file", dest="leader_yaml_file", default=None)
    parser.add_argument("--lore-source-module", dest="lore_source_module", default=None)
    parser.add_argument("--lore-source-file", dest="lore_source_file", default=None)
    parser.add_argument("--lore-yaml-file", dest="lore_yaml_file", default=None)
    parser.add_argument("--vox-source-module", dest="vox_source_module", default=None)
    parser.add_argument("--vox-source-file", dest="vox_source_file", default=None)
    parser.add_argument("--vox-yaml-file", dest="vox_yaml_file", default=None)
    parser.add_argument(
        "exclude",
        nargs="*",
        choices=[name for name, _ in generators],
        help="Card types to skip. Example: python scripts/batchAllCards.py vox lore",
    )

    args = parser.parse_args(argv[1:])

    excluded = set(args.exclude or [])

    any_failures = False
    for name, script_path in generators:
        if name in excluded:
            print(f"Skipping {name} cards")
            continue

        if not os.path.exists(script_path):
            print(f"Warning: generator script not found: {script_path}. Skipping.")
            any_failures = True
            continue

        print(f"\n=== Running {name} generator ===")
        cmd = [sys.executable, script_path]
        if args.last is not None:
            cmd.append(f"--last={args.last}")
        # Forward source-module/file flags, allowing per-type overrides
        type_module = None
        type_file = None
        if name == "guild":
            type_module = args.guild_source_module or args.source_module
            type_file = args.guild_source_file or args.source_file
        elif name == "leader":
            type_module = args.leader_source_module or args.source_module
            type_file = args.leader_source_file or args.source_file
        elif name == "lore":
            type_module = args.lore_source_module or args.source_module
            type_file = args.lore_source_file or args.source_file
        elif name == "vox":
            type_module = args.vox_source_module or args.source_module
            type_file = args.vox_source_file or args.source_file

        if type_module:
            cmd.append(f"--source-module={type_module}")
        if type_file:
            cmd.append(f"--source-file={type_file}")
        # Forward yaml-file flags
        type_yaml = None
        if name == "guild":
            type_yaml = args.guild_yaml_file or args.yaml_file
        elif name == "leader":
            type_yaml = args.leader_yaml_file or args.yaml_file
        elif name == "lore":
            type_yaml = args.lore_yaml_file or args.yaml_file
        elif name == "vox":
            type_yaml = args.vox_yaml_file or args.yaml_file

        if type_yaml:
            cmd.append(f"--yaml-file={type_yaml}")
        proc = subprocess.run(cmd, cwd=repo_root)
        if proc.returncode != 0:
            any_failures = True
            print(f"*** {name} generator exited with code {proc.returncode} ***")

    return 1 if any_failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
