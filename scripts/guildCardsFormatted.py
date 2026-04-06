guild_cards = [
    {
        "name": "testguild",  # looks for cardAssets/guildImages/testguild.png
        "title": "Testguild",
        "title_font_size": 25,
        "body": (
            "This is a **Guild** card test.\n"
            "Rich text: *italic* **bold** ***bolditalic*** with punctuation: **Tax**, *Influence.*\n"
            "\n"
            "Long wrapping sentence to confirm layout works the same as lore cards."
        ),
        "footer_left": "G",
        "footer": "Guild",
        "footer_right": "1",
        "footer_font_size": 16,
        "body_font_size": 18,

        # Guild-specific inputs:
        "resource": "fuel",  # one of: material, fuel, weapon, relic, psionic
        "raid": 2,  # 1, 2, 3, or "X" (defaults to 2)

        # Optional render/asset controls (same as lore cards):
        "render_scale": 2,
        "allow_upscale": True,
        "zoom": 1.0,
        "boundary_shift": 1.0,
    },
    {
        "name": "testguild_material",  # looks for cardAssets/guildImages/testguild_material.png
        "title": "testguild_material",
        "title_font_size": 25,
        "body": (
            "Material suit test.\n"
            "Rich text: *italic* **bold** ***bolditalic***.\n"
            "Raid icon test: raid=1."
        ),
        "footer_left": "G",
        "footer": "Guild",
        "footer_right": "2",
        "footer_font_size": 16,
        "body_font_size": 18,

        "resource": "material",
        "raid": 1,

        "render_scale": 2,
        "allow_upscale": True,
        "zoom": 1.0,
        "boundary_shift": 0.0,
    },
    {
        "name": "testguild_weapon",  # looks for cardAssets/guildImages/testguild_weapon.png
        "title": "testguild_weapon",
        "title_font_size": 25,
        "body": (
            "Weapon suit test.\n"
            "Punctuation baseline: **Tax**, *Influence.* and ***Secure!***\n"
            "Raid icon test: raid=2 (default)."
        ),
        "footer_left": "G",
        "footer": "Guild",
        "footer_right": "3",
        "footer_font_size": 16,
        "body_font_size": 18,

        "resource": "weapon",
        "raid": 2,

        "render_scale": 2,
        "allow_upscale": True,
        "zoom": 1.0,
        "boundary_shift": 0.0,
    },
    {
        "name": "testguild_relic",  # looks for cardAssets/guildImages/testguild_relic.png
        "title": "testguild_relic",
        "title_font_size": 25,
        "body": (
            "Relic suit test.\n"
            "Long wrap sentence: this line is intentionally a bit longer to wrap across multiple lines in the body text area.\n"
            "Raid icon test: raid=3."
        ),
        "footer_left": "G",
        "footer": "Guild",
        "footer_right": "4",
        "footer_font_size": 16,
        "body_font_size": 18,

        "resource": "relic",
        "raid": 3,

        "render_scale": 2,
        "allow_upscale": True,
        "zoom": 1.0,
        "boundary_shift": 0.0,
    },
    {
        "name": "testguild_psionic",  # looks for cardAssets/guildImages/testguild_psionic.png
        "title": "testguild_psionic",
        "title_font_size": 25,
        "body": (
            "Psionic suit test.\n"
            "Raid icon test: raid='X'."
        ),
        "footer_left": "G",
        "footer": "Guild",
        "footer_right": "5",
        "footer_font_size": 16,
        "body_font_size": 18,

        "resource": "psionic",
        "raid": "X",

        "render_scale": 2,
        "allow_upscale": True,
        "zoom": 1.0,
        "boundary_shift": 0.0,
    },
]
