#!/usr/bin/env python3
"""
Script to analyze and display the most used resource combinations from leaders.
"""

import collections
from leadersFormatted import leaders

def analyze_resource_combos():
    """Analyze resource combinations from all leaders."""
    combos = []

    for leader in leaders:
        resources = leader.get('resources', [])
        # Include all leaders with 2 resource slots, treating empty strings and "none" as valid
        if len(resources) == 2:
            # Normalize empty strings and "none" to "None" for consistency
            normalized_resources = []
            for r in resources:
                if not r or r.lower().strip() == "none":
                    normalized_resources.append("None")
                else:
                    normalized_resources.append(r.strip())
            # Sort the resources to treat ["A", "B"] and ["B", "A"] as the same combo
            combo = tuple(sorted(normalized_resources))
            combos.append(combo)

    # Count frequencies
    combo_counts = collections.Counter(combos)

    # Sort by frequency (most common first), then alphabetically
    sorted_combos = sorted(combo_counts.items(),
                          key=lambda x: (-x[1], x[0]))

    return sorted_combos

def main():
    print("Most Used Resource Combinations in Leaders")
    print("=" * 50)

    sorted_combos = analyze_resource_combos()
    total_leaders = len([l for l in leaders if len(l.get('resources', [])) == 2])

    for combo, count in sorted_combos:
        combo_str = f"{combo[0]} + {combo[1]}"
        percentage = (count / total_leaders) * 100
        print(f"{combo_str:<20} {count:>2} leaders ({percentage:>5.1f}%)")

    print(f"\nTotal leaders analyzed: {total_leaders}")
    print(f"Unique combinations: {len(sorted_combos)}")

if __name__ == "__main__":
    main()