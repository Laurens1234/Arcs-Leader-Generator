leaders = [
    {
        "name": "Kaiju",
        "abilities": (
            "**Devouring:** When you destroy a city, repair all your ships in its cluster.\n"
            "**Feared:** When you tax a city you control, damage it."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 4, "building": "city", "damaged": False},
            "B": {"ships": 4, "building": "city", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Shapeshifter",
        "abilities": (
            "**Mimicry:** When any player declares an ambition, gain a resource of its type. "
            "(Weapon for Tyrant and Warlord, you choose Material or Fuel for Tycoon.)\n"
            "**Flickering:** At the end of each chapter, discard all your resources, then gain 1 Material."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Sentient",
        "abilities": (
            "**Formless:** At the start of each chapter, choose a gate. Until the end of the chapter, you may Catapult and build ships there any number of times per turn. "
            "(You do not need any Loyal pieces to build.)\n"
            "**Shapeless:** In setup, scrap all your starports."
        ),
        "resources": ["Fuel", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 2, "building": "None", "damaged": False},
            "C": {"ships": 3, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Hierarch",
        "abilities": (
            "**Zealous:** When you influence a card with no Loyal agents, you may influence another card with no Loyal agents.\n"
            "**Rigid:** You cannot influence when you Pivot."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Smuggler",
        "abilities": (
            "**Resourceful:** When you battle and roll any raid dice, you may steal 1 additional resource for free.\n"
            "**Infamous:** When you destroy a building, scrap 1 agent and 1 ship in your supply."
        ),
        "resources": ["Fuel", "Weapon"],
        "setup": {
            "A": {"ships": 4, "building": "starport", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "General",
        "abilities": (
            "**Blitzing:** Prelude: Once per turn, you may spend a resource to battle.\n"
            "**Reckless:** In battle, when you roll an intercept, add 1 self hit to your roll and immediately reroll any other die without a self hit."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Necromancer",
        "abilities": (
            "**Arising:** When you destroy any piece, you may place a matching fresh piece of your own there.\n"
            "**Gravebound:** You cannot build fresh pieces and build them damaged instead. You cannot repair buildings."
        ),
        "resources": ["Psionic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": True},
            "B": {"ships": 3, "building": "starport", "damaged": True},
            "C": {"ships": 3, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Composer",
        "abilities": (
            "**Elegant:** When you spend a pip to repair, gain 1 resource.\n"
            "**Obsessed:** You cannot build in clusters where any of your pieces are damaged."
        ),
        "resources": ["Material", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 3, "building": "None", "damaged": False}
        }
    },
    # ... Continue with the rest in the same format.
]
leaders += [
    {
        "name": "Maw",
        "abilities": (
            "**Voracious:** When you declare an ambition, place a ship anywhere on the map.\n"
            "**Crushing:** When more than 1 Rival ship enters a planetary system you control, you destroy 1 of those ships.\n"
            "**Erratic:** At the end of each chapter, destroy 1 of your ships."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Saint",
        "abilities": (
            "**Sacred:** At the end of each chapter, for each ambition a Rival won that chapter, they must give you a resource. If they can’t, they must give you a Guild card.\n"
            "**Blessed:** Before scoring, if there is any ambition marker left unplaced, you may declare any ambition.\n"
            "**Corrupted:** At the end of each chapter, discard 1 resource for each ambition you won this chapter."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Seer",
        "abilities": (
            "**Reflective:** At the start of each turn, choose a Guild card in the Court. You may use all its abilities this turn, except its Prelude action.\n"
            "**Unstable:** You cannot have more than 1 resource type on your player board."
        ),
        "resources": ["Psionic", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Terrestrial",
        "abilities": (
            "**Symbiotic:** You may place pieces you build in adjacent systems with no rival pieces.\n"
            "**Fertile:** Gain 1 Material when you build a starport; gain 1 matching resource when you build a city.\n"
            "**Sprouting:** At the start of each chapter, you may replace one Loyal building with a ship.\n"
            "**Rooted:** You cannot battle in clusters where you have no buildings."
        ),
        "resources": ["Material", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "city", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        },
        "body_font_size": 17
    },
    {
        "name": "Manipulator",
        "abilities": (
            "**Scheming:** When you score second place in an ambition, gain a Weapon and Relic.\n"
            "**Clever:** When you declare an ambition, you may move the ambition marker up or down one box.\n"
            "**Fraudulent:** When an ambition has multiple markers, you only score Power for the highest one and get no city bonus."
        ),
        "resources": ["Weapon", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Sentinel",
        "abilities": (
            "**Vigilant:** After moving, you may place a ship from anywhere on the map in a gate.\n"
            "**Assertive:** When attacking in battle, deal 1 extra hit.\n"
            "**Cautious:** You cannot roll more Raid and Assault dice combined than you have fresh attacking ships."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Prefect",
        "abilities": (
            "**Judicious:** In scoring, if any players tie for first in an ambition, you gain the initiative.\n"
            "**Immunized:** If you have the initiative you don't provoke Outrage.\n"
            "**Constrained:** In battle, when you Ransack the Court, you take a normal secure action instead."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Ghost",
        "abilities": (
            "**Manifested:** When you Catapult move, your ships may move through one Rival-controlled system. If you move through one, you may influence a card after the move.\n"
            "**Directionless:** You cannot move each ship more than once per turn. You cannot end your Catapult move in the system you catapulted from."
        ),
        "resources": ["Fuel", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    # Continue adding the rest (Desecrator, Chosen, Sage, Gambler) in the same format.
]
leaders += [
    {
        "name": "Desecrator",
        "abilities": (
            "**Unholy:** In your Prelude, you may damage and destroy Rival buildings you control and Loyal pieces.\n"
            "**Reaping:** After you place an agent to provoke Outrage, gain a resource you have not Outraged.\n"
            "**Ascendant:** After Sacrificial if you performed it, if you control no buildings, secure the top card of the Court discard pile; if you control no systems, fill up your empty resource slots with any resources you have not outraged.\n"
            "**Sacrificial:** At the end of each chapter, Outrage half of your not Outraged resources, scrap half of the agents or scrap half of the ships in your supply (rounded up). You can only scrap if it would scrap at least 2. If you did, perform Ascendant."
        ),
        "resources": ["Material", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "city", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        },
        "body_font_size": 13  # custom body font size
    },
    {
        "name": "Chosen",
        "abilities": (
            "**Hallowed:** In setup, choose a ship you place to be the chosen ship. When anyone destroys it, they place it fresh in any system. Once per turn, after it moves, it may battle by itself. In battle, the die it rolls has the following effects: Skirmish: double damage; Assault: self hit gives 1 key, intercept gives 2 keys; Raid: each key repairs 1 Loyal ship after the battle.\n"
            "**Forsaken:** If you have not attacked with the chosen ship this chapter, you cannot secure or declare any ambition."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        },
        "body_font_size": 16
    },
    {
        "name": "Sage",
        "abilities": (
            "**Arcane:** In setup, gain 5 extra Lore cards.\n"
            "**Elusive:** Players may influence and secure your lore. When you secure your own lore, you may discard it to gain a new one. At the end of each chapter, gain a lore per lore that was taken from you. If the lore deck is empty, reshuffle the lore discard."
        ),
        "resources": ["Relic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "starport", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        }
    },
    {
        "name": "Gambler",
        "abilities": (
            "**Daring:** At the start of your turn you may pass the initiative to any player and guess a suit. If they have it, they must play the lowest card of that suit they have, you gain a Psionic and you may surpass only with cards of other suits. (The original suit wins the trick if you tie.)\n"
            "**Brash:** If you guess incorrectly you cannot surpass this round. You must pass this initiative if you have it at the start of the chapter."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city", "damaged": False},
            "B": {"ships": 3, "building": "city", "damaged": False},
            "C": {"ships": 2, "building": "None", "damaged": False}
        },
        "body_font_size": 17
    }
]
