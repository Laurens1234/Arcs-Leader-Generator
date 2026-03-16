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
            "*Zealous.* After you **influence** a card with a rival agent, you may influence a different card with a rival agent.\n"
            "*Rigid.* You cannot **influence** when you Pivot."
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
            "*Hunted.* After you destroy a building in **battle**, the defender may take a free move action."
        ),
        "resources": ["Fuel", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # General
    {
        "name": "General",
        "abilities": (
            "*Blitzing.* After you **tax**, you may discard a resource to gain a Weapon. When attacking in **battle**, you may discard a Weapon to ignore one rolled intercept.\n"
            "*Reckless.* In **battle**, you must always roll at least 1 die of each type if you can. (1 type with 1, 2 with 2.)"
        ),
        "resources": ["Weapon", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
    },
    # Necromancer
    {
        "name": "Necromancer",
        "abilities": (
            "*Arising.* After you destroy a piece in **battle**, you may place a matching fresh loyal piece there.\n"
            "*Gravebound.* In **setup**, damage both of your buildings. You cannot **build** fresh pieces and place them damaged instead. You cannot repair buildings."
        ),
        "resources": ["Psionic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
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
            "*Erratic.* In **scoring**, destroy 1 loyal fresh ship for each ambition you win."
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
            "*Sacred.* When a Rival wins an ambition, they must give you a resource. If they can't, they must give you a Guild card.\n"
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
            "*Reflective.* After you discard a Guild card, you may influence.\n"
            "*Unstable.* Discard a Guild card if you have two or more of the same type."
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
            "*Sprouting.* At the start of each chapter, you may replace one Loyal building with a ship.\n"
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
    # Manipulator
    {
        "name": "Manipulator",
        "abilities": (
            "*Clever.* When you **declare** **an** **ambition**, you may move any agents in the Court to other cards.\n"
            "*Fraudulent.* When you **secure** a card with rival agents on it, capture at most one and place the rest on other cards."
        ),
        "resources": ["Weapon", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Sentinel
    {
        "name": "Sentinel",
        "abilities": (
            "*Assertive.* When attacking in **battle**, deal 1 extra hit.\n"
            "*Cautious.* You cannot roll more Raid and Assault dice than you have fresh attacking ships."
        ),
        "resources": ["Material", "Fuel"],
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
            "*Immunized.* If you have the initiative you don't provoke Outrage.\n"
            "*Constrained.* In **battle**, when you Ransack the Court, you take a normal secure action instead."
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
            "*Manifested.* When you Catapult **move**, your ships may move through one Rival-controlled gate. If they do, you may influence.\n"
            "*Directionless.* You can use at most one **move** action each turn. You cannot end a Catapult **move** in a system with a loyal starport."
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
            "*Hallowed.* In **setup**, choose a ship you place to be the chosen ship. When anyone destroys it, they place it fresh in any system. Once per turn, after it **moves**, it may battle by itself. In battle, the die it rolls has its result count twice.\n"
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
            "*Cunning.* You may pass the initiative to any player, then guess a suit. If they have it, they must play the lowest card of that suit they have and the card you play that round additionally has the pips of that card.\n"
            "*Compulsive.* You must pass the initiative the first time you have it each chapter."
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
            "*Exorbitant.* You can only **build** starports at cities, once per city per turn.\n"
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
            "*Elusive.* After you **tax** a city, you may place it in any building slot you control.\n"
            "*Unmasked.* When you **tax** a rival city, you only gain a captive or resource, not both."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Weaver
    {
        "name": "Weaver",
        "abilities": (
            "*Interwoven.* After you use a pip to **secure**, you may influence an adjacent card.\n"
            "*Tangled.* You must discard a resource to **influence** a card with any Rival agents on it."
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
            "*Lucid.* When you **declare** **an** **ambition**, gain 1 Lore card.\n"
            "*Blurred.* Your lore cards have a raid cost of 3 keys."
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
            "*Distracted.* After **scoring**, discard a resource matching each declared ambition."
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
        "name": "Herald",
        "abilities": (
            "*Baneful.* When you **secure** a card, discard it without effect, then look at the top 3 cards of the Court deck, secure 1, put 1 in the Court and bury 1.\n"
            "*Scathing.* After you discard a Guild card with its Prelude action, shuffle it back into the Court deck."
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
        "resources": ["Psionic", "Relic"],
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
            "*Visionary.* You may build using **repair**. After you repair a piece you may build.\n"
            "*Meticulous.* You cannot **tax** if any of your pieces are damaged."
        ),
        "resources": ["Material", "Fuel"],
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
            "*Venerated.* After a **battle** where a rival destroys any of your pieces, gain a resource matching its system (none if in gate).\n"
            "*Selfless.* When attacking in **battle**, any hits that would damage a city damage your fresh ships first. Provoke outrage if you harm any city."
        ),
        "resources": ["Psionic", "Material"],
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
            "*Pyromaniacal.* After you destroy a city in a system you control or a loyal city, destroy all damaged pieces there.\n"
            "*Insatiable.* At the end of each chapter, if you did not destroy a city this chapter, destroy a loyal city or a city you control."
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
            "*Frugal.* If you start a turn with no resources and no Guild cards, gain any resource.\n"
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
            "*Savage.* When you **battle** in a system with no buildings, collect 1 extra die.\n"
            "*Uncivilized.* When you **secure** a card with any rival agents, destroy one of your pieces."
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
            "*Conductive.* Once per turn, you may spend a resource as a resource no player has provoked Outrage in.\n"
            "*Overloaded.* In **setup**, provoke Weapon Outrage."
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
            "*Guiding.* Once per turn, when a rival tries to **influence** a card with one of your agents, you may force them to influence another card.\n"
            "*Straining.* To **secure** a card with a rival agent on it, you must have 2 more agents on it than them instead of 1."
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
            "*Overclocked.* If you spend 2 or more resources, you may influence at the end of your Prelude.\n"
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
            "*Ironclad.* After a **battle**, you may discard a resource to keep all your destroyed ships from that battle damaged instead.\n"
            "*Cold.* At the end of each chapter, destroy all your damaged ships."
        ),
        "resources": ["Material", "Fuel"],
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
            "*Settled.* **Prelude:** You may move freely from planets (no Catapult moves).\n"
            "*Rooted.* When your ships Catapult **move** into an enemy-controlled gate, one of them takes a hit."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 4, "building": "city"},
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
            "*Obliged.* To score points from an ambition, you must return a trophy or captive, if you don't, score no points."
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
            "*Genesis.* At the start of each chapter, place a resource from the fullest supply on any planet (if tied, choose). That planet gains that resource type. Also do this for a system after you destroy a city in it.\n"
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
            "*Misdirecting.* Before you play an action card, you may swap a facedown action card with one of yours without looking at it first. Put yours face-up.\n"
            "*Revealed.* When you discard a card to seize or copy, place it faceup."
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
            "*Wayfaring.* When you **move**, you may take **any** pieces you control with you. Cities in gates match the resource types of each planet in its cluster. If there is no space on a planet, place the building outside the building slots until there is.\n"
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
            "*Radical.* When you discard a card to seize, you may destroy a city you control to steal a Guild card from a player which type matches your or their outrage.\n"
            "*Fervent.* In **setup**, destroy both of your cities."
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
            "*Wrathful.* In **setup**, **Provoke** **Outrage** in all resource types, then gain any 2 resources."
        ),
        "resources": ["Fuel", "Material"],
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
            "*Cunning.* **Prelude:** Once per turn, you may **Provoke** **Outrage** in a resource type, then secure cards from the top of the deck matching the amount of cards you just discarded. Then gain **any** resources matching the amount you've just discarded.\n"
            "*Irate.* In **setup**, provoke Relic or Psionic outrage."
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
            "*Meticulous.* When you **secure** a card, you may discard it to secure the top two cards of the lore deck.\n"
            "*Ascetic.* At the end of each chapter, give two lore cards to other players, divided as you choose."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1
        },
    {
        "name": "Cartographer",
        "abilities": (
            "*Exploratory.* When you **move**, you may move ships from two different systems instead of one.\n"
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
            "*Vigilant.* When a fresh Rival ship moves into a gate you control, you may gain 1 resource matching any city in that gate's cluster.\n"
            "*Heedless.* Damaged ships may continue moving after moving into a gate you control."
        ),
        "resources": ["Material", "Psionic"],
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
        "resources": ["Material", "Fuel"],
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
            "*Imposing.* After any player whose city you control takes a **tax** action, you may also **tax**. After any player whose starport you control takes a **build** action, you may also **build**.\n"
            "*Munificent.* At the end of each chapter, give 1 resource to each player whose building you control."
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
            "*Mercantile.* When you **influence** a card, you may place 1 of your resources on it to influence it again. When it is **secured**, the player who secures it gains those resources. When a card with resources is Ransacked, only the resources on it are gained.\n"
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
            "*Ruinous.* In **battle**, if the defender has any buildings in the system, you may collect 1 extra Assault die.\n"
            "*Brutal.* When you destroy a building in **battle**, destroy 1 of your ships in that system."
        ),
        "resources": ["Weapon", "Weapon"],
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
            "*Swift.* At the start of each chapter, each rival player places an agent on a planet with none of your ships (then the player on your left places 2 of yours in 2p and 1 in 3p), when you move a ship into one, gain a resource matching that planet and return the agent.\n"
            "*Careless.* You cannot score city bonus points if you have not returned all agents on the board."
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
            "A": {"ships": 3, "building": "None"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.25,

    },
    {
        "name": "Highroller",
        "abilities": (
            "*Audacious.* After you roll dice in **battle**, you may damage 1 of your attacking ships to reroll all dice.\n"
            "*Feverish.* After you reroll dice in **battle**, Provoke Outrage in any resource."
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
            "*Incendiary.* When attacking in **battle**, before collecting dice, you may destroy fresh 1 attacking ship to destroy 2 defending ships.\n"
            "*Abhored.* When you destroy a starport also provoke outrage of its system."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Musician",
        "abilities": (
            "*Inspiring.* Instead of discarding a card to seize, you may give 1 resource to the player with the initiative to seize it.\n"
            "*Temperamental.* When you gain the iniative, damage 1 loyal ship."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    }

]
