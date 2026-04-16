vox_cards = [

    {
        "name": "testvox_icons",  # optional: cardAssets/voxImages/testvox_icons.png
        "title": "Vox Icons",
        "title_font_size": 25,
        "body": (
            "{icon:resource_fuel} Icon at sentence start.\n"
            "Icon in middle {icon:resource_weapon} of a sentence.\n"
            "Icon at end {icon:resource_relic}.\n"
            "Two icons back-to-back: {icon:dice_hit_black} {icon:dice_hit_black}.\n"
            "Icon with comma {icon:dice_key_black}, then words; icon with period {icon:dice_intercept_black}.\n"
            "Mixed set: {icon:crisis_hex} {icon:edict_arrow} {icon:id_moon} {icon:objective} {icon:summit}.\n"
        ),
        "footer_left": "V",
        "footer": "Vox",
        "footer_right": "99",
        "footer_font_size": 16,
        "body_font_size": 18,

        "render_scale": 2,
        "allow_upscale": True,
        "zoom": 1.0,
        "boundary_shift": 0.0,
        "text_top_y": 24,
        "body_top_padding": 16,
    },
    {
        "name": "testvox",  # looks for cardAssets/voxImages/testvox.png
        "title": "Testvox",
        "title_font_size": 25,
        "body": (
            "Vox card test to validate the lore-style renderer.\n"
            "Rich text: *italic* **bold** ***bolditalic*** with punctuation: **Tax**, *Influence.*\n"
            "\n"
            "This line is intentionally long to verify wrapping higher on the card.\n"
        ),
        "footer_left": "V",
        "footer": "Vox",
        "footer_right": "1",
        "footer_font_size": 16,
        "body_font_size": 18,

        # Optional render/asset controls (same as lore cards):
        "render_scale": 2,
        "allow_upscale": True,
        "zoom": 1.0,
        "boundary_shift": 0.0,
    },
]
