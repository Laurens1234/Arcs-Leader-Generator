leaders = [
    # Kaiju
    {
        "name": "Kaiju",
        "abilities": (
            "*Devouring.* When you destroy a city, repair all your ships in its cluster.\n"
            "*Feared.* When you **tax** a city you control, damage it."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 4, "building": "city"},
            "B": {"ships": 4, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15,
        "boundary_shift": 0.12
    },
    # Shapeshifter
    {
        "name": "Shapeshifter",
        "abilities": (
            "*Mimicry.* When any player **declares** **an** **ambition**, gain a resource of its type. (Weapon for Warlord, you choose Material or Fuel for Tycoon.)\n"
            "*Flickering.* At the end of each chapter, discard all your resources, then gain 1 Material."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.1,
        "boundary_shift": 0.1
    },
    # Sentient
    {
        "name": "Sentient",
        "abilities": (
            "*Formless.* At the start of each chapter, choose a gate. Until the end of the chapter, you may Catapult and **build** ships there any number of times per turn. (You do not need any Loyal pieces to build them.)\n"
            "*Shapeless.* In **setup**, scrap all your starports."
        ),
        "resources": ["Fuel", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 2, "building": "None"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Hierarch
    {
        "name": "Hierarch",
        "abilities": (
            "*Entitled.* At the end of your turn, influence a card where you are tied with another player.\n"
            "*Rigid.* You cannot **influence** on a turn in which you Pivot."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Smuggler
    {
        "name": "Smuggler",
        "abilities": (
            "*Opportunistic.* When you **battle** and roll any raid dice, you may steal 1 resource for free.\n"
            "*Hunted.* After you destroy a building in **battle**, the defender may force you to move all your ships back into the gate."
        ),
        "resources": ["Fuel", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Manipulator
    {
        "name": "Manipulator",
        "abilities": (
            "*Clever.* When you **declare** **an** **ambition**, you may move any agents on cards to other cards.\n"
            "*Fraudulent.* When you **secure** a card with rival agents on it, capture/take only 1 and place the rest on other cards."
        ),
        "resources": ["Weapon", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Necromancer
    {
        "name": "Necromancer",
        "abilities": (
            "*Arising.* After **any** **battle**, for each piece you destroyed, you may place a matching fresh loyal piece there.\n"
            "*Gravebound.* In **setup**, damage both of your buildings. You cannot **build** fresh pieces, place them damaged instead."
        ),
        "resources": ["Psionic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Composer
    {
        "name": "Composer",
        "abilities": (
            "*Elegant.* When you spend a pip to **repair**, gain 1 resource.\n"
            "*Obsessed.* You cannot **build** or **tax** in clusters where any of your pieces are damaged."
        ),
        "resources": ["Material", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Maw
    {
        "name": "Maw",
        "abilities": (
            "*Voracious.* When you **declare** **an** **ambition**, place a ship in any system.\n"
            "*Crushing.* When more than 1 Rival ship moves into a planet you control, you destroy 1 of those ships.\n"
            "*Starving.* In **scoring**, if Warlord is declared and you don't win it, scrap 2 loyal ships."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Saint
    {
        "name": "Saint",
        "abilities": (
            "*Sacred.* When a Rival wins an ambition, they give you a resource. If they can't, they give you a Guild card.\n"
            "*Blessed.* Before **scoring**, you may **declare** **an** **ambition**.\n"
            "*Corrupted.* When you win an ambition, discard a resource. If you can't, discard a Guild card."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Seer
    {
        "name": "Seer",
        "abilities": (
            "*Prescient.* After you discard a Guild card, you may take an action on the **Lead** **card**.\n"
            "*Narrow-minded.* You **cannot** take more than 2 different types of standard actions each turn."
        ),
        "resources": ["Psionic", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Terrestrial
    {
        "name": "Terrestrial",
        "abilities": (
            "*Symbiotic.* You may **build** in adjacent systems with no rival pieces.\n"
            "*Fertile.* Gain 1 Material when you **build** a starport; gain 1 matching resource when you **build** a city.\n"
            "*Sprouting.* At the start of each chapter, you may replace a Loyal building with a ship.\n"
            "*Rooted.* You cannot **battle** in clusters where you have no buildings."
        ),
        "resources": ["Material", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.155,
        "boundary_shift": -0.02
    },
    # General
    {
        "name": "General",
        "abilities": (
            "*Blitzing.* In **battle**, you may discard a resource to ignore all intercepts.\n"
            "*Insurmountable.* In **battle**, if you have more fresh ships, collect 1 extra die.\n"
            "*Reckless.* In **battle**, you must always roll at least 1 die of each type if you can."
        ),
        "resources": ["Weapon", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Sentinel
    {
        "name": "Sentinel",
        "abilities": (
            "*Assertive.* At the start of **battle**, if you control the gate of the cluster the battle is in, deal 1 hit.\n"
            "*Cautious.* You cannot roll more raid and assault dice than you have fresh attacking ships."
        ),
        "resources": ["Material", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.3,
        "boundary_shift": 0.9
    },
    # Prefect
    {
        "name": "Prefect",
        "abilities": (
            "*Judicious.* In **scoring**, if any players tie for first in an ambition, you gain the initiative.\n"
            "*Immunized.* If you have the initiative you don't **Provoke** **Outrage**.\n"
            "*Fair.* Before **scoring**, the Rival player with the least Power may take a resource or 3 power from you."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.45,
        "boundary_shift": 0.33
    },
    # Ghost
    {
        "name": "Ghost",
        "abilities": (
            "*Manifested.* Once per turn, when you Catapult **move**, your ships may move through one Rival controlled gate. If you do, you may influence.\n"
            "*Directionless.* You can use at most one **move** action each turn."
        ),
        "resources": ["Fuel", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1,
        "boundary_shift": 0.1
    },
    # Chosen
    {
        "name": "Chosen",
        "abilities": (
            "*Hallowed.* In **setup**, choose a ship you place to be the chosen ship. When anyone destroys it, they place it fresh in any system. Once per turn, after it **moves**, it may **battle** by itself. In **battle**, the die it rolls has its result count twice.\n"
            "*Forsaken.* If you have not attacked with the chosen ship this chapter, you cannot **secure** or **declare** **an** **ambition**."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Sage
    {
        "name": "Sage",
        "abilities": (
            "*Arcane.* In **setup**, gain 5 extra Lore cards.\n"
            "*Elusive.* Players may **influence** and **secure** your lore. When you **secure** your own lore, gain one lore card."
        ),
        "resources": ["Relic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Gambler
    {
        "name": "Gambler",
        "abilities": (
            "*Cunning.* You may **pass** the initiative to any player, then guess a suit. If they have it, they must play it, and the card you play that round additionally has the pips of the card they play. (Even if you copy or pivot.)\n"
            "*Compulsive.* You must **pass** the initiative the first time you have it each chapter."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Engineer
    {
        "name": "Engineer",
        "abilities": (
            "*Versatile.* Your starports can **move**, **battle**, intercept and control like a ship. You place starports outside building slots.\n"
            "*Exorbitant.* You can only **build** starports at cities, once per city, per turn.\n"
            "*Fragile.* After you Catapult **move**, damage the starport you used."
        ),
        "resources": ["Material", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Magician
    {
        "name": "Magician",
        "abilities": (
            "*Elusive.* After you **tax** a city, you may place it in any building slot you control or swap it with any loyal building.\n"
            "*Unmasked.* When you **tax** a rival city, you only gain a resource or captive, not both."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Weaver
    {
        "name": "Weaver",
        "abilities": (
            "*Interwoven.* When you use a pip to **secure**, you may influence an adjacent card.\n"
            "*Tangled.* You must discard a resource to **influence** a card with only Rival agents on it."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Dreamer
    {
        "name": "Dreamer",
        "abilities": (
            "*Lucid.* When you **declare** **an** **ambition**, gain 1 lore card.\n"
            "*Blurred.* Your lore cards have a raid cost of 2 keys."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Seeker
    {
        "name": "Seeker",
        "abilities": (
            "*Inquisitive.* When you **tax**, gain the resource twice if the matching ambition is declared (Weapon matches Warlord).\n"
            "*Distracted.* After **scoring**, discard one resource matching a declared ambition."
        ),
        "resources": ["Material", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Herald
    {
        "name": "Augur",
        "abilities": (
            "*Baneful.* When you **secure** a card from the court, bury it, then look at the top 2 cards of the Court deck, secure one and bury the other.\n"
            "*Ominous.* After you discard a Guild card using its Prelude action, look at the bottom card of the Court deck. If it shares a resource type with the discarded card, **Provoke** **Outrage** in that type."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2,
        "boundary_shift": 0.25
    },
    # Alchemist
    {
        "name": "Alchemist",
        "abilities": (
            "*Transformative.* When you **declare** **an** **ambition**, discard 1 resource to gain 2 resources of different types other than the one you discarded.\n"
            "*Cautious.* You cannot spend your last resource."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Architect
    {
        "name": "Architect",
        "abilities": (
            "*Visionary.* You may build using **repair**. You may build at any starport you control.\n"
            "*Meticulous.* You cannot **tax** if any of your pieces are damaged."
        ),
        "resources": ["Relic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Martyr
    {
        "name": "Martyr",
        "abilities": (
            "*Venerated.* After defending in a **battle**, if the attacker took any trophies, gain a resource matching the battle's system, gain **any** if in gate.\n"
            "*Selfless.* In **battle** in a system with your ships, any hits that would damage a city damage your fresh ships first instead."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
    },
    # Scourge
    {
        "name": "Scourge",
        "abilities": (
            "*Pyromaniacal.* In **battle**, you may damage cities if your opponent has no fresh ships.\n"
            "*Incendiary.* When you destroy a city, destroy all damaged pieces in its system./n"
            "*Insatiable.* Before **scoring**, if you did not destroy a city this chapter, destroy a city in a system you control or a loyal city."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2,
        "boundary_shift": 0.2
    },
    # Beggar
    {
        "name": "Beggar",
        "abilities": (
            "*Frugal.* If you start a turn with no resources and no Guild cards, gain **any** resource.\n"
            "*Communal.* If you start your turn with any resources, discard 1."
        ),
        "resources": ["Material", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Feral
    {
        "name": "Feral",
        "abilities": (
            "*Savage.* In **battle** in a system with no buildings, collect 2 extra dice.\n"
            "*Uncivilized.* When you **secure** (not ransack) a card with any rival agents on it, destroy a building you control."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Conduit
    {
        "name": "Conduit",
        "abilities": (
            "*Conductive.* Once per turn, you may spend a resource as a resource no player has **Provoked** **Outrage** in.\n"
            "*Overloaded.* In **setup**, Provoke Weapon Outrage."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Puppeteer
    {
        "name": "Puppeteer",
        "abilities": (
            "*Guiding.* Once per turn, when a rival tries to **influence** a card with your agents on it, you may force them to influence any other card instead.\n"
            "*Straining.* To **secure** a card with any rival agents on it, you must have 2 more agents on it than them instead of 1."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Automaton
    {
        "name": "Automaton",
        "abilities": (
            "*Overclocked.* If you spend 2 or more resources, you may **influence** at the end of your Prelude.\n"
            "*Wasteful.* After you **secure** a card using 2 or more agents, scrap an agent."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Golem
    {
        "name": "Golem",
        "abilities": (
            "*Ironclad.* After assinging hits in **battle**, you may discard a resource to keep all your loyal destroyed ships from that battle damaged instead.\n"
            "*Cold.* At the end of each chapter, destroy **all** your damaged ships."
        ),
        "resources": ["Material", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2,
        "boundary_shift": 0.2
    },
    # Solian
    {
        "name": "Solian",
        "abilities": (
            "*Settled.* **Prelude:** You may move freely from planets (no free Catapult moves).\n"
            "*Grounded.* When your ships **move** into an Rival-controlled gate, one of them takes a hit."
        ),
        "resources": ["Relic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2,
        "boundary_shift": 0.4
    },
    # Bargainer
    {
        "name": "Bargainer",
        "abilities": (
            "*Leveraged.* You may return a player’s trophy or captive to **tax** one of their cities.\n"
            "*Obliged.* To gain Power from an ambition, you must return a trophy or captive, if you don't, gain no Power."
        ),
        "resources": ["Weapon", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Terraformer
    {
        "name": "Terraformer",
        "abilities": (
            "*Genesiacal.* At the start of each chapter, place a resource from the fullest supply on a planet you control (if tied, you choose). That planet now has only that resource type. Also do this after you destroy a city on a planet.\n"
            "*Codependent.* When you **tax**, you only gain resources from terraformed planets."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Trickster
    {
        "name": "Trickster",
        "abilities": (
            "*Misdirecting.* Before you play an action card, you may swap a played facedown action card with one of yours without looking at it first. Place yours face-up.\n"
            "*Revealed.* When you discard a card to seize or copy, place it face-up."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1,
        "boundary_shift": 0.25
    },
    # Nomad
    {
        "name": "Nomad",
        "abilities": (
            "*Wayfaring.* When you **move**, you may take **any** pieces you control with you. Cities in gates match the resource types of each planet in its cluster. After moving, if there is no space on a planet, place the building outside the building slots until there is.\n"
            "*Itinerant.* You cannot **tax** cities in planetary systems."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Iconoclast
    {
        "name": "Iconoclast",
        "abilities": (
            "*Radical.* After you discard a card to seize, you may destroy a city you control to steal a Guild card which type matches that city's type.\n"
            "*Fervent.* In **setup**, destroy one of your cities."
        ),
        "resources": ["Psionic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2,
        "boundary_shift": 0.25
    },
    # Fiend
    {
        "name": "Fiend",
        "abilities": (
            "*Gluttonous.* When you **Provoke** **Outrage**, if you already have it outraged, clear it instead and gain that resource thrice.\n"
            "*Wrathful.* In **setup**, **Provoke** **Outrage** in all resource types except 1, then gain any 2 resources."
        ),
        "resources": ["", ""],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1,
        "boundary_shift": 0.35
    },
    # Wheeler-dealer
    {
        "name": "Wheeler-dealer",
        "abilities": (
            "*Cunning.* **Prelude:** When you **declare** **an** **ambition**, you may **Provoke** **Outrage**. \n After you **Provoke** **Outrage**, secure cards from the top of the deck matching the amount of cards you just discarded. Then gain **any** resources matching the amount you've just discarded.\n"
            "*Irate.* In **setup**, Provoke Relic or Psionic Outrage."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1,
        "boundary_shift": 0.1
    },
    # Curator
    {
        "name": "Curator",
        "abilities": (
            "*Meticulous.* When you **secure** a card, you may discard it to gain two lore cards.\n"
            "*Ascetic.* At the end of each chapter, give one lore card to another player. If you're in first place, give away another."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1
    },
    {
        "name": "Cartographer",
        "abilities": (
            "*Exploratory.* When you initiate a Catapult **move**, gain a Fuel.\n"
            "*Distracted.* When you Catapult **move**, after each move you must drop off 1 ship."
        ),
        "resources": ["Fuel", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Custodian",
        "abilities": (
            "*Vigilant.* When a Rival ships **move** into a gate you control, gain 1 resource matching any city in that gate's cluster.\n"
            "*Heedless.* Damaged Rival ships may move again after moving into a gate you control."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Salvager",
        "abilities": (
            "*Opportunistic.* After a **battle** in a system adjacent to one of your ships, if any ship was destroyed in that battle, you may place 1 ship in that system.\n"
            "*Grimy.* At the end of each chapter, damage 1 loyal ship in each system that has any damaged ships."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.25,
        "boundary_shift": 0.25
    },
    {
        "name": "Chief",
        "abilities": (
            "*Imposing.* After any rival player of which you control a city takes a **tax** action, you may **tax**. After any rival player of which you control a starport takes a **build** action, you may **build**.\n"
            "*Bountiful.* At the end of each chapter, give 1 resource to each player of which you control a building."
        ),
        "resources": ["Relic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Duelist",
        "abilities": (
            "*Daring.* In **battle**, if you attack with exactly 1 ship, collect 3 extra dice.\n"
            "*Honor-bound.* In **battle**, if you attack a smaller fleet, you cannot roll assault dice."
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
        "name": "Prophet",
        "abilities": (
            "*Revelatory.* When you **declare** **an** **ambition**, you may **secure** any Guild card in the Court discard pile.\n"
            "*Fatalistic.* You cannot seize the initiative."
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
        "name": "Broker",
        "abilities": (
            "*Mercantile.* When you **influence** a card, you may place 1 of your resources on it to influence it again. When it is **secured**, gain those resources.\n"
            "*Indebted.* When you **declare** **an** **ambition**, discard a resource or return a piece."
        ),
        "resources": ["Relic", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Siegebreaker",
        "abilities": (
            "*Ruinous.* In **battle**, if the defender has any buildings in the system, you may collect 1 extra assault die.\n"
            "*Brutal.* When you destroy a building in **battle**, destroy 1 of your ships in that system (the defender takes it as a trophy)."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Courier",
        "abilities": (
            "*Swift.* At the start of each chapter, place 3 agents on planets with no loyal pieces. When you **move** into one, return the agent and gain a resource matching that planet. (While on a planet an agent is not considered a loyal piece.)\n"
            "*Careless.* You **cannot** gain bonus city Power if you have not returned all agents on the board."
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
        "name": "Forager",
        "abilities": (
            "*Rooting.* When you **move** into a planet with no pieces, gain 1 matching resource.\n"
            "*Territorial.* When you **move** out of a planet, if it would be left empty, you must leave 1 of your pieces there."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.25
    },
    {
        "name": "Highroller",
        "abilities": (
            "*Audacious.* After you roll dice in **battle**, you may damage 1 of your attacking ships to reroll **all** dice.\n"
            "*Feverish.* After you reroll dice in **battle**, **Provoke** **Outrage** in a resource."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Insurgent",
        "abilities": (
            "*Seditious.* After attacking in **battle**, you may **influence** a card with a defender's agent on it.\n"
            "*Decentralized.* You cannot **repair** ships."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Bomber",
        "abilities": (
            "*Incendiary.* When attacking in **battle**, before collecting dice, you may destroy 1 fresh attacking ship to destroy 2 defending ships.\n"
            "*Infamous.* When you destroy a starport, also **Provoke** **Outrage** of its system's tyoe."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Musician",
        "abilities": (
            "*Inspiring.* Instead of discarding a card to seize, you may give two resources they don't have to the player with the initiative to seize it.\n"
            "*Temperamental.* When you gain the initiative, damage 1 loyal ship."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Ozymendias
    {
        "name": "Ozymendias",
        "abilities": (
            "*Hubristic.* When you control all gates, **secure** the entire Court, returning all agents, then you destroy all ships in the gates.\n"
            "*Forgotten.* You cannot **influence** if you control no gates."
        ),
        "resources": ["Weapon", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Collector
    {
        "name": "Collector",
        "abilities": (
            "*Acquisitive.* When you **secure** a card, gain a resource matching its type.\n"
            "*Jaded.* At the end of each chapter, discard a Guild card, if you can't, discard all resources you have."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Samurai",
        "abilities": (
            "*Perfected.* When attacking in **battle**, you may change 1 of your dice to any face (like a reroll).\n"
            "*Honorable.* When attacking in **battle**, return half the pieces you destroy (rounded down)."
        ),
        "resources": ["Weapon", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.3,
        "boundary_shift": 0.4
    },
    # Assasin
    {
        "name": "Assasin",
        "abilities": (
            "*Lethal.* After you **influence**, if you have the most agents on a card, destroy one rival agent on it.\n"
            "*Doomed.* If a Rival has as many or more agents on a card than you, you can only **influence** those cards."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # # Companion
    # {
    #     "name": "Companion",
    #     "abilities": (
    #         "*Helpful.* When a rival **battles**, you may allow them to use your ships like they are loyal. If they do, take 1 of their agents as a favor. You may spend this favor to use their ships like they are loyal in a **battle** on your turn.\n"
    #         "*Entangled.* At the start of each chapter, give 1 favor to a player."
    #     ),
    #     "resources": ["Relic", "Fuel"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # # Witch
    # {
    #     "name": "Witch",
    #     "abilities": (
    #         "*Hexing.* When you **influence** a card, you may discard 1 resource to capture 1 rival agent from that card.\n"
    #         "*Ostracized.* idk."
    #     ),
    #     "resources": ["Psionic", "Relic"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # # Creator
    # {
    #     "name": "Creator",
    #     "abilities": (
    #         "*Ingenious.* When you **build** a ship, you may take it from any rival's supply and build it at any starport. If you build a rival's ship, take a resource matching that system.\n"
    #         "*Onerous.* idk"
    #     ),
    #     "resources": ["Material", "Fuel"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # # Messiah
    # {
    #     "name": "Messiah",
    #     "abilities": (
    #         "*Redemptive.* When you **build** a city in a system with any damaged rival ships, you may replace all those damaged rival ships with loyal fresh ships.\n"
    #         "*Reckoning.* In **scoring**, if you win no ambitions, destroy all your damaged ships."
    #     ),
    #     "resources": ["Relic", "Weapon"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # # Abomination
    # {
    #     "name": "Abomination",
    #     "abilities": (
    #         "*Ravenous.* When you play a card, you may discard a card to take twice as many actions with your played card.\n"
    #         "*Revealed.* When a suit is led, reveal all your matching cards."
    #     ),
    #     "resources": ["Psionic", "Weapon"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # # Crusader
    # {
    #     "name": "Crusader",
    #     "abilities": (
    #         "*Zealous.* When you destroy a building, **secure** a matching card from the Court.\n"
    #         "*Dogmatic.* You cannot **influence** a card with no agents if a rival can secure a card with any of your loyal agents.."
    #     ),
    #     "resources": ["Weapon", "Material"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # # Djinn
    # {
    #     "name": "Djinn",
    #     "abilities": (
    #         "*Wishful.* At the start of your Prelude, name a resource type. Until the end of your turn, you may spend resources only as that type.\n"
    #         "*Bound.* When you have a resource type outraged, you **cannot** spend it."
    #     ),
    #     "resources": ["Relic", "Psionic"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },

    # # Beacon
    # {
    #     "name": "Beacon",
    #     "abilities": (
    #         "*Guiding.* When you **move** into a gate, you may place a beacon there. Beacons allow any player to Catapult **move** through that gate.\n"
    #         "*Radiant.* Before scoring, you may discard a beacon to gain 2 resources."
    #     ),
    #     "resources": ["Fuel", "Material"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "starport"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # }
]
