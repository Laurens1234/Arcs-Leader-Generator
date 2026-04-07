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
        proc = subprocess.run(cmd, cwd=repo_root)
        if proc.returncode != 0:
            any_failures = True
            print(f"*** {name} generator exited with code {proc.returncode} ***")

    return 1 if any_failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
