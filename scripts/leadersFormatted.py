leaders = [
    {
        "name": "Kaiju",
        "abilities": (
            "**Devouring:** When you destroy a city, repair all your ships in its cluster.\n"
            "**Feared:** When you tax a city you control, damage it."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 4, "building": "city"},
            "B": {"ships": 4, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Shapeshifter",
        "abilities": (
            "**Mimicry:** When any player declares an ambition, gain a resource of its type.\n"
            "**Flickering:** At the end of each chapter, discard all your resources, then gain 1 Material."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Sentient",
        "abilities": (
            "**Formless:** At the start of each chapter, choose a gate. Until the end of the chapter, you may Catapult and build ships there any number of times per turn.\n"
            "**Shapeless:** In setup, scrap all your starports."
        ),
        "resources": ["Fuel", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 2, "building": "None"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Hierarch",
        "abilities": (
            "**Zealous:** When you influence a card with a rival agent, you may influence another card with a rival agent.\n"
            "**Rigid:** You cannot influence when you Pivot."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Smuggler",
        "abilities": (
            "**Resourceful:** When you battle and roll any raid dice, you may steal 1 resource for free.\n"
            "**Infamous:** When you destroy a building, scrap 1 agent or 1 ship in your supply."
        ),
        "resources": ["Fuel", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "General",
        "abilities": (
            "**Blitzing:** Prelude: You may spend resources to battle.\n"
            "**Reckless:** In battle, for each intercept you roll, take 1 self hit."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Necromancer",
        "abilities": (
            "**Arising:** When you destroy any piece, you may place a matching fresh piece of your own there.\n"
            "**Gravebound:** In setup, damage both of your buildings. You cannot build fresh pieces and build them damaged instead. You cannot repair buildings."
        ),
        "resources": ["Psionic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Composer",
        "abilities": (
            "**Elegant:** When you spend a pip to repair, gain 1 resource.\n"
            "**Obsessed:** You cannot build in clusters where any of your pieces are damaged."
        ),
        "resources": ["Material", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Maw",
        "abilities": (
            "**Voracious:** When you declare an ambition, place a ship anywhere on the map.\n"
            "**Crushing:** When more than 1 Rival ship enters a planetary system you control, you destroy 1 of those ships.\n"
            "**Erratic:** At the end of each chapter, destroy 1 of your ships."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Saint",
        "abilities": (
            "**Sacred:** At the end of each chapter, for each ambition a Rival won that chapter, they must give you a resource. If they can’t, they must give you a Guild card.\n"
            "**Blessed:** Before scoring, if there is an ambition marker left unplaced, you may declare an ambition.\n"
            "**Corrupted:** After sacred, at the end of each chapter, discard 1 resource per ambition you won this chapter."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 17
    },
    {
        "name": "Seer",
        "abilities": (
            "**Reflective:** You play as if you have all cards in the court: you have all their icons and can use all their abilities, but you cannot use prelude actions that would discard them.\n"
            "**Ethereal:** When you secure a vox card, you may bury it to secure the top card of the court deck instead.\n"
            "**Unstable:** You cannot have more than 1 resource type on your player board."
        ),
        "resources": ["Psionic", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
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
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
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
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
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
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
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
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Ghost",
        "abilities": (
            "**Manifested:** When you Catapult move, your ships may move through one Rival-controlled system. If you move through one, you may influence a card after the move.\n"
            "**Directionless:** You cannot move each ship more than once per turn. You cannot end your Catapult move in the system you catapulted from."
        ),
        "resources": ["Fuel", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Desecrator",
        "abilities": (
            "**Unholy:** In your Prelude, you may damage and destroy Rival buildings you control and Loyal pieces. After you destroy a loyal city, scrap it.\n"
            "**Reaping:** After you provoke outrage, gain a non-Outraged resource.\n"
            "**Ascendant:** After Sacrificial, if you control no buildings, secure the top card of the Court discard pile, if you control no systems, fill up your empty resource slots with any resources.\n"
            "**Sacrificial:** At the end of each chapter, if you did not outrage any non-Outraged resource this chapter, do so now, if you did not scrap any city this chapter, scrap any loyal city now, then resolve Ascendant."
        ),
        "resources": ["Material", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 13
    },
    {
        "name": "Chosen",
        "abilities": (
            "**Hallowed:** In setup, choose a ship you place to be the chosen ship. When anyone destroys it, they place it fresh in any system. Once per turn, after it moves, it may battle by itself. In battle, the die it rolls has the following effects: Skirmish: double damage; Assault: self hit gives 1 key, intercept gives 2 keys; Raid: each key repairs 1 attacking Loyal ship after the battle.\n"
            "**Forsaken:** If you have not attacked with the chosen ship this chapter, you cannot secure or declare an ambition."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 15
    },
    {
        "name": "Sage",
        "abilities": (
            "**Arcane:** In setup, gain 5 extra Lore cards.\n"
            "**Elusive:** Players may influence and secure your lore. When you secure your own lore, you may discard it to gain a new one. At the end of each chapter, gain a lore per lore that was taken from you. If the lore deck is empty, reshuffle the lore discard."
        ),
        "resources": ["Relic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Gambler",
        "abilities": (
            "**Cunning:** When you pass the initiative, you may pass it to any player and guess a suit. If they have it, they must play the lowest card of that suit they have, you gain any resource and you may surpass with cards of any suit. (The original suit wins the trick if you tie.) If you guess incorrectly, you cannot surpass this round.\n"
            "**Compulsive:** You must pass the initiative the first time you have it each chapter."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 17
    }
]
