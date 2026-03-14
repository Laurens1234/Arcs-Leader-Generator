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
        "body_font_size": 18
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
        "zoom": 1.2,
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
            "*Zealous.* Affer you **influence** a card with a rival agent, you may influence a different card with a rival agent.\n"
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
            "*Blitzing.* After you **tax**, you may discard a resource to gain a weapon. You may a discard a weapon to ignore one rolled intercept.\n"
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
    # Necromancer
    {
        "name": "Necromancer",
        "abilities": (
            "*Arising.* After you destroy a piece in **battle**, you may place a matching fresh loyal piece there..\n"
            "*Gravebound.* In **setup**, damage both of your buildings. You cannot **build** fresh pieces and place them damaged instead. You cannot repair buildings."
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
            "*Erratic.* In scoring, destroy 1 loyal fresh ship for each ambition you win."
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
            "*Sacred.* At the end of each chapter, for each ambition a Rival won that chapter, they must give you a resource. If they can’t, they must give you a Guild card.\n"
            "*Blessed.* Before scoring, you may **declare** **an** **ambition**.\n"
            "*Corrupted.* After sacred, discard 1 resource per ambition you won this chapter."
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
            "*Reflective.* Once per turn, you may discard a guild card to secure one in the court with no agents on it.\n"
            "*Unstable.* Discard a guild card for no effect if you have two or more of the same type."
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
        "body_font_size": 18
    },
    # Manipulator
    {
        "name": "Manipulator",
        "abilities": (
            "*Clever.* When you **declare** **an** **ambition**, you may move any agents in the court to other cards.\n"
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
            "*Judicious.* In scoring, if any players tie for first in an ambition, you gain the initiative.\n"
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
            "*Manifested.* When you Catapult **move**, your ships may move through one Rival-controlled system. If you move through one, you may influence a card after the move.\n"
            "*Directionless.* You cannot **move** each ship more than once per turn. You cannot end your Catapult **move** in the system you catapulted from."
        ),
        "resources": ["Fuel", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.25,
        "boundary_shift": 0.2
    },
    # Chosen
    {
        "name": "Chosen",
        "abilities": (
            "*Hallowed.* In **setup**, choose a ship you place to be the chosen ship. When anyone destroys it, they place it fresh in any system. Once per turn, after it **moves**, it may battle by itself. In battle, the die it rolls has its result count twice.\n"
            "*Forsaken.* If you have not attacked with the chosen ship this chapter, you cannot **secure**  or **declare** **an** **ambition**."
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
            "*Elusive.* Players may **influence** and **secure**  your lore. When you **secure** your own lore, gain one lore card."
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
            "*Exorbitant.* You can only **build** starports at cities. It costs 2 **build** actions to **build** a starport.\n"
            "*Fragile.* After you catapult **move**, damage the starport you used. "
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
            "*Illusive.* After you **tax** a city, you may place it in any building slot you control.\n"
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
            "*Tangled.* You must discard a resource to be able to **secure** a card with any Rival agents on it."
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
            "*Inquisitive.*  When you copy or pivot to **tax**, gain an additional resource if it’s a type you haven’t taxed this chapter.\n"
            "*Distracted.* After scoring tycoon, keeper or empath, discard a resource matching that ambition."
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
            "*Baneful.* After you **secure** a card discard it without effect, then look at the top 3 cards of the Court deck, secure 1, put 1 in the court and bury 1.\n"
            "*Scathing.* After you discard a guild card with it's Prelude action, shuffle it back into the court deck. "
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
            "*Transformative.* At the start of each chapter discard 1 resource to gain 2 resources different types other than the one you discarded.\n"
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
            "*Visionary.* You may build using **repair** actions.\n"
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
            "*Venerated.* After a **battle** where rival destroys any of your pieces, gain a matching resource (none if in gate), if they destroyed one of your cities, secure the top card of the court deck instead.\n"
            "*Selfless.* After a **battle**, where you destroy a city, damage all your fresh ships in its system."
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
            "*Pyromaniacal.* After you destroy a city in a system you control, destroy all damaged pieces there.\n"
            "*Insatiable.* At the end of each chapter, if you did not destroy any city this chapter, destroy a loyal city."
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
            "*Frugal.* If you start a turn with no resources or guild cards, gain any resource.\n"
            "*Depleted.* If you start your turn with any resources on your player board, discard 1."
        ),
        "resources": ["Material", "Relic"],
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
            "*Uncivilized.* When you **influence** a card with any rival agents, damage one of your pieces."
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
            "*Conductive.* Once per turn, you may spend a resource as a resource no player has provoked outraged in.\n"
            "*Overloaded.* You cannot have more than 1 resource of each type on your player board."
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
            "*Guiding.* Once per round, when a rival tries to **influence** a card with one of your agents, you may force them to influence another card.\n"
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
            "*Overclocked.* If you spend 2 or more resources this turn, you may influence at the end of your prelude.\n"
            "*Wasteful.* If you **secure**  a card using 3 or more agents, discard a resource."
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
            "*Ironclad.* After a battle where one or more of your ships is destroyed, you may discard a resource to keep all your destroyed ships damaged instead.\n"
            "*Cold.* At the end of each chapter, destroy all damaged loyal ships."
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
            "*Settled.* **Prelude:** You may move freely from planets (no catapult moves).\n"
            "*Rooted.* When your ships catapult move into an enemy-controlled gate, one of them takes a hit."
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
            "*Leverage.* You may return a player’s trophy or captive to **tax** one of their cities.\n"
            "*Obliged.* You must return a trophy or captive when you when you score first place. If you can’t, you get the second-place points and don’t get the city bonus."
        ),
        "resources": ["Relic", "Material"],
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
            "*Genesis.* At the start of each chapter, place a resource token from the fullest supply on any planet (if tied you choose). That planet now has this resource type.\n"
            "*Codependent.* When taxing you only gain resources from terraformed planets."
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
            "*Wayfaring.* When **moving** you may take **any** pieces you control with you. Cities in gates match the resource types of each planet in its cluster. If there is no space on a planet place the building outside the building slots.\n"
            "*Itinerant.* You cannot **Tax** cities in planetary systems.\n"
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    }
    ,
    # Iconoclast
    {
        "name": "Iconoclast",
        "abilities": (
            "*Radical.* When you may discard a card to seize, you may destroy a city you control to steal a guild card from a player which type matches your or their outrage.\n"
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
            "*Gluttonous.* When you provoke outrage, clear it if you already have it outraged; if you do, gain that resource up to your empty slots.\n"
            "*Wrathful.* In **setup**, provoke outrage in all resource types. (Before you gain resources.)"
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
            "*Cunning.* **Prelude:** Once per turn, you may provoke outrage in a resource type, then secure cards from the top of the deck matching the amount of cards you just discarded. Then gain **any** resources matching the amount you've just discarded.\n"
            "*Irate.* In **setup**, provoke relic or psionic outrage."
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
        "zoom": 1,
        
    },
    # GOD'S HAND
    {
        "name": "God's Hand",
        "abilities": (
            "*Faithful* *Reach.* Before dealing action cards, mix in the 6 Faithful Action cards (FL1-6) and take Champion of the Faith title (F7).\n"
            "*An* *Era* *of* *Heresy.* When any player wins Empath, they take Champion of the Faith title."
        ),
        "resources": ["Psionic", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    },
    {
        "name": "Firebrand",
        "abilities": (
            "*Partisan* *Seizing.* Place the Partisan Seizing rules card near the action area. This game, players can seize by provoking outrage if they do not wish to spend a second action card.\n"
            "*Shameless.* Whenever you win **any** ambition, you may discard a resource to remove the matching outrage."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1,
        "boundary_shift": 0.22
    },
    # SCAVENGER
    {
        "name": "Scavenger",
        "abilities": (
            "**Scavenge** **(Tax):** Damage a fresh rival ship in a system you control. Then gain a resource matching that system.\n"
            "*Broken* *Reach.* In **setup**, all players Provoke Material Outrage."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.25,
        "boundary_shift": 0.25
    },
    # DIPLOMAT
    {
        "name": "Diplomat",
        "abilities": (
            "*Canny.* Before **scoring** **ambitions**, you **secure** all cards where you have the most agents.\n"
            "*Greedy.* In **setup**, place an agent on your Relic Outrage slot."
        ),
        "resources": ["Psionic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.3,
        "boundary_shift": 0.33
    },
    # IMPERATOR
    {
        "name": "Imperator",
        "abilities": (
            "*Empire* *Builder.* When you win an ambition score twice as many points from your city bonus.\n"
            "*Sneering.* You do not score second place for any ambition."
        ),
        "resources": ["Material", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.15,
        "boundary_shift": 0.5
    },
    # ANCIENT WRAITH
    {
        "name": "Ancient Wraith",
        "abilities": (
            "*The* *Undying* *Reach.* Place the Twisted Passage rules card in play. Players may move out of the Passage, and no players may harm Rivals there.\n"
            "*Ethereal.* You cannot build shipyards, but your destroyed ships are never taken as trophies and are instead placed on the Twisted Passage."
        ),
        "resources": ["Weapon", "Psionic"],
        "setup": {
            "A": {"ships": 4, "building": "None"},
            "B": {"ships": 3, "building": "None"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18
    }
]
