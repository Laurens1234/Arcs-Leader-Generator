import os
import sys

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

from scripts.LeaderimageScript import create_card as create_leader_image
from leadersFormatted import leaders

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
    requested_names = argv[1:]
    selected_leaders, missing = _select_leaders(leaders, requested_names)

    if missing:
        print("Warning: unknown leader name(s): " + ", ".join(missing))

    if not selected_leaders:
        print("No leaders selected. Nothing to do.")
        return 1

    success_count = 0
    error_count = 0

    for leader in selected_leaders:
        try:
            name = leader["name"]
            print(f"Creating image for: {name}")
            create_leader_image(leader)
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
