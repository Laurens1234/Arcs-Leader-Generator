leaders = [
    # Kaiju
    {
        "name": "Kaiju",
        "abilities": (
            "*Devouring.* When you destroy a city, repair all your ships in its cluster.\n"
            "*Feared.* When you  **tax** a city you control, damage it."
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
            "*Mimicry.* When any player declares an ambition, gain a resource of its type. (Weapon for Tyrant and Warlord, you choose Material or Fuel for Tycoon.)\n"
            "*Flickering.* At the end of each chapter, discard all your resources, then gain 1 Material."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
    },
    # Sentient
    {
        "name": "Sentient",
        "abilities": (
            "*Formless.* At the start of each chapter, choose a gate. Until the end of the chapter, you may Catapult and  **build** ships there any number of times per turn. (You do not need any Loyal pieces to build them.)\n"
            "*Shapeless.* In **setup,** scrap all your starports."
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
            "*Zealous.* When you influence a card with a rival agent, you may influence another card with a rival agent.\n"
            "*Rigid.* You cannot influence when you Pivot."
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
            "*Opportunistic.* When you  **battle** and roll any raid dice, you may steal 1 resource for free.\n"
            "*Hunted.* After you destroy a building in  **battle,** the defender may move from adjacent systems into the system you just battled in."
        ),
        "resources": ["Fuel", "Weapon"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # General
    {
        "name": "General",
        "abilities": (
            "*Blitzing.* Prelude: You may spend resources to  **battle.**\n"
            "*Reckless.* In  **battle,** for each intercept you roll, take 1 self hit additionally."
        ),
        "resources": ["Material", "Fuel"],
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
            "*Arising.* After you destroy a piece in  **battle,** you may place a matching fresh loyal piece there..\n"
            "*Gravebound.* In **setup,** damage both of your buildings. You cannot  **build** fresh pieces and place them damaged instead. You cannot repair buildings."
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
            "*Elegant.* When you spend a pip to repair, gain 1 resource.\n"
            "*Obsessed.* You cannot  **build** in clusters where any of your pieces are damaged."
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
            "*Voracious.* When you  **declare** **an** **ambition,** place a ship anywhere on the map.\n"
            "*Crushing.* When more than 1 Rival ship moves into a planet you control, you destroy 1 of those ships.\n"
            "*Erratic.* At the end of each chapter, destroy 1 of your ships."
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
            "*Blessed.* Before scoring, if no ambitions have been declared, you may  **declare** **an** **ambition.**\n"
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
            "*Reflective.* You play as if you have all cards in the court: you have all their icons and can use all their abilities, but you cannot use their prelude actions.\n"
            "*Unstable.* You cannot have more than 1 resource type on your player board."
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
            "*Symbiotic.* You may  **build** in adjacent systems with no rival pieces. (Place pieces damaged if the adjacent system you use to  **build** is Rival controlled.)\n"
            "*Fertile.* Gain 1 Material when you  **build** a starport; gain 1 matching resource when you  **build** a city.\n"
            "*Sprouting.* At the start of each chapter, you may replace one Loyal building with a ship.\n"
            "*Rooted.* You cannot  **battle** in clusters where you have no buildings."
        ),
        "resources": ["Material", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 15
    },
    # Manipulator
    {
        "name": "Manipulator",
        "abilities": (
            "*Clever.* When you  **declare** **an** **ambition,** you may declare an adjacent one.\n"
            "*Fraudulent.* When an ambition has multiple markers, you only score Power for the lowest one."
        ),
        "resources": ["Weapon", "Relic"],
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
            "*Vigilant.* After moving, you may place a ship from anywhere on the map in a gate.\n"
            "*Assertive.* When attacking in  **battle,** deal 1 extra hit.\n"
            "*Cautious.* You cannot roll more Raid and Assault dice combined than you have fresh attacking ships."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
    },
    # Prefect
    {
        "name": "Prefect",
        "abilities": (
            "*Judicious.* In scoring, if any players tie for first in an ambition, you gain the initiative.\n"
            "*Immunized.* If you have the initiative you don't provoke Outrage.\n"
            "*Constrained.* In  **battle,** when you Ransack the Court, you take a normal secure action instead."
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
            "*Manifested.* When you Catapult **move,** your ships may move through one Rival-controlled system. If you move through one, you may influence a card after the move.\n"
            "*Directionless.* You cannot **move** each ship more than once per turn. You cannot end your Catapult **move** in the system you catapulted from."
        ),
        "resources": ["Fuel", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    },
    # Chosen
    {
        "name": "Chosen",
        "abilities": (
            "*Hallowed.* In **setup,** choose a ship you place to be the chosen ship. When anyone destroys it, they place it fresh in any system. Once per turn, after it moves, it may  **battle** by itself. In  **battle,** the die it rolls has the following effects: Skirmish: double damage; Assault: self hit gives 1 key, intercept gives 2 keys; Raid: each key repairs 1 attacking Loyal ship after the battle.\n"
            "*Forsaken.* If you have not attacked with the chosen ship this chapter, you cannot  **secure**  or  **declare** **an** **ambition.**"
        ),
        "resources": ["Relic", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 15
    },
    # Sage
    {
        "name": "Sage",
        "abilities": (
            "*Arcane.* In **setup,** gain 5 extra Lore cards.\n"
            "*Elusive.* Players may influence and  **secure**  your lore. When you  **secure**  your own lore, you may discard it to gain a new one. At the end of each chapter, gain a lore per lore that was taken from you by other players. If the lore deck is empty, reshuffle the lore discard."
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
            "*Cunning.* When you pass the initiative, you may pass it to any player and guess a suit. If they have it, they must play the lowest card of that suit they have, you may surpass with cards of any suit and gain 1 extra pip. (The original suit gets the initiative if you tie.)\n"
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
            "*Versatile.* Your starports can **move,**  **battle** intercept and control like a ship. You place starports outside building slots.\n"
            "*Exorbitant.* You can only  **build** starports at cities, once per city each turn. It costs 2  **build** actions to  **build** a starport.\n"
            "*Fragile.* After you catapult **move,** damage the starport you used. "
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
            "*Illusive.* After you  **tax** a city, you may place it in any building slot you control.\n"
            "*Unmasked.* When you  **tax** a rival city, you only gain a captive or resource, not both."
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
            "*Interwoven.* Before you  **secure**  a card in the court, you may influence an adjacent card.\n"
            "*Tangled.* You must discard a resource to  **secure**  a card with a 2 or more Rival agents."
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
            "*Lucid.* When you  **declare** **an** **ambition,** gain 1 Lore card.\n"
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
            "*Inquisitive.*  When you copy or pivot to  **tax,** gain two resources if it’s a type you haven’t taxed this chapter.\n"
            "*Distracted.* After scoring tycoon keeper or empath, discard a resource matching that ambition."
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
            "*Farsighted.* After you  **secure** , look at the top 3 cards of the Court deck, keep 1 on top, put 1 in the court and bury 1.\n"
            "*Hasty.* After you discard a guild card with it's Prelude action, shuffle it back into the court deck. "
        ),
        "resources": ["Material", "Relic"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
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
            "*Visionary.* You may  **build** using repair actions.\n"
            "*Meticulous.* You cannot  **tax** if any of your pieces are damaged."
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
            "*Venerated.* After a  **battle** where rival damages or destroys one of your cities, secure the top card of the court deck.\n"
            "*Selfless.* When attacking in **battle,** when you destroy a city also damage all your ships in its system."
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
            "*Pyromaniacal.* After a  **battle** where you destroy a building, destroy all damaged pieces in its system if you have any attacking ships left.\n"
            "*Insatiable.* At the end of each chapter, if you did not destroy and buildings this chapter, destroy a loyal city."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
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
            "*Savage.* When you  **battle** in a system with no buildings, collect 1 extra die.\n"
            "*Uncivilized.* When you influence a card with any rival agents, damage one of your pieces."
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
            "*Conductive.* Once per turn, you may spend a resource as a resource non-Outraged resource.\n"
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
            "*Guiding.* Once per round, when a rival tries to influence a card with one of your agents, you may force him to influence another card.\n"
            "*Straining.* To  **secure**  a card with a rival agent on it, you must have 2 more agents on it than them instead of 1."
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
            "*Wasteful.* If you  **secure**  a card using 3 or more agents, discard a resource."
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
            "*Ironclad.* When one of your ships is destroyed, you may discard a resource to repair it instead.\n"
            "*Cold.* At the end of each chapter, destroy all damaged loyal ships."
        ),
        "resources": ["Material", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
    },
    # Solian
    {
        "name": "Solian",
        "abilities": (
            "*Raiding.* You can catapult **move** through planetary systems as if they were gates.\n"
            "*Brutal.* When your ships catapult into an enemy-controlled gate, one of them takes a hit."
        ),
        "resources": ["Weapon", "Fuel"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
    },
    # Bargainer
    {
        "name": "Bargainer",
        "abilities": (
            "*Leverage.* You may return a player’s trophy or captive to  **tax** one of their cities. (You don’t get a captive.)\n"
            "*Obliged.* You must return a trophy or captive when you before first place. If you can’t, you get the second-place points and don’t get the city bonus."
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
            "*Genesis.* At the start of each chapter, place a resource token from the emptiest supply on any planet (if tied you choose). That planet now has this resource type.\n"
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
            "*Misdirecting.* Once per chapter, before you play an action card, you may take a played facedown action card and replace it with one of yours.\n"
            "*Revealed.* When you discard a card to seize, play it faceup."
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
            "*Versatile.* Your starports can **move** **battle** intercept and control like a ship. You place starports outside building slots\n"
            "*Exorbitant.* You can only build starports at cities once per city each turn. It costs 2 build actions to build a starport. \n"
            "*Fragile.* After you catapult **move** damage the starport you used."
        ),
        "resources": ["Material", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "starport"},
            "B": {"ships": 3, "building": "city"},
            "C": {"ships": 2, "building": "None"}
        },
        "body_font_size": 18
    }
    ,
    # Iconoclast
    {
        "name": "Iconoclast",
        "abilities": (
            "*Radical.* When you may discard a card to seize the initiative you may steal a guild card from a player which type matches your or their outrage, if none exist, you may instead move an ambition marker to a different box.\n"
            "*Hoarding.* You only draw 5 cards each chapter. On your final turn of each chapter of playing your final card you may pass to keep it for the next chapter.\n"
            "*Fervent.* In **setup,** provoke outrage of your city's starting types, then gain any amount of any resources."
        ),
        "resources": ["Psionic", "Psionic"],
        "setup": {
            "A": {"ships": 4, "building": "city"},
            "B": {"ships": 4, "building": "city"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 15,
        "zoom": 1.2
    },
    # Fiend
    {
        "name": "Fiend",
        "abilities": (
            "*Gluttonous.* When you provoke outrage, clear it if you already have it outraged; if you do, gain that resource up to your empty slots.\n"
            "*Malevolent.* Prelude: If you have outrage in all types, you may spend a resource to damage a ship in a matching system.\n"
            "*Frenzied.* In **setup,** provoke outrage in all resource types. (Before you gain resources.)"
        ),
        "resources": ["Fuel", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 17,
        "zoom": 1.2
    },
    # Wheeler-dealer
    {
        "name": "Wheeler-dealer",
        "abilities": (
            "*Cunning.* After securing a card, you may outrage its resource type, then secure cards from the top of the deck matching the amount of cards you just discarded.\n"
            "*Irate.* In **setup,** provoke relic outrage."
        ),
        "resources": ["Psionic", "Material"],
        "setup": {
            "A": {"ships": 3, "building": "city"},
            "B": {"ships": 3, "building": "starport"},
            "C": {"ships": 3, "building": "None"}
        },
        "body_font_size": 18,
        "zoom": 1.2
    },
    # Curator
    {
        "name": "Curator",
        "abilities": (
            "*Meticulous.* When you secure a card, you may discard it to secure the top card of the lore deck instead. You must do this if you have more guild cards than lore cards.\n"
            "*Ascetic.* At the end of each chapter scrap a lore card you have."
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
            "*Broken* *Reach.* In **setup,** all players Provoke Material Outrage."
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
            "*Canny.* Before **scoring** **ambitions,** you **secure** all cards where you have the most agents.\n"
            "*Greedy.* In **setup,** place an agent on your Relic Outrage slot."
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
