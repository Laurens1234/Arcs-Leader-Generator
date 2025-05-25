# Arcs-Leader-Generator

A Python project to instantly generate leader cards for Arcs. It uses the **Pillow** library to manipulate images and create customizable leader cards.

## Requirements

* Python 3.x
* Pillow: Install via `pip install Pillow`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/arcs-development-kit.git
   ```

2. Install dependencies:

   ```bash
   pip install Pillow
   ```

## Usage

### Generate a Card for All Leaders:

Run the following script to generate cards for all leaders defined in `leadersFormatted.py`:

```bash
python scripts/batchImages.py
```

Add the leaders you have made to leadersFormatted.py in this format:

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
    }
},
```

If you need to change the font size you can change the last lines of the leader to this:

```python
"C": {"ships": 2, "building": "None", "damaged": False}
},
"body_font_size": 16
```

I recommend you use ChatGPT or another AI tool to quickly reformat your leader data into this format.

If you want to change the body font on your card you can surround words with \* to do so (you have to surround each word individually):

* \**italic\*
* \*\***bold**\*\*
* \*\*\****both***\*\*\*

Cards will be saved in the `results/` folder.

### Example Card:

![Demo Card](https://github.com/Laurens1234/Arcs-Leader-Generator/blob/main/results/Shapeshifter_Card.png)
