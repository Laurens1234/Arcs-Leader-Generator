# General advice: leaders need to have a one word noun as their name.
# Both abilities are adjectives.
# 1 negative and 1 positive.
leaders = [
    # Kaiju
    {
        "name": "Kaiju",
        "abilities": (
            "*Devouring.* When you destroy a city, **repair** all your ships in its cluster.\n"
            "*Feared.* When you **tax** a city you control, damage it."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 4, "building": "city"},
            "B": {"ships": 4, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.00,
        "boundary_shift": 0.00
    },
    # Shapeshifter
    {
        "name": "Shapeshifter",
        "abilities": (
            "*Mimicry.* When any player **declares** **an** **ambition**, gain a resource of its type. (Weapon for Warlord, you choose Material or Fuel for Tycoon.)\n"
            "*Flickering.* After **scoring**, discard all your resources, then gain 1 Material."
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
            "*Formless.* **At** **the** **start** **of** **each** **chapter**, choose a gate. Until the end of the chapter, you may Catapult and **build** ships there any number of times per turn.\n"
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
        "resources": ["Relic", "Material"],
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
            "*Opportunistic.* In **battle**, if you rolled any {icon:dice_key_black}, you may steal 1 resource for free.\n"
            "*Hunted.* After you destroy a building in **battle**, the defender may move all your attacking ships into a gate."
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
        "body_font_size": 18,
        "zoom": 1.15
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
            "*Crushing.* When any Rival moves ships into a planet you control, you may destroy 1.\n"
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
            "C": {"ships": 3, "building": "None"}
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
            "*Symbiotic.* You may build in adjacent systems with no Rival pieces.\n"
            "*Fertile.* Gain 1 Material when you **build** a starport; gain 1 matching resource when you **build** a city.\n"
            "*Sprouting.* When you **declare** **an** **ambition**, replace any building you control with a ship.\n"
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
            "*Blitzing.* In **battle**, you may discard a resource to ignore all {icon:dice_intercept_black}.\n"
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
            "*Assertive.* At the start of **any** **battle**, if you control the gate of the cluster the battle is in, deal 1 hit.\n"
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
            "*Fair.* Before **scoring**, the Rival with the least Power may take a resource or 3 power from you."
        ),
        "resources": ["Psionic", "Material"],
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
            "*Hallowed.* After you **move** a single ship, you may battle with only it, the die it rolls has its result count thrice.\n"
            "*Forsaken.* If you have not attacked this chapter, you cannot **declare** **an** **ambition**."
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
            "*Arcane.* In **setup**, gain 5 extra Lore.\n"
            "*Elusive.* Players may **influence** and **secure** your lore. When you **secure** your own lore, gain one lore."
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
            "*Cunning.* You may **pass** the initiative to any player, then guess a suit. If they have it, they must play it, and the card you play this round lets you take twice as many actions.\n"
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
            "*Exorbitant.* You can only **build** starports at cities, damaged, once per city, per turn.\n"
            "*Fragile.* After you finish Catapult **moving**, damage the starport you used."
        ),
        "resources": ["Material", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15
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
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    # Weaver
    {
        "name": "Weaver",
        "abilities": (
            "*Interwoven.* When you **secure**, you may influence an adjacent card.\n"
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
            "*Lucid.* When you **declare** **an** **ambition**, gain 1 lore.\n"
            "*Blurred.* Your lore have a raid cost of {icon:dice_key_black} {icon:dice_key_black}."
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
            "C": {"ships": 3, "building": "None"}
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
            "*Visionary.* You can **build** at loyal cities and **tax** loyal starports.\n"
            "*Meticulous.* You cannot **move** if you would lose control of a building."
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
            "*Venerated.* After defending in a **battle**, if the attacker took any trophies, gain any resource.\n"
            "*Selfless.* In **any** **battle** in a system with your ships, any hits that would damage a city damage your fresh ships first instead."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
    },
    # Scourge
    {
        "name": "Scourge",
        "abilities": (
            "*Pyromaniacal.* When attacking in **battle**, at the start, you may return any number of trophies matching the defender; deal 1 hit for each.\n"
            "*Insatiable.* Before **scoring**, if you have no cities as trophies, destroy a Loyal city."
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
            "*Communal.* If you start your turn with any resources, discard a resource or any card."
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
            "*Overclocked.* If you spend 2 or more resources, you may influence at the end of your Prelude.\n"
            "*Wasteful.* After you **secure** a card using 2 or more agents, scrap an agent from your supply."
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
            "*Cold.* In **clean** **up**, destroy **all** your damaged ships."
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
            "*Grounded.* When your ships **move** into a Rival-controlled gate, one of them takes a hit."
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
            "*Leveraged.* When you **tax**, you may return a Rival's trophy or captive to tax one of their cities.\n"
            "*Obliged.* In **scoring**, to gain Power from an ambition, you must return a trophy or captive, if you don't, gain no Power."
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
            "*Genesiacal.* **At** **the** **start** **of** **each** **chapter**, place a resource from the fullest supply on a planet with any loyal pieces to change its type. Also do this to a planet after you destroy a city on it.\n"
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
            "*Misdirecting.* When you **declare an** **ambition**, draw up to 2 cards from the bottom of the action card deck, then discard as many.\n"
            "*Revealed.* When you Copy or play an extra card, place it face-up."
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
            "*Radical.* When you **declare** **an** **ambition**, you may destroy a city you control to steal a Guild card matching that city's type.\n"
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
        "name": "Wheeler-Dealer",
        "abilities": (
            "*Devious.* When you **declare** **an** **ambition**, you may **Provoke** **Outrage** in a non-Outraged type to **clear** **Outrage** in a different type. Then, take and spend 1 resource from the cleared type’s supply.\n"
            "*Irate.* In **setup**, Provoke Relic or Psionic Outrage."
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
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
            "*Meticulous.* When you **secure** a card, you may discard it to gain 2 lore.\n"
            "*Ascetic.* After **scoring**, give 1 lore to another player. If you're in first place, give away another."
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
            "*Exploratory.* After you **move** from a starport, gain a Fuel.\n"
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
            "*Vigilant.* When a Rival **moves** into a gate you control, gain 1 resource matching any city in that gate's cluster.\n"
            "*Heedless.* After damaged Rival ships **move** into a gate you control, they may move again."
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
            "*Opportunistic.* After **any** **battle** in a system adjacent to one of your ships, if any ship was destroyed in that battle, you may place 1 ship in that system.\n"
            "*Grimy.* You can **build** at most 1 ship per turn."
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
            "*Imposing.* After any Rival of whom you control a building **taxes** or **builds**, you may tax or build respectively.\n"
            "*Bountiful.* Before **scoring**, give 1 resource to each player of whom you control a building."
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
            "*Revelatory.* When you **declare** **an** **ambition**, you may secure a Guild card in the Court discard pile which type matches the declared ambition.\n"
            "*Fatalistic.* You cannot seize the initiative."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Broker",
        "abilities": (
            "*Mercantile.* When you **influence** a card, you may place 1 of your resources on it to influence it again. When anyone **secures** it, they gain those resources.\n"
            "*Indebted.* To **declare** **an** **ambition**, you must return a piece or give a resource to a Rival."
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
            "*Brutal.* In **battle**, {icon:dice_intercept_black} on Assault dice you roll also count as {icon:dice_self_hit_black}."
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
            "*Swift.* **At** **the** **start** **of** **each** **chapter**, place 3 agents on planets with no Loyal pieces. When you **move** into one, return the agent and gain a resource matching that planet. (The agent cannot be battled or used to build at.)\n"
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
            "*Territorial.* When you **move** out of a planet, if it's left empty, build a building there."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.25
    },
    {
        "name": "High-Roller",
        "abilities": (
            "*Audacious.* After you roll dice in **battle**, you may damage 1 of your attacking ships to reroll **all** dice.\n"
            "*Feverish.* After you reroll dice in **battle**, **Provoke** **Outrage** in any resource."
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
            "*Seditious.* After attacking in **battle**, you may influence a card with a defender's agent on it.\n"
            "*Decentralized.* You cannot **repair** ships."
        ),
        "resources": ["Weapon", "Relic"],
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
            "*Inspiring.* To seize the initiative, you may give two resources to the player with the initiative.\n"
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
    # Ozymandias
    {
        "name": "Ozymandias",
        "abilities": (
            "*Hubristic.* When you control all gates, **secure** the entire Court, returning any agents, then destroy all loyal ships in the gates.\n"
            "*Forgotten.* You cannot **influence** if you control no gate."
        ),
        "resources": ["Fuel", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Collector",
        "abilities": (
            "*Acquisitive.* When you **secure** a card, gain a resource matching its type.\n"
            "*Jaded.* After **scoring**, discard a Guild card, if you can't, discard all resources you have."
        ),
        "resources": ["Relic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15
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
    # Assassin
    {
        "name": "Assassin",
        "abilities": (
            "*Lethal.* After you **influence**, if you have the most agents on a card, you destroy one Rival agent on it.\n"
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
            "*Malefic.* When you **secure**, you may capture a Rival agent on an adjacent card.\n"
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
            "*Diplomatic.* When you **declare** **an** **ambition**, you may secure any number of times.\n"
            "*Unauthorized.* You cannot **secure** unless an ambition is declared."
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
            "*Holistic.* When you **declare** **an** **ambition**, you may repair all your damaged ships.\n"
            "*Disruptive.* You cannot **repair** with pips."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
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
            "*Autocratic.* When you **declare** **an** **ambition**, you may tax one city you control of each player.\n"
            "*Merciless.* After **scoring**, damage one Loyal ship in each system with a city."
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
            "*Administrative.* In **setup**, scrap 4 starports."
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
            "*Bloodsoaked.* When you Copy or Pivot to **battle**, you may declare Warlord, if you do, each die you roll has its result count twice.\n"
            "*Hellbent.* In **scoring**, if you win no ambitions, lose 5 Power."
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
        "name": "Extortioner",
        "abilities": (
            "*Shrewd.* When you Copy or Pivot to **tax**, you may tax a city of the player who led.\n"
            "*Vindictive.* In **scoring**, if Tyrant is declared and you don't win it, scrap 3 agents."
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
        "name": "Emperor",
        "abilities": (
            "*Imperial.* In **scoring**, your city bonus is 2 Power per city you control.\n"
            "*Exacting.* In **scoring**, you don't gain Power for second place unless you tied for first."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Titan",
        "abilities": (
            "*Immovable.* When defending in **battle**, your ships cannot be destroyed unless the attacker controls the gate of the battle system's cluster.\n"
            "*Stationary.* Your damaged ships cannot Catapult **move**."
        ),
        "resources": ["Relic", "Weapon"],
        "setup": {
            "A": {"ships": 4, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Egoist",
        "abilities": (
            "*Willful.* When you Pivot, take any action except those on your played card instead.\n"
            "*Inflexible.* You can only Copy with cards of the lead suit, face up."
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
        "name": "Enforcer",
        "abilities": (
            "*Mandating.* When you **declare** **an** **ambition**, take an action on your played card twice. *(Show* *it* *if* *you* *copied.)*\n"
            "*Unpopular.* You cannot **influence** if no ambitions have been declared."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Treasurer
    {
        "name": "Treasurer",
        "abilities": (
            "*Bankrolled.* **At the start of each chapter**, tax all cities you control.\n"
            "*Deskbound.* You can **tax** at most once per turn."
        ),
        "resources": ["Material", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },

    {
        "name": "Wayfinder",
        "abilities": (
            "*Bridging.* You treat systems with a loyal building as adjacent.\n"
            "*Anchored.* When you Catapult **move**, stop after 2 moves."
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
        "name": "Champion",
        "abilities": (
            "*Victorious.* When you win an ambition, place 3 ships in a matching system or gate, or gain 2 matching resources.\n"
            "*Humbled.* When you get second place, discard all your resources matching that ambition."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Tribune",
        "abilities": (
            "*Endorsed.* After you destroy a starport, ransack the Court like you destroyed a city.\n"
            "*Sanctioned.* When you destroy a city, don't ransack the Court."
        ),
        "resources": ["Relic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15
    },
    # Dissector
    {
        "name": "Dissector",
        "abilities": (
            "*Incisive.* When you take an action, you may return 1 captive or scrap 1 agent from your supply to take any different action instead.\n"
            "*Sadistic.* Before **scoring**, scrap 2 agents from your supply, return 2 captives, or 1 of each."
        ),
        "resources": ["Relic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },

    # 
    {
        "name": "Schemer",
        "abilities": (
            "*Manipulative.* After you **influence**, you may move 1 loyal agent on a card to a different card.\n"
             "*Compromised.* In **clean** **up**, return all your agents from a card where you have at least 1 loyal agent."
        ), 
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15
    },

    # Hydra
    {
        "name": "Hydra",
        "abilities": (
            "*Regenerative.* After **any** **battle**, if 2+ of your loyal pieces got destroyed, you may place 1 loyal ship from any trophy box in any system with loyal pieces.\n"
            "*Unwieldy.* You cannot Catapult **move** with more than 3 ships in a single move."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Enchanter",
        "abilities": (
            "*Alluring.* When you copy or pivot to **influence** a card with a rival agent on it, you may replace one of their ships with a loyal one.\n"
            "*Resisted.* If you only have 1 ship in a gate, it doesn't count for control."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15,
    },
    {
        "name": "Creator",
        "abilities": (
            "*Cosmic.* When you **build**, you may instead take a ship from a Rival's supply and place it fresh one of their starports, if you do, gain a resource matching that system.\n"
            "*Detached.* In **cleanup**, you always return all trophies, even if Warlord was not declared."
        ),
        "resources": ["Material", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15,
        "boundary_shift": 0.00
    },
    # Messiah
    {
        "name": "Messiah",
        "abilities": (
            "*Salvific.* When you **build** a city in a system with any damaged ships, you may repair all ships in that system, then replace all repaired Rival ships with Loyal ships.\n"
            "*Reckoned.* In **scoring**, if you win no ambitions, return all your buildings on the map."
        ),
        "resources": ["Weapon", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Abomination
    {
        "name": "Abomination",
        "abilities": (
            "*Frenzied.* When you play a card, you may discard an action card to take twice as many actions with your played card.\n"
            "*Possessed.* When a suit is led, reveal a matching card if you have one."
        ),
        "resources": ["Psionic", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15
    },
    # Crusader
    {
        "name": "Crusader",
        "abilities": (
            "*Zealous.* After you destroy a city, also **secure** any card with no or only Loyal agents on it matching that city's type.\n"
            "*Dogmatic.* You cannot **influence** a card with no agents on it if a Rival can secure a card with any of your Loyal agents on it."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
   # 
    {
        "name": "Phantom",
        "abilities": (
            "*Spectral.* When attacking in **battle**, you may choose to ignore any {icon:dice_hit_black} you roll; at the end of the **battle**, you may move any of your attacking ships once per ignored {icon:dice_hit_black}.\n"
            "*Tethered.* You cannot **move** if you don't control the system you're in."
        ),
        "resources": ["Fuel", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15,
        "boundary_shift": 0.00
    },

    
    {
        "name": "Harbormaster",
        "abilities": (
            "*Portwide.* When you **tax** a city, you may also tax all other cities in its system. When you **build** at a starport, you may also build at all other starports in its system. *(Even Rival ones!)*\n"
            "*Methodical.* You cannot have 2 loyal buildings of different types on a planet"
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "none"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },

    # 
    {
        "name": "Investor",
        "abilities": (
            "*Capitalizing.* In **setup**, gain any 2 resources, place them on this card. This card holds any number of resources. Their raid cost is {icon:dice_key_black} each.\n"
            "*Yielding.* When you **declare an ambition**, gain 1 resource of each type on this card.\n"
            "*Diversified.* When you **tax**, don't gain a resource if you already have a resource of that type."
        ),
        "resources": ["", ""],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },

    # 
    {
        "name": "Envoy",
        "abilities": (
            "*Parleyed.* After *Soft*, you may discard a resource, if you do, the attacker can only collect Skirmish dice.\n"
            "*Soft.* When defending in **battle**, before the attacker collects dice, if the attacker outnumbers you, they may steal 1 resource from you to end the battle immediately."
        ),
        "resources": ["Fuel", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },

    # 
    {
        "name": "Syndic",
        "abilities": (
            "*Networked.* You can **tax** any city in a cluster where you control 2 systems.\n"
            "*Compartmental.* You cannot **build** buildings in systems adjecent to a system with another loyal building."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },

    
    {
        "name": "Sollicitor",
        "abilities": (
            "*Entreating.* When you **declare** **an** **ambition**, you may ask a Rival for a suit, they must give you the highest numbered card of that suit they have. If they did, give them an action card back.\n"
            "*Compelled.* When you lead, you must **declare** **an** **ambition**."
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    
    {
        "name": "Seraph",
        "abilities": (
            "*Celestial.* After you collect dice in **battle**, say a number. You must reroll that many.\n"
            "*Ardent.* You can only reroll dice with {icon:dice_hit_black} or {icon:dice_building_hit_black} on them."
        ),
        "resources": ["Fuel", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15
    },
    {
        "name": "Paragon",
        "abilities": (
            "*Exemplary.* When you Pivot and play a card of equal rank to the lead card, you may use all pips on your played card.\n"
            "*Immutable.* You cannot Pivot with cards of different rank than the lead card.\n"
        ),
        "resources": ["Psionic", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15
    },

    # {
    #     "name": "Forgemaster",
    #     "abilities": (
    #         "*.* In **battle**, you may choose to reroll Assualt and Raid dice one at a time. For each rerolled die that has a self hit, immediately damage one of your ships. You may stop only after rolling a hit or key.\n"
    #         "*."
    #     ),
    #     "resources": ["Weapon", "Relic"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # {
    #     "name": "Oracle",
    #     "abilities": (
    #         "*Prescient.* In **battle**, you may reroll any number of dice in systems matching declared ambitions.\n"
    #         "*Unnerved.* ."
    #     ),
    #     "resources": ["Psionic", "Fuel"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 18
    # },
    # # Dice-mechanic leaders (one per requested mechanic)
    # {
    #     "name": "Setmaker",
    #     "abilities": (  
    #         "*Jackpot.* When you roll only skirmish dice, if all of them hit gain the reward of the amount you rolled and all lower ones:\n"
    #         "1: damage a defending ship (1/2)\n"
    #         "2: gain a resource matching the system (1/4)\n"
    #         "3: all your hits count as keys instead (1/8)\n"
    #         "4: (1/16)\n"
    #         "5: all dice hit and roll again (1/32)\n"
    #         "6: Destroy all defending ships\n"
    #         "Any amount of times in **battle**, you may damage and attacking ship to reroll a dice, then increase its cost by 1 this battle.\n"
    #         "You can only collect Skirmish dice.\n"
    #         "At the end of each **battle**, deal self hits equal to the amount of dice that missed.\n"
    #         ),
    #     "resources": ["Material", "Fuel"],
    #     "setup": {
    #         "A": {"ships": 3, "building": "city"},
    #         "B": {"ships": 3, "building": "starport"},
    #         "C": {"ships": 2, "building": "None"}
    #     },
    #     "body_font_size": 12.7
    # },
]
