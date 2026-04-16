# Arcs Leader and Lore Generator

A Python project to generate custom leader cards and lore cards for Arcs. It uses the **Pillow** library to manipulate images and create customizable cards.

Website: https://arcs-card-generator.streamlit.app/

## Requirements

* Python 3.x
* Pillow: Install via `pip install Pillow`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Arcs-Leader-Generator.git
   ```


   ```bash
   pip install Pillow
   ```

Also ensure PyYAML is installed so the generators can load YAML data files:

```bash
pip install pyyaml
```

## Usage

### Generate Leader Cards

Run the following script to generate cards for all leaders defined in `leadersFormatted.py`:

```bash
python scripts/batchLeaderCards.py
```

**Leader Card Numbering**

Leader cards can optionally show a small white number near the top-right of the card (using the same font as the leader title).

- The number is based on the leader's position (order) in `scripts/leadersFormatted.py`.
- You can start from a higher number with `--number-start`.
- You can disable numbers entirely with `--no-numbers`.

Examples:

```bash
# Default numbering (starts at 1)
python scripts/batchLeaderCards.py

# Start numbering at 11
python scripts/batchLeaderCards.py --number-start 11

# Disable numbering
python scripts/batchLeaderCards.py --no-numbers

# Generate a single leader, but keep numbering based on file order
python scripts/batchLeaderCards.py --number-start 50 Kaiju

# Generate only the bottom N leaders in the file
python scripts/batchLeaderCards.py --last 10
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

    Generate all leaders at 2×:

    ```bash
    python scripts/batchLeaderCards.py --render-scale 2
    ```

    Generate just one leader at 2× and allow art upscaling:

    ```bash
    python scripts/batchLeaderCards.py --render-scale 2 --allow-upscale Kaiju
    ```

    Generate lore cards at 3×:

    ```bash
    python scripts/batchLoreCards.py --render-scale 3
    ```

    2 = noticeably sharper text when zoomed, file sizes still reasonable.

    3 = very crisp when zoomed, but slower + bigger PNGs (good if you’re printing or doing close inspection).

    4 = only worth it if you really need maximum sharpness; file sizes get huge.


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
python scripts/batchLoreCards.py

# Generate only the bottom N lore cards in the file
python scripts/batchLoreCards.py --last 10
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

### Generate Guild Cards

Run the following script to generate guild cards defined in `scripts/guildCardsFormatted.py`:

```bash
python scripts/batchGuildCards.py

# Generate only the bottom N guild cards in the file
python scripts/batchGuildCards.py --last 10
```

You can optionally generate only specific cards by name:

```bash
python scripts/batchGuildCards.py testguild
```

Guild card artwork is loaded from `cardAssets/guildImages/<name>.png`.

Artifact-style guild cards: you can create "artifact" guild cards that overlay
`cardAssets/Artifact_top_half.png` on top of a normal guild card. To enable this,
set the card's `resource` to `"artifact"` or add `"artifact_top": True` to the
card entry in `scripts/guildCardsFormatted.py`.

### Generate Vox Cards

Run the following script to generate Vox cards defined in `scripts/voxCardsFormatted.py`:

```bash
python scripts/batchVoxCards.py

# Generate only the bottom N Vox cards in the file
python scripts/batchVoxCards.py --last 10
```

Or generate a single card by name:

```bash
python scripts/batchVoxCards.py testvox
```

Vox card artwork is loaded from `cardAssets/voxImages/<name>.png`.

**Vox Frame + Bar Overlay**

Vox cards currently use these top-level assets:

- `cardAssets/CardAsset-Texture-Frame.png` as the Vox frame/texture.
- `cardAssets/Voxbar.png` as an overlay layer pasted on top of the frame/art (but below text).

**Vox Text Placement Tweaks**

You can adjust Vox text placement per-card in `scripts/voxCardsFormatted.py`:

- `text_top_y` (default is controlled in `scripts/batchVoxCards.py`): smaller = title/body block starts higher.
- `body_top_padding`: spacing between the title and the body (smaller = body starts closer to the title).

### Load card definitions from a custom module or file

Each generator supports loading card definitions from an alternate Python module or `.py` file. This makes it easy to keep multiple decks or experiment without editing the default formatted files.

- Use `--source-module` to reference an importable module (dot path), or `--source-file` to point to a `.py` file path.
- The module/file must expose the same symbol name each generator expects:
    - `batchGuildCards.py` expects `guild_cards`
    - `batchVoxCards.py` expects `vox_cards`
    - `batchLoreCards.py` expects `lore_cards`
    - `batchLeaderCards.py` expects `leaders`

Examples:

```bash
# From an importable module (module must be on PYTHONPATH or relative package path):
python scripts/batchGuildCards.py --source-module scripts.guild_deck_formatted

# From a direct file path:
python scripts/batchVoxCards.py --source-file scripts/guild_deck_formatted.py

# Lore from a custom file and render at 3x:
python scripts/batchLoreCards.py --source-file scripts/my_lore_set.py --render-scale 3

# Leaders from a custom module, generate only a named leader:
python scripts/batchLeaderCards.py --source-module scripts.custom_leaders MyLeaderName
```

Notes:

- If the provided module/file doesn't define the expected variable (for example `guild_cards`), the generator will exit with an error.
- These flags let you keep multiple formatted decks in `scripts/` (or elsewhere) and render any of them without editing the default formatted files.

### Run All Card Generators (One Command)

Run all generators (Guild → Leader → Lore → Vox):

```bash
python scripts/batchAllCards.py

# Generate only the bottom N cards of each type
python scripts/batchAllCards.py --last 10
```

Exclude some types by listing them after the command:

```bash
# Skip Vox
python scripts/batchAllCards.py vox

# Skip Vox + Lore
python scripts/batchAllCards.py vox lore
```

### Footer Right Numbering Alignment (Guild / Lore / Vox)

The bottom-right footer text (`footer_right`) is centered for multi-character values (e.g. `"10"`, `"11"`) so it doesn't drift based on digit widths.
This behavior is implemented in the three batch scripts:

- `scripts/batchGuildCards.py`
- `scripts/batchLoreCards.py`
- `scripts/batchVoxCards.py`

### Text Formatting

For both leader and lore cards, you can format text by surrounding words with asterisks (each word individually):

* `*italic*` → *italic*
* `**bold**` → **bold**
* `***both***` → ***bold italic***

Explicit vertical space

- Insert a standalone token `{vspace:N}\n` on its own line inside a card `body` to add N pixels of vertical space (scaled by the card's `render_scale`). Example: `{vspace:6}\n` adds `_s(6)` pixels of extra vertical gap. The token must occupy the line by itself (leading spaces allowed). This is useful for fine-tuning text layout when a manual break is needed.


### Inline Icons

You can embed icons directly into card text (leader `abilities`, and guild/lore/vox `body`) using an inline token:

- **Syntax:** `{icon:NAME}`
- Treat the icon token like a single “word” (separate it with spaces like normal text).
- Trailing punctuation is supported (e.g. `{icon:dice_key_white},` or `{icon:resource_fuel}.`).

**Where icons come from**

Icons are loaded from the `icon and punchboard/` folder.

When you write `{icon:NAME}`, the generator will try to find an image file matching one of these patterns:

- `icon and punchboard/arcs dev_icon NAME.png`
- `icon and punchboard/NAME.png`

Notes:

- If `NAME` contains underscores, they are treated as spaces when resolving filenames (because the token has no spaces).
- You can also include the `.png` in the token (e.g. `{icon:resource_fuel.png}`).
- If an icon is missing, the generator prints a warning and draws a placeholder box.

**Examples**

```text
Start with an icon: {icon:resource_fuel} then words.
In the middle {icon:dice_hit_white} of a sentence.
Punctuation after icon {icon:dice_key_black}, then more.
```

**Available icon tokens**

These are the built-in icon names currently available (from `icon and punchboard/arcs dev_icon *.png`). Use them like `{icon:<name>}`:

```text
{icon:crisis}
{icon:crisis_arrow}
{icon:crisis_hex}
{icon:crisis_moon}
{icon:dice_building_hit_black}
{icon:dice_building_hit_white}
{icon:dice_hit_black}
{icon:dice_hit_white}
{icon:dice_intercept_black}
{icon:dice_intercept_white}
{icon:dice_key_black}
{icon:dice_key_white}
{icon:dice_self_hit_black}
{icon:dice_self_hit_white}
{icon:edict}
{icon:edict_arrow}
{icon:edict_hex}
{icon:edict_moon}
{icon:grand_ambition}
{icon:id_arrow}
{icon:id_hex}
{icon:id_moon}
{icon:objective}
{icon:players}
{icon:resource_material}
{icon:resource_fuel}
{icon:resource_weapon}
{icon:resource_relic}
{icon:resource_psionic}

## YAML data workflow (recommended)

The project now prefers YAML data files over the old formatted Python modules. This makes it easy to edit card data (and add inline comments) from the web UI or your editor.

- Primary data files: `scripts/data/*.yml` (guilds.yml, lore.yml, vox.yml, leaders.yml, btr.yml, edifice.yml).
- Web UI behavior: `app.py` always uses YAML for editing/generation and will never fall back to `.py` templates. When editing in the UI the app creates a per-template single-entry file named `<stem>_single.yml` (for example `leaders_single.yml`) so the editor only shows one entry to modify.
- Legacy templates: the original formatted Python files were moved to `scripts/legacy/`. These are only used as a fallback when no YAML file exists (CLI/back-compat).
- Temporary data handoff: when you click Run in the web UI the app writes edited YAML into a private temporary folder and sets `ADK_DATA_DIR` for the generator subprocess. The app does not show internal temp paths to users.
- Error behavior: if a YAML file exists in `ADK_DATA_DIR` and the generator fails to parse it (syntax error or empty result), the generator exits with a clear error and the app displays the concise error plus full output, there is no silent fallback to `.py`.

Converter and tools

- Convert legacy `.py` templates to YAML:

```bash
python scripts/py_to_yaml_converter.py
```

- Verify YAML files:

```bash
python scripts/verify_yaml.py
```

Quick test (end-to-end)

1. Start the web UI:

```bash
streamlit run app.py
```

2. Select a card type (e.g. Leader), edit the YAML entry in the editor and click **Run**.
3. If you introduce a YAML syntax error, the generator will fail and the UI will show a clear error message and the full script output (no fallback to `.py`).

Notes and next steps

- If you want comment-preserving round-trips when the app rewrites YAML, consider switching to `ruamel.yaml` (optional).
- Update `requirements.txt` to include `pyyaml` (done). If you prefer `ruamel.yaml` replace the YAML usage accordingly.
- The `scripts/legacy/` folder keeps the old formatted templates for manual editing or CLI use; prefer YAML for day-to-day edits.
{icon:summit}
```

## Project Structure

```
├── cardAssets/
│   ├── guildImages/      # Guild card artwork
│   ├── leaderImages/     # Leader card artwork
│   ├── loreImages/       # Lore card artwork
│   ├── voxImages/        # Vox card artwork
│   ├── CardAsset-Texture-Frame.png
│   └── Voxbar.png
├── fonts/                # Font files
├── results/
│   ├── guild/            # Generated guild cards
│   ├── lore/             # Generated lore cards
│   └── vox/              # Generated vox cards
├── scripts/
│   ├── batchAllCards.py       # Run all generators (optionally excluding some)
│   ├── batchGuildCards.py     # Generate guild cards
│   ├── batchLeaderCards.py    # Generate leader cards
│   ├── batchLoreCards.py      # Generate lore cards
│   ├── batchVoxCards.py       # Generate vox cards
│   ├── guildCardsFormatted.py # Guild card data
│   ├── leadersFormatted.py    # Leader card data
│   ├── loreCardsFormatted.py  # Lore card data
│   └── voxCardsFormatted.py   # Vox card data
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
