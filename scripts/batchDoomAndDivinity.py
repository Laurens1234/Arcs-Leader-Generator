#!/usr/bin/env python3
"""
Wrapper script to batch render all Doom & Divinity guild and vox cards.

This script temporarily renames the deck-specific YAML files to the expected
naming convention (guild_single.yml / vox_single.yml), renders all cards,
and then renames them back.

Usage:
  python scripts/batchDoomAndDivinity.py [--render-scale SCALE] [--allow-upscale]
"""

import os
import sys
import argparse
import shutil
import subprocess
import yaml

script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir, "data")

GUILD_SOURCE = os.path.join(data_dir, "doom_and_divinity.yml")
GUILD_TEMP = os.path.join(data_dir, "guild_single.yml")

VOX_SOURCE = os.path.join(data_dir, "doom_and_divinity_vox.yml")
VOX_TEMP = os.path.join(data_dir, "vox_single.yml")


def setup_files():
    """Copy deck files to temporary names for batch scripts to find them."""
    try:
        shutil.copy(GUILD_SOURCE, GUILD_TEMP)
        print(f"✓ Set up {os.path.basename(GUILD_TEMP)}")
    except FileNotFoundError:
        print(f"✗ Error: {GUILD_SOURCE} not found")
        return False

    try:
        shutil.copy(VOX_SOURCE, VOX_TEMP)
        print(f"✓ Set up {os.path.basename(VOX_TEMP)}")
    except FileNotFoundError:
        print(f"✗ Error: {VOX_SOURCE} not found")
        return False

    return True


def setup_first_n_files(first_n):
    """Write the first N cards from each source YAML to the temporary files."""
    try:
        with open(GUILD_SOURCE, 'r', encoding='utf-8') as f:
            guild_cards = yaml.safe_load(f) or []
        with open(GUILD_TEMP, 'w', encoding='utf-8') as f:
            yaml.safe_dump(guild_cards[:first_n], f, sort_keys=False)
        print(f"✓ Set up {os.path.basename(GUILD_TEMP)} with first {first_n} guild cards")
    except FileNotFoundError:
        print(f"✗ Error: {GUILD_SOURCE} not found")
        return False

    try:
        with open(VOX_SOURCE, 'r', encoding='utf-8') as f:
            vox_cards = yaml.safe_load(f) or []
        with open(VOX_TEMP, 'w', encoding='utf-8') as f:
            yaml.safe_dump(vox_cards[:first_n], f, sort_keys=False)
        print(f"✓ Set up {os.path.basename(VOX_TEMP)} with first {first_n} vox cards")
    except FileNotFoundError:
        print(f"✗ Error: {VOX_SOURCE} not found")
        return False

    return True


def cleanup_files():
    """Remove temporary files."""
    for temp_file in [GUILD_TEMP, VOX_TEMP]:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"✓ Cleaned up {os.path.basename(temp_file)}")


def get_card_names_from_yaml(yaml_file):
    """Extract card names from a YAML file."""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            cards = yaml.safe_load(f) or []
        return [card.get('name') for card in cards if isinstance(card, dict) and 'name' in card]
    except Exception as e:
        print(f"Error reading {yaml_file}: {e}")
        return []


def move_specific_cards(source_dir, dest_dir, card_names):
    """Move only specific cards to the destination folder."""
    if not os.path.exists(source_dir):
        return 0

    os.makedirs(dest_dir, exist_ok=True)
    count = 0
    
    # Determine suffix based on directory
    if "guild" in source_dir:
        target_suffixes = ["_Guild_Card.png"]
    elif "vox" in source_dir:
        target_suffixes = ["_Vox_Card.png"]
    else:
        target_suffixes = ["_Guild_Card.png", "_Vox_Card.png"]
    
    filenames_to_move = set()
    for card_name in card_names:
        for suffix in target_suffixes:
            filenames_to_move.add(f"{card_name}{suffix}")
    
    # Move only matching files
    for file in os.listdir(source_dir):
        if file in filenames_to_move:
            src_file = os.path.join(source_dir, file)
            dest_file = os.path.join(dest_dir, file)
            if os.path.isfile(src_file):
                shutil.move(src_file, dest_file)
                count += 1
    return count


def run_batch_script(script_name, args):
    """Run a batch script with the given arguments."""
    script_path = os.path.join(script_dir, script_name)
    cmd = [sys.executable, script_path] + args
    print(f"\n▶ Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=script_dir)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Batch render Doom & Divinity guild and vox cards."
    )
    parser.add_argument(
        "--render-scale",
        type=int,
        default=2,
        help="Render scale (1-4, default: 2)",
    )
    parser.add_argument(
        "--allow-upscale",
        action="store_true",
        help="Allow upscaling low-res artwork",
    )
    parser.add_argument(
        "--no-allow-upscale",
        action="store_true",
        help="Disallow upscaling low-res artwork",
    )
    parser.add_argument(
        "--first",
        type=int,
        default=None,
        help="Render only the first N cards from each deck YAML file.",
    )

    args = parser.parse_args()

    # Build command-line arguments for batch scripts
    batch_args = [f"--render-scale={args.render_scale}"]
    if args.allow_upscale:
        batch_args.append("--allow-upscale")
    if args.no_allow_upscale:
        batch_args.append("--no-allow-upscale")

    # Setup: copy files to expected names
    if args.first is not None:
        if args.first <= 0:
            print("✗ --first must be greater than 0")
            return 1
        if not setup_first_n_files(args.first):
            return 1
    else:
        if not setup_files():
            return 1

    # Define output folder for this deck
    base_path = os.path.dirname(script_dir)
    deck_output_dir = os.path.join(base_path, "results", "doom_and_divinity")
    deck_guild_dir = os.path.join(deck_output_dir, "guild")
    deck_vox_dir = os.path.join(deck_output_dir, "vox")

    try:
        # Run guild cards
        print("\n" + "=" * 60)
        print("Rendering Guild Cards")
        print("=" * 60)
        guild_exit = run_batch_script("batchGuildCards.py", batch_args)

        # Run vox cards
        print("\n" + "=" * 60)
        print("Rendering Vox Cards")
        print("=" * 60)
        vox_exit = run_batch_script("batchVoxCards.py", batch_args)

        if guild_exit == 0 and vox_exit == 0:
            # Move cards to deck-specific folder
            print("\n" + "=" * 60)
            print("Organizing Cards")
            print("=" * 60)
            
            # Get card names from the YAML files
            guild_card_names = get_card_names_from_yaml(GUILD_TEMP)
            vox_card_names = get_card_names_from_yaml(VOX_TEMP)
            
            print(f"Guild cards to move: {guild_card_names}")
            print(f"Vox cards to move: {vox_card_names}")
            
            default_guild_dir = os.path.join(base_path, "results", "guild")
            default_vox_dir = os.path.join(base_path, "results", "vox")
            
            guild_count = move_specific_cards(default_guild_dir, deck_guild_dir, guild_card_names)
            vox_count = move_specific_cards(default_vox_dir, deck_vox_dir, vox_card_names)
            
            print(f"\n✓ Moved {guild_count} guild cards to {deck_guild_dir}")
            print(f"✓ Moved {vox_count} vox cards to {deck_vox_dir}")
            print(f"\n✓ All Doom & Divinity cards rendered successfully!")
            return 0
        else:
            print("\n✗ Some cards failed to render")
            return 1

    finally:
        # Always cleanup temporary files
        cleanup_files()


if __name__ == "__main__":
    raise SystemExit(main())
