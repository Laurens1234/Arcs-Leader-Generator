import argparse
import importlib
import importlib.util
import os
import sys

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

# Prefer YAML data files in `scripts/data/` but fall back to importing the existing
# formatted Python module for compatibility.
leaders = None
try:
    import yaml

    # Prefer leaders.yml (official leadersFormatted.py export). Fall back to btr.yml
    # which contains BTR-specific leaders converted from btrFormatted.py.
    data_dir_env = os.environ.get("ADK_DATA_DIR")
    if data_dir_env:
        leaders_path = os.path.join(data_dir_env, "leaders.yml")
        btr_path = os.path.join(data_dir_env, "btr.yml")
    else:
        leaders_path = os.path.join(script_dir, "scripts", "data", "leaders.yml")
        btr_path = os.path.join(script_dir, "scripts", "data", "btr.yml")
    # Prefer per-template single file when present in ADK_DATA_DIR, otherwise
    # prefer the full list file. If ADK_DATA_DIR is set and any YAML file exists
    # there, treat load errors or empty results as fatal (no fallback to .py).
    full_path = leaders_path
    single_path = os.path.join(os.path.dirname(full_path), "leaders_single.yml")
    chosen = None
    if os.path.exists(single_path):
        chosen = single_path
    elif os.path.exists(full_path):
        chosen = full_path

    if chosen:
        try:
            with open(chosen, encoding="utf-8") as f:
                leaders = yaml.safe_load(f)
        except Exception as e:
            print(f"[leaderCards] Failed to load YAML at {chosen}: {e}")
            sys.exit(2)

        if leaders is None and data_dir_env:
            print(f"[leaderCards] YAML at {chosen} is empty or invalid")
            sys.exit(2)
except Exception:
    leaders = None

if leaders is None:
    from scripts.legacy.leadersFormatted import leaders

from scripts.LeaderimageScript import create_card as create_leader_image

base_path = os.path.dirname(os.path.dirname(__file__))
result_path = os.path.join(base_path, "results")

if not os.path.exists(result_path):
    os.makedirs(result_path)


def _select_leaders(all_leaders, requested_names):
    if not requested_names:
        return list(all_leaders), []

    by_lower_name = {l["name"].casefold(): l for l in all_leaders}
    selected = []
    missing = []
    for raw in requested_names:
        key = raw.casefold()
        leader = by_lower_name.get(key)
        if leader is None:
            missing.append(raw)
            continue
        selected.append(leader)

    return selected, missing


def main(argv):
    parser = argparse.ArgumentParser(description="Generate leader cards.")
    parser.add_argument(
        "--render-scale",
        type=int,
        dest="render_scale",
        default=None,
        help="Render the whole card at this scale (1-4). Overrides per-card setting if provided.",
    )
    upscale_group = parser.add_mutually_exclusive_group()
    upscale_group.add_argument(
        "--allow-upscale",
        action="store_true",
        dest="allow_upscale",
        help="Allow upscaling low-res artwork (may look blurry). Overrides per-card setting.",
    )
    upscale_group.add_argument(
        "--no-allow-upscale",
        action="store_false",
        dest="allow_upscale",
        help="Disallow upscaling low-res artwork (default behavior). Overrides per-card setting.",
    )
    parser.set_defaults(allow_upscale=None)
    parser.add_argument(
        "names",
        nargs="*",
        help="Optional leader names to generate (case-insensitive). If omitted, generates all leaders.",
    )

    parser.add_argument(
        "--source-module",
        dest="source_module",
        default=None,
        help="Optional Python module path to import leaders from (e.g. scripts.custom_leaders).",
    )

    parser.add_argument(
        "--source-file",
        dest="source_file",
        default=None,
        help="Optional path to a .py file to load leaders from.",
    )

    parser.add_argument(
        "--yaml-file",
        dest="yaml_file",
        default=None,
        help="Optional path to a YAML file containing leaders (list).",
    )

    parser.add_argument(
        "--last",
        type=int,
        dest="last",
        default=None,
        help="Only generate the last N leaders from the selected set.",
    )

    parser.add_argument(
        "--number-start",
        type=int,
        dest="number_start",
        default=1,
        help=(
            "Starting number for leader cards. The first leader in leadersFormatted.py will be this number, "
            "the next leader will be +1, etc."
        ),
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        dest="no_numbers",
        help="Disable drawing the small leader card number.",
    )

    args = parser.parse_args(argv[1:])

    requested_names = args.names

    # Support loading leaders from alternate module/file
    cards_source = leaders
    if args.source_module or args.source_file:
        try:
            if args.source_module:
                mod = importlib.import_module(args.source_module)
            else:
                spec = importlib.util.spec_from_file_location("custom_leaders_module", args.source_file)
                if spec is None or spec.loader is None:
                    print(f"Error: cannot load source file: {args.source_file}")
                    return 3
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

            if hasattr(mod, "leaders"):
                cards_source = getattr(mod, "leaders")
            else:
                print("Error: source does not define 'leaders'.")
                return 3
        except Exception as e:
            print(f"Failed to import leaders from source: {e}")
            return 3

    # Allow loading leaders directly from a YAML file provided on the CLI.
    if args.yaml_file:
        try:
            import yaml as _yaml
        except Exception:
            print("Error: loading YAML requires PyYAML (pip install pyyaml)")
            return 3

        if not os.path.exists(args.yaml_file):
            print(f"Error: YAML file not found: {args.yaml_file}")
            return 3

        try:
            with open(args.yaml_file, encoding="utf-8") as f:
                loaded = _yaml.safe_load(f)
        except Exception as e:
            print(f"Failed to load YAML file {args.yaml_file}: {e}")
            return 3

        if loaded is None or not isinstance(loaded, list):
            print(f"Error: YAML at {args.yaml_file} did not contain a list of leaders.")
            return 3

        cards_source = loaded
        print(f"[leaderCards] Loaded {len(cards_source)} entries from {args.yaml_file}")

    selected_leaders, missing = _select_leaders(cards_source, requested_names)

    # Numbering is based on the order of leaders in the source module
    leader_index_by_name = {l["name"].casefold(): idx for idx, l in enumerate(cards_source)}

    if missing:
        print("Warning: unknown leader name(s): " + ", ".join(missing))

    if args.last is not None:
        if args.last <= 0:
            print("Error: --last must be a positive integer")
            return 2
        if len(selected_leaders) > args.last:
            selected_leaders = selected_leaders[-args.last:]

    if not selected_leaders:
        print("No leaders selected. Nothing to do.")
        return 1

    success_count = 0
    error_count = 0

    for leader in selected_leaders:
        try:
            leader_payload = dict(leader)
            if args.render_scale is not None:
                leader_payload["render_scale"] = args.render_scale
            if args.allow_upscale is not None:
                leader_payload["allow_upscale"] = args.allow_upscale

            if args.no_numbers:
                leader_payload["show_number"] = False
            else:
                idx = leader_index_by_name.get(leader_payload["name"].casefold())
                if idx is not None:
                    leader_payload["card_number"] = args.number_start + idx

            name = leader_payload["name"]
            print(f"Creating image for: {name}")
            create_leader_image(leader_payload)
            success_count += 1
        except Exception as e:
            print(f"Error generating image for {leader['name']}: {e}")
            error_count += 1

    print(f"\nImage creation complete.")
    print(f"Leaders processed successfully: {success_count}")
    print(f"Leaders with errors: {error_count}")
    return 0 if error_count == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
