import argparse
import os
import sys

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

from leadersFormatted import leaders

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
    selected_leaders, missing = _select_leaders(leaders, requested_names)

    # Numbering is based on the order of leaders in leadersFormatted.py
    leader_index_by_name = {l["name"].casefold(): idx for idx, l in enumerate(leaders)}

    if missing:
        print("Warning: unknown leader name(s): " + ", ".join(missing))

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
