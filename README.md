# Arcs Leader and Lore Generator

A Python project to generate custom leader cards and lore cards for Arcs. It uses the **Pillow** library to manipulate images and create customizable cards.

## Requirements

* Python 3.x
* Pillow: Install via `pip install Pillow`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Arcs-Leader-Generator.git
   ```

2. Install dependencies:

   ```bash
   pip install Pillow
   ```

## Usage

### Generate Leader Cards

Run the following script to generate cards for all leaders defined in `leadersFormatted.py`:

```bash
python scripts/batchLeaderCards.py
```

Add the leaders you have made to `leadersFormatted.py` in this format:

```python
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
    },
    "body_font_size": 16  # Optional: adjust text size (default: 18)
}
```

Leader cards will be saved in the `results/` folder.

### Generate Lore Cards

Run the following script to generate lore cards defined in `loreCardsFormatted.py`:

```bash
python scripts/batchloreCards.py
```

Add lore cards to `loreCardsFormatted.py` in this format:

```python
{
    "name": "Ancient Prophecy",      # Must match image filename in cardAssets/loreImages/ (without .png)
    "title": "Ancient Prophecy",     # Title displayed on the card
    "body": (
        "When you destroy a city, discard this lore and draw 2 Lore cards."
    ),
    "footer_left": "L",              # Left footer text (black)
    "footer": "Lore",                # Center footer text (white)
    "footer_right": "29",            # Right footer text (black)
    "footer_font_size": 16,          # Optional: footer text size (default: 14)
    "body_font_size": 18             # Optional: body text size (default: 18)
}
```

**Adding Lore Images:**
Place your lore card artwork in `cardAssets/loreImages/` with the filename matching the card's `name` field (e.g., `Ancient Prophecy.png`).

Lore cards will be saved in the `results/lore/` folder.

### Text Formatting

For both leader and lore cards, you can format text by surrounding words with asterisks (each word individually):

* `*italic*` → *italic*
* `**bold**` → **bold**
* `***both***` → ***bold italic***

## Project Structure

```
├── cardAssets/
│   ├── loreImages/       # Place lore card artwork here
│   └── leaderImages/     # Leader card assets
├── fonts/                # Font files
├── results/
│   └── lore/             # Generated lore cards
├── scripts/
│   ├── batchImages.py    # Generate all leader cards
│   ├── leadersFormatted.py   # Leader card data
│   ├── loreCards.py      # Generate lore cards
│   └── loreCardsFormatted.py # Lore card data
└── README.md
```

## Tips

I recommend using ChatGPT or another AI tool to quickly reformat your card data into the required format.

Here you can find the most up to date version of my custom leaders: https://docs.google.com/document/d/11SS9AGXG0q3Vlb67Kl0mdvhnE0kKLfgCDgx5LVDwsGk/edit?usp=sharing

### Example Cards:

**Leader Card:**

![Demo Leader Card](https://github.com/Laurens1234/Arcs-Leader-Generator/blob/main/results/Ghost_Card.png)

**Lore Card:**

![Demo Lore Card](https://github.com/Laurens1234/Arcs-Leader-Generator/blob/main/results/lore/Ancient%20Prophecy_Lore_Card.png)
