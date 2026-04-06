lore_cards = [
    {
        "name": "Ancient Prophecy",  # This should match the image filename in loreImages folder (without .png)
        "title": "Ancient Prophecy",  # Title displayed on the card
        "title_font_size": 25,  # Font size for title text
        "body": (
            "When you destroy a city, discard this lore and gain 2 Lore cards."
        ),
        "footer_left": "L",  # Left footer text (black)
        "footer": "Lore",  # Center footer text (white)
      #  "footer_right": "",  # Right footer text (black)
        "footer_font_size": 16,  # Font size for footer text
        "body_font_size": 20,

        # Optional render/asset controls (same feature set as leader cards):
        "render_scale": 2,  # 1-4; higher = sharper text, slower render
        "allow_upscale": True,  # False = don't enlarge low-res art (avoids blur)

        # Optional art placement controls:
        "zoom": 1.0,  # >1 zooms/crops art; <1 shrinks art
        "boundary_shift": 0.0,  # +/- fraction; positive pushes art boundary downward
    },
    {
        "name": "testlore",  # looks for cardAssets/loreImages/testlore.png
        "title": "testlore",
        "title_font_size": 25,
        "body": (
            "This is a *test* lore to validate **bold**, *italic*, and ***bolditalic*** rendering.\n"
            "Punctuation test: **Tax**, *Influence.* and ***Secure!***\n"
            "\n"
            "Also tests wrapping with a longer sentence that should span multiple lines in the body area."
        ),
        # Use long strings to confirm left/right footer centering behavior.
        "footer_left": "LONG",
        "footer": "Lore",
        "footer_right": "R1",
        "footer_font_size": 16,
        "body_font_size": 18,

        # Optional render/asset controls:
        "render_scale": 2,
        "allow_upscale": False,

        # Optional art placement controls:
        "zoom": 1.0,
        "boundary_shift": 1,
    },
    # {
    #     "name": "Weaponized Bureaucracy",
    #     "title": "Weaponized Bureaucracy",
    #     "title_font_size": 20,
    #     "body": (
    #         "When you secure a court card, you may Tax one loyal city matching that card’s suit."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "30",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Propaganda Engines",
    #     "title": "Propaganda Engines",
    #     "title_font_size": 25,
    #     "body": (
    #         "When a Rival declares an Ambition, you may Influence once."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "31",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Debt Spiral Protocol",
    #     "title": "Debt Spiral Protocol",
    #     "title_font_size": 23,
    #     "body": (
    #         "You may spend a non-outraged resource from its supply. After you do so provoke outrage in that resource type."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "32",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Memory-Leech AI",
    #     "title": "Memory-Leech AI",
    #     "title_font_size": 23,
    #     "body": (
    #         "When a Rival plays a card face down you may look at it."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "33",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Evacuation Grid",
    #     "title": "Evacuation Grid",
    #     "title_font_size": 25,
    #     "body": (
    #         "When one of your buildings would be destroyed, you may instead move it to an empty building slot in an adjacent system."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "34",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Panopticon Network",
    #     "title": "Panopticon Network",
    #     "title_font_size": 25,
    #     "body": (
    #         "After you secure a card you may refill it with the top card of the discard pile."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "35",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Cultural Assimilators",
    #     "title": "Cultural Assimilators",
    #     "title_font_size": 23,
    #     "body": (
    #         "When you Secure a card, place any number of agents on it. The number of agents on this card is the new raid cost. (if the card is stolen the agents return to your supply.)"
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "36",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Mutual Assured Infrastructure",
    #     "title": "Mutual Assured Infrastructure",
    #     "title_font_size": 16,
    #     "body": (
    #         "When one of your buildings is destroyed, you may destroy a piece in the same system."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "37",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Hollow Crown",
    #     "title": "Hollow Crown",
    #     "title_font_size": 25,
    #     "body": (
    #         "While you have the most Power (not tied), your ships roll one fewer die in battle.\nWhile you do not, they roll one extra die."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "38",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Exiles",
    #     "title": "Exiles",
    #     "title_font_size": 25,
    #     "body": (
    #         "Pieces you destroy in battle may instead be placed in any empty system, damaged."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "39",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Entropy Subsidies",
    #     "title": "Entropy Subsidies",
    #     "title_font_size": 25,
    #     "body": (
    #         "You may discard guild cards to gain matching resources."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "40",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Event Horizon Economy",
    #     "title": "Event Horizon Economy",
    #     "title_font_size": 23,
    #     "body": (
    #         "After you spend a Resource you may choose to remove it from the game"
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "41",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Interlocking Claims",
    #     "title": "Interlocking Claims",
    #     "title_font_size": 25,
    #     "body": (
    #         "Systems you control count as adjacent to each other."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "42",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Hostile Arbitration",
    #     "title": "Hostile Arbitration",
    #     "title_font_size": 25,
    #     "body": (
    #         "Influence: Instead of placing an Agent, remove one Rival Agent."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "43",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Unstable Production",
    #     "title": "Unstable Production",
    #     "title_font_size": 23,
    #     "body": (
    #         "When building you may place one additional ship.\nDestroy one of your ships at the end of each round."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "44",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Sovereignty Denial",
    #     "title": "Sovereignty Denial",
    #     "title_font_size": 25,
    #     "body": (
    #         "Rivals cannot control gates with your ships in them."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "45",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },
    # {
    #     "name": "Parallel Economies",
    #     "title": "Parallel Economies",
    #     "title_font_size": 25,
    #     "body": (
    #         "This card holds any amount of resources. They all have a raid cost of ½ key."
    #     ),
    #     "footer_left": "L",
    #     "footer": "Lore",
    #     "footer_right": "46",
    #     "footer_font_size": 16,
    #     "body_font_size": 20
    # },

]
