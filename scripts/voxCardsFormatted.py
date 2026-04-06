vox_cards = [
    {
        "name": "testvox",  # looks for cardAssets/voxImages/testvox.png
        "title": "testvox",
        "title_font_size": 25,
        "body": (
            "Vox card test to validate the lore-style renderer.\n"
            "Rich text: *italic* **bold** ***bolditalic*** with punctuation: **Tax**, *Influence.*\n"
            "\n"
            "This line is intentionally long to verify wrapping higher on the card.\n"
            ". . . . . . . . . . . a a a a a / / / / . . . . . . . . . . . . . . . . . . . . a a a a a / / / / . . . . . . . . . . . . . . . . . . . . a a a a a / / / / . . . . . . . . . . . . . . . . . . . . a a a a a / / / / . . . . . . . . ."
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
