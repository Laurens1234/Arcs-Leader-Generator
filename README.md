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

**Leader Image Options**
- **zoom**: : A numeric multiplier applied to the leader artwork (e.g., `1.5` for 150%). Zooming enlarges the image and may cause the left/right edges of the card to be cropped, which is expected when zoom > 1.
- **boundary_shift**: : A fractional value that moves the card image boundaries up or down. Positive values move the top and bottom boundaries lower on the card (e.g., `0.25` moves them 25% lower), negative values move them up. This affects how the artwork is fitted and where its bottom aligns relative to the title area.

**Image Quality / Blurry Text When Zooming**

If the exported PNG looks a little blurry when you zoom in, that usually means the image simply doesn’t have enough pixels (the base templates are relatively small). The generator supports rendering the whole card at a higher internal resolution so the text stays crisp when zoomed.

- **render_scale** (recommended): Integer `1`–`4` (default: `2`). Renders the entire card at `render_scale×` resolution (fonts and coordinates scale with it). Higher values look sharper when zoomed, but generate larger output files.
- **allow_upscale**: Boolean (default: `True`). Keeps artwork filling the available space even when the source image is smaller (it will upscale, which can look blurry). Set `allow_upscale=False` to clamp to the source resolution (sharper, but the artwork may appear smaller).
- **Output DPI metadata**: Saved PNGs include ~300 DPI metadata. This doesn’t add pixels by itself, but it helps some print/export tools interpret the image size more predictably.

**Apply to One Card vs All Cards**

- **One card**: Add `render_scale` / `allow_upscale` to that specific leader (in `scripts/leadersFormatted.py`) or lore card (in `scripts/loreCardsFormatted.py`).

    Example (one leader):

    ```python
    {
            "name": "Kaiju",
            "abilities": (...),
            "resources": ["Weapon", "Material"],
            "setup": {...},
            "render_scale": 3,
            "allow_upscale": False,
    }
    ```

- **All cards** (global default): Change the default in the generator scripts.

    Leader cards default is controlled in `scripts/LeaderimageScript.py` via:

    ```python
    render_scale = _clamp_int(input_data.get("render_scale", 2), 1, 4, 2)
    ```

    Lore cards default is controlled in `scripts/batchLoreCards.py` via:

    ```python
    render_scale = _clamp_int(input_data.get("render_scale", 2), 1, 4, 2)
    ```

    To make *everything* render at 3× by default, change the `2` to `3` in those lines.

- **All cards (one-off from the terminal)**: Pass flags to the batch scripts. If you don’t pass a flag, the script uses the existing per-card setting or the built-in default.

    Generate all leaders at 3×:

    ```bash
    python scripts/batchLeaderCards.py --render-scale 3
    ```

    Generate just one leader at 4× and allow art upscaling:

    ```bash
    python scripts/batchLeaderCards.py --render-scale 4 --allow-upscale Kaiju
    ```

    Generate lore cards at 3×:

    ```bash
    python scripts/batchLoreCards.py --render-scale 3
    ```

You can set these per-leader in `scripts/leadersFormatted.py`. Example:

```python
{
    "name": "Prefect",
    "abilities": (...),
    "resources": ["Psionic", "Fuel"],
    "body_font_size": 18,
    "zoom": 1.45,
    "boundary_shift": 0.33,
    "render_scale": 2,      # Optional: 1–4 (higher = sharper when zoomed)
    "allow_upscale": False  # Optional: keep small art from being stretched
}
```
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
    "body_font_size": 18,            # Optional: body text size (default: 18)
    "render_scale": 2,               # Optional: 1–4 (higher = sharper when zoomed)
    "allow_upscale": False           # Optional: keep small lore art from being stretched
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

![Demo Leader Card](https://github.com/Laurens1234/Arcs-Leader-Generator/blob/main/results/Prefect_Card.png)

![Demo Leader Card](https://github.com/Laurens1234/Arcs-Leader-Generator/blob/main/results/Ghost_Card.png)

**Lore Card:**

![Demo Lore Card](https://github.com/Laurens1234/Arcs-Leader-Generator/blob/main/results/lore/Ancient%20Prophecy_Lore_Card.png)
