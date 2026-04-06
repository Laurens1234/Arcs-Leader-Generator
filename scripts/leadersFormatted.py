#general advice: leaders need to have a one word noun as their name
#both abilities are adjectives
#1 negative and 1 possitive
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
            "*Entitled.* At the end of your turn, **influence** a card where you are tied with another player.\n"
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
            "*Clever.* When you **declare** **an** **undeclared** **ambition**, you may move any agents on cards to other cards.\n"
            "*Fraudulent.* When you **secure** a card with Rival agents on it, capture/take only 1 and place the rest on other cards."
        ),
        "resources": ["Psionic", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Necromancer
    {
        "name": "Necromancer",
        "abilities": (
            "*Arising.* After **any** **battle**, for each piece you destroyed, you may place a matching fresh Loyal piece there.\n"
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
            "*Starving.* In **scoring**, if Warlord is declared and you don't win it, scrap 2 Loyal ships."
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
            "B": {"ships": 3, "building": "city"},
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
            "*Symbiotic.* You may **build** in adjacent systems with no Rival pieces.\n"
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
            "*Hallowed.* In **setup**, choose a ship you place to be the chosen ship. When anyone destroys it, they place it fresh in any system. After it **moves**, it may **battle** by itself. In **battle**, the die it rolls has its result count twice.\n"
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
            "*Cunning.* You may **pass** the initiative to any player, then guess a suit. If they have it, they must play it, and the card you play that round additionally has the pips of the card they play. (Even if you Copy or Pivot.)\n"
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
            "*Elusive.* After you **tax** a city, you may place it in any building slot you control or swap it with any Loyal building.\n"
            "*Unmasked.* When you **tax** a Rival city, you only gain a resource or captive, not both."
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
    # Augur
    {
        "name": "Augur",
        "abilities": (
            "*Baneful.* When you **secure** a card, you may bury it to secure the top card of the deck instead.\n"
            "*Accursed.* After you **secure** a card, discard all your matching resources."
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
            "*Pyromaniacal.* Once per **battle**, you may damage a city if your opponent has no fresh ships.\n"
            "*Incendiary.* When you destroy a city, destroy all damaged pieces in its system.\n"
            "*Insatiable.* Before **scoring**, if you did not destroy a city this chapter, destroy a city in a system you control or a Loyal city."
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
            "*Frugal.* If you start your **Prelude** with no resources and no Guild cards, gain **any** resource.\n"
            "*Communal.* If you start your turn with any resources, discard a resource or card."
        ),
        "resources": ["", ""],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Feral
    {
        "name": "Feral",
        "abilities": (
            "*Savage.* In **battle** in a system with no buildings, collect 2 extra dice.\n"
            "*Uncivilized.* When you **secure** (not ransack) a card with any Rival agents on it, destroy a building you control."
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
            "*Guiding.* Once per turn, when a Rival tries to **influence** a card with your agents on it, you may force them to influence any other card instead.\n"
            "*Straining.* To **secure** a card with any Rival agents on it, you must have 2 more agents on it than them instead of 1."
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
            "*Ironclad.* After **any** **battle**, you may discard a resource to keep all your Loyal destroyed ships from that battle damaged instead.\n"
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
            "*Genesiacal.* At the start of each chapter, place a resource from the fullest supply on a planet you control (if tied, you choose). That planet now has only that resource type. Also do this to a planet after you destroy a city on it.\n"
            "*Codependent.* When you **tax**, you only gain resources from altered planets."
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
            "*Revealed.* When you discard a card to seize or Copy, place it face-up."
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
            "*Unadorned.* While you have the fewest resources, ignore the **tax** limit and city control.\n"
            "*Appeasing.* When you **tax** a Rival city, they gain 1 resource of your choice."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Iconoclast
    {
        "name": "Iconoclast",
        "abilities": (
            "*Radical.* After you play an extra action card, you may destroy a city you control to steal a Guild card which matches that city's type.\n"
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
            "*Devious.* When you **declare** **an** **ambition**, you may **Provoke** **Outrage** in any type.\n"
            "*Cunning.* After you **Provoke** **Outrage**, secure cards from the top of the deck matching the amount of cards you just discarded. Then gain **any** resources matching the amount you've just discarded.\n"
            "*Irate.* In **setup**, Provoke Relic or Psionic Outrage."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
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
            "*Exploratory.* After you initiate a Catapult **move**, gain a Fuel.\n"
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
            "*Grimy.* You can build at most 1 ship per turn."
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
            "*Imposing.* After any Rival player of which you control a city takes a **tax** action, you may **tax**. After any Rival player of which you control a starport takes a **build** action, you may **build**. You may build at and Catapult from Rival starports you control.\n"
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
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Broker",
        "abilities": (
            "*Mercantile.* When you **influence** a card, you may place 1 of your resources on it to influence it again. When it is **secured**, gain those resources.\n"
            "*Indebted.* When you **declare** **an** **ambition**, return a piece or give a resource to a Rival."
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
            "*Brutal.* When you destroy a building in **battle**, destroy 1 of your ships in that system."
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
            "*Swift.* At the start of each chapter, place 3 agents on planets with no Loyal pieces. When you **move** into one, return the agent and gain a resource matching that planet. (The agent cannot be battled or used to build at.)\n"
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
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Bomber",
        "abilities": (
            "*Incendiary.* When attacking in **battle**, before collecting dice, you may destroy 1 attacking ship to destroy 2 defending pieces.\n"
            "*Infamous.* When you destroy a starport, also **Provoke** **Outrage** of that starport's planet type."
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
            "*Inspiring.* To seize the iniative, you may give two resources they don't have to the player with the initiative.\n"
            "*Temperamental.* When you gain the initiative, damage 1 Loyal ship."
        ),
        "resources": ["Material", "Fuel"],
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
        "resources": ["Fuel", "Relic"],
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
        "resources": ["Relic", "Relic"],
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
            "*Perfected.* In **battle**, you may change 1 of your dice to any face (like a reroll).\n"
            "*Honorable.* After attacking in **battle**, return half the pieces you took as trophies (rounded down)."
        ),
        "resources": ["Weapon", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.3,
        "boundary_shift": 0.4
    },
    # Assasin
    {
        "name": "Assasin",
        "abilities": (
            "*Lethal.* After you **influence**, if you have the most agents on a card, destroy one Rival agent on it.\n"
            "*Bloodthirsty.* If a Rival has as many or more agents on a card than you, you can only **influence** those cards."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },

    # Witch
    {
        "name": "Witch",
        "abilities": (
            "*Malefic.* When you **secure**, you may capture a Rival agent on another card.\n"
            "*Covenbound.* You cannot **secure** unless there is an agent on another card."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Ambassador
    {
        "name": "Ambassador",
        "abilities": (
            "*Diplomatic.* When you **declare** **an** **ambition**, you may **secure** any number of times.\n"
            "*Unauthorized.* You cannot **secure** unless an ambition has been declared."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Restorer
    {
        "name": "Shaman",
        "abilities": (
            "*Holostic.* When you **declare** **an** **ambition**, you may **repair** damaged ships you don't control.\n"
            "*Disruptive.* You cannot **repair** ships you control."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Mediator
    {
        "name": "Mediator",
        "abilities": (
            "*Conciliatory.* When you **secure** a Guild card, you may discard it to clear its type's **Outrage** and gain a matching resource.\n"
            "*Punitive.* If you **Provoke** **Outrage** in a type you already have outraged, **Provoke** **Outrage** in a type you don't have outraged."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Despot
    {
        "name": "Despot",
        "abilities": (
            "*Autocratic.* When you **declare** **an** **ambition**, you may **tax** one city you control of each player.\n"
            "*Merciless.* At the end of each chapter, destroy one Loyal ship in each system with a city."
        ),
        "resources": ["Fuel", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Viceroy
    {
        "name": "Viceroy",
        "abilities": (
            "*Delegated.* When any player **builds** a city, you may place 1 of your ships in that city's cluster.\n"
            "*Administrative.* In **setup**, scrap 4 starports. If any player destroys your starport, they return it and take two agents instead."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Artificer",
        "abilities": (
            "*Proficient.* After you Copy or Pivot to **build** or **repair**, you may build or repair.\n"
            "*Diligent.* You cannot Pivot if the lead suit is Construction or Administration."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Berserker
    {
        "name": "Warmonger",
        "abilities": (
            "*Blood-soaked.* When you Copy or Pivot to **battle**, you may declare Warlord, if you do, each die you roll has its result count twice.\n"
            "*Glorybound.* In **scoring**, if you win no ambitions, lose 5 Power."
        ),
        "resources": ["Weapon", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Taxman
    {
        "name": "Extortioner",
        "abilities": (
            "*Shrewd.* When you Copy or Pivot to **tax**, you may tax the city of the player who led.\n"
            "*Vindictive.* In **scoring**, if Tyrant is declared and you don't win it, scrap 3 agents."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    }
    # # Prince
    # {
    #     "name": "Prince",
    #     "abilities": (
    #         "*Royal. When you lead you may \"knight\" a Rival's ship, making it Loyal to you for the rest of the turn.\n"
    #         "*Juvenile.* At the end of each chapter, lose 1 ship if you didn't declare an ambition."
    #     ),
    #     "resources": ["Weapon", "Relic"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # }
    # # Companion
    # {
    #     "name": "Companion",
    #     "abilities": (
    #         "*Helpful.* When a Rival **battles**, you may allow them to use your ships like they are Loyal. If they do, take 1 of their agents as a favor. You may spend this favor to use their ships like they are Loyal in a **battle** on your turn.\n"
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
    # # Creator
    # {
    #     "name": "Creator",
    #     "abilities": (
    #         "*Ingenious.* When you **build** a ship, you may take it from any Rival's supply and build it at any starport. If you build a Rival's ship, take a resource matching that system.\n"
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
    #         "*Redemptive.* When you **build** a city in a system with any damaged Rival ships, you may replace all those damaged Rival ships with Loyal fresh ships.\n"
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
    #         "*Dogmatic.* You cannot **influence** a card with no agents if a Rival can secure a card with any of your Loyal agents.."
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
    # },
    # Fabricator

]
