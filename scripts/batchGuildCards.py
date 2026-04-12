import argparse
import importlib
import importlib.util
import os
import sys

from PIL import Image, ImageDraw, ImageFont

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

from scripts.guildCardsFormatted import guild_cards

_DEFAULT_OUTPUT_DPI = (300, 300)


def _clamp_int(value, minimum, maximum, default):
    try:
        value = int(value)
    except Exception:
        return default
    return max(minimum, min(maximum, value))


def _select_cards(all_cards, requested_names):
    if not requested_names:
        return list(all_cards), []

    by_lower_name = {c.get("name", "").casefold(): c for c in all_cards}
    selected = []
    missing = []
    for raw in requested_names:
        key = raw.casefold()
        card = by_lower_name.get(key)
        if card is None:
            missing.append(raw)
            continue
        selected.append(card)

    return selected, missing


def _normalize_resource(value: str) -> str:
    if value is None:
        return "fuel"
    key = str(value).strip().casefold()
    aliases = {
        "mat": "material",
        "materials": "material",
        "wep": "weapon",
        "psi": "psionic",
    }
    return aliases.get(key, key)


def _guild_frame_filename(resource: str) -> str:
    resource = _normalize_resource(resource)
    mapping = {
        "fuel": "CardAsset-Frame-Guild-Fuel.png",
        "material": "CardAsset-Frame-Guild-Material.png",
        "weapon": "CardAsset-Frame-Guild-Weapon.png",
        "relic": "CardAsset-Frame-Guild-Relic.png",
        "psionic": "CardAsset-Frame-Guild-Psionic.png",
    }
    if resource not in mapping:
        raise ValueError(
            f"Unknown guild resource '{resource}'. Expected one of: material, fuel, weapon, relic, psionic."
        )
    return mapping[resource]


def _raid_icon_filename(raid_value) -> str:
    if raid_value is None:
        raid_value = 2

    if isinstance(raid_value, str):
        raid_value = raid_value.strip()

    if str(raid_value).casefold() == "x":
        return "CardAsset-Icon-Raid-Cost-X.png"

    try:
        raid_int = int(raid_value)
    except Exception:
        raid_int = 2

    if raid_int == 1:
        return "CardAsset-Icon-Raid-Cost-1.png"
    if raid_int == 2:
        return "CardAsset-Icon-Raid-Cost-2.png"
    if raid_int == 3:
        return "CardAsset-Icon-Raid-Cost-3.png"

    # Fallback: treat anything else as X
    return "CardAsset-Icon-Raid-Cost-X.png"


def create_guild_card(input_data):
    base_path = os.path.dirname(os.path.dirname(__file__))

    custom_font_path = os.path.join(base_path, "fonts", "FMBolyarPro-900.ttf")
    neue_kabel_font_path = os.path.join(base_path, "fonts", "neue-kabel.otf")
    neue_kabel_bold_path = os.path.join(base_path, "fonts", "NeueKabel-Bold.otf")
    neue_kabel_italic_path = os.path.join(base_path, "fonts", "NeueKabel-Italic.otf")
    neue_kabel_bolditalic_path = os.path.join(base_path, "fonts", "NeueKabel-BoldItalic.otf")

    result_path = os.path.join(base_path, "results", "guild")
    guild_image_folder = os.path.join(base_path, "cardAssets", "guildImages")
    footer_image_path = os.path.join(base_path, "cardAssets", "CardAsset-Footer-Paper.png")

    resource = input_data.get("resource", "fuel")
    guild_frame_path = os.path.join(base_path, "cardAssets", _guild_frame_filename(resource))

    raid_icon_path = os.path.join(base_path, "cardAssets", _raid_icon_filename(input_data.get("raid")))

    output_image_path = os.path.join(result_path, f"{input_data['name']}_Guild_Card.png")

    render_scale = _clamp_int(input_data.get("render_scale", 2), 1, 4, 2)
    allow_upscale = bool(input_data.get("allow_upscale", True))

    def _s(value):
        if isinstance(value, tuple):
            return tuple(int(v * render_scale) for v in value)
        return int(value * render_scale)

    guild_frame = Image.open(guild_frame_path).convert("RGBA")
    raid_overlay = Image.open(raid_icon_path).convert("RGBA")

    if render_scale != 1:
        guild_frame = guild_frame.resize(_s(guild_frame.size), Image.Resampling.LANCZOS)
        raid_overlay = raid_overlay.resize(_s(raid_overlay.size), Image.Resampling.LANCZOS)

    card_width, card_height = guild_frame.size

    base_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 255))

    # Artwork (same behavior as lore)
    guild_art_path = os.path.join(guild_image_folder, f"{input_data['name']}.png")
    try:
        art_img = Image.open(guild_art_path).convert("RGBA")

        target_width = card_width
        aspect_ratio = art_img.height / art_img.width
        target_height = int(target_width * aspect_ratio)

        zoom = input_data.get("zoom", 1.0)
        try:
            zoom = float(zoom)
        except Exception:
            zoom = 1.0
        target_width = max(1, int(target_width * zoom))
        target_height = max(1, int(target_height * zoom))

        if not allow_upscale:
            max_w = art_img.width * render_scale
            max_h = art_img.height * render_scale
            if target_width > max_w or target_height > max_h:
                target_width = min(target_width, max_w)
                target_height = int(target_width * aspect_ratio)
                print(
                    f"Note: '{input_data['name']}' guild art is smaller than the frame width; "
                    f"not upscaling to avoid blur. Set allow_upscale=True to keep it full-size."
                )

        art_img = art_img.resize((target_width, target_height), Image.Resampling.LANCZOS)

        image_bottom_y = int(card_height * 0.545)
        shift = input_data.get("boundary_shift", 0.0)
        try:
            shift = float(shift)
        except Exception:
            shift = 0.0
        overlay_bottom_y = int(image_bottom_y * (1 + shift))
        overlay_bottom_y = max(1, min(card_height - 1, overlay_bottom_y))

        art_x = (card_width - art_img.width) // 2
        art_y = overlay_bottom_y - art_img.height
        base_img.paste(art_img, (art_x, art_y), art_img)

    except FileNotFoundError:
        print(
            f"Warning: Guild image '{input_data['name']}.png' not found in guildImages folder. Proceeding without image."
        )

    # Frame overlay
    base_img.paste(guild_frame, (0, 0), guild_frame)

    draw = ImageDraw.Draw(base_img)

    # Fonts
    try:
        title_font_size = input_data.get("title_font_size", 25)
        footer_font_size = input_data.get("footer_font_size", 14)
        body_font_size = input_data.get("body_font_size", 18)

        title_font = ImageFont.truetype(custom_font_path, _s(title_font_size))
        footer_font = ImageFont.truetype(custom_font_path, _s(footer_font_size))
        body_font = ImageFont.truetype(neue_kabel_font_path, _s(body_font_size))
        italic_font = ImageFont.truetype(neue_kabel_italic_path, _s(body_font_size))
        bold_font = ImageFont.truetype(neue_kabel_bold_path, _s(body_font_size))
        bolditalic_font = ImageFont.truetype(neue_kabel_bolditalic_path, _s(body_font_size))
    except IOError as e:
        print(f"Font loading error: {e}")
        title_font = body_font = italic_font = bold_font = bolditalic_font = footer_font = ImageFont.load_default()
        body_font_size = input_data.get("body_font_size", 18)

    # Text box (same coordinates as lore)
    text_margin = _s(40)
    text_x0 = text_margin
    text_x1 = card_width - text_margin
    text_width = text_x1 - text_x0

    text_y0 = int(card_height * 0.552)

    title_text = input_data.get("title", input_data["name"])
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = text_x0 + (text_width - (title_bbox[2] - title_bbox[0])) // 2
    title_y = text_y0
    draw.text((title_x, title_y), title_text, fill="black", font=title_font)

    line_y = title_y + (title_bbox[3] - title_bbox[1]) + _s(12)

    icon_assets_dir = os.path.join(base_path, "icon and punchboard")
    _icon_cache = {}
    _missing_icon_warned = set()

    _TRAILING_PUNCT = set(",.;:!?)]}\"'”’»")

    def _split_trailing_punct(token: str) -> tuple[str, str]:
        trailing = ""
        while token and token[-1] in _TRAILING_PUNCT:
            if token[-1] == "}" and token.casefold().startswith("{icon:"):
                break
            trailing = token[-1] + trailing
            token = token[:-1]
        return token, trailing

    def _try_parse_icon_spec(core: str):
        prefix = "{icon:"
        if core.casefold().startswith(prefix) and core.endswith("}"):
            spec = core[len(prefix) : -1].strip()
            return spec or None
        return None

    def _resolve_icon_path(icon_spec: str):
        raw = (icon_spec or "").strip()
        if not raw:
            return None

        # Icon tokens are single "words" in formatted text, so spaces are represented as underscores.
        normalized = raw.replace("_", " ")

        candidates = []
        if normalized.casefold().endswith(".png"):
            candidates.append(normalized)
        else:
            candidates.append(f"arcs dev_icon {normalized}.png")
            candidates.append(f"{normalized}.png")

        for filename in candidates:
            path = os.path.join(icon_assets_dir, filename)
            if os.path.exists(path):
                return path
        return None

    def _load_icon(icon_spec: str, target_height_px: int):
        key = (icon_spec, int(target_height_px))
        if key in _icon_cache:
            return _icon_cache[key]

        path = _resolve_icon_path(icon_spec)
        if path is None:
            _icon_cache[key] = None
            if icon_spec not in _missing_icon_warned:
                _missing_icon_warned.add(icon_spec)
                print(f"Warning: Missing icon for token '{{icon:{icon_spec}}}'. Looked in: {icon_assets_dir}")
            return None

        try:
            icon_img = Image.open(path).convert("RGBA")
        except Exception as e:
            _icon_cache[key] = None
            if icon_spec not in _missing_icon_warned:
                _missing_icon_warned.add(icon_spec)
                print(f"Warning: Failed to load icon '{path}': {e}")
            return None

        # Trim transparent padding so icons with extra margins don't render smaller than others.
        try:
            alpha = icon_img.getchannel("A")
            bbox = alpha.getbbox()
            if bbox is not None:
                icon_img = icon_img.crop(bbox)
        except Exception:
            pass

        if target_height_px <= 0:
            _icon_cache[key] = None
            return None

        w, h = icon_img.size
        if h <= 0:
            _icon_cache[key] = None
            return None

        target_width_px = max(1, int(round(target_height_px * (w / h))))
        icon_img = icon_img.resize((target_width_px, int(target_height_px)), Image.Resampling.LANCZOS)
        _icon_cache[key] = icon_img
        return icon_img

    def _parse_rich_token(token: str, font, italic_font, bold_font, bolditalic_font):
        core, trailing = _split_trailing_punct(token)

        icon_spec = _try_parse_icon_spec(core)
        if icon_spec is not None:
            return "icon", icon_spec, trailing, font

        font_to_use = font
        text_to_draw = core

        if core.startswith("***") and core.endswith("***") and len(core) > 6:
            text_to_draw = core[3:-3]
            font_to_use = bolditalic_font
        elif core.startswith("**") and core.endswith("**") and len(core) > 4:
            text_to_draw = core[2:-2]
            font_to_use = bold_font
        elif core.startswith("*") and core.endswith("*") and len(core) > 2:
            text_to_draw = core[1:-1]
            font_to_use = italic_font

        return "text", text_to_draw, trailing, font_to_use

    def _icon_layout_for_font(font) -> tuple[int, int]:
        """Return (y_offset_px, height_px) for an inline icon to match letter extents."""
        try:
            bbox = draw.textbbox((0, 0), "H", font=font)
            if (bbox[3] - bbox[1]) <= 0:
                bbox = draw.textbbox((0, 0), "x", font=font)
            y_offset = int(round(bbox[1]))
            height = int(round(bbox[3] - bbox[1]))
            if height <= 0:
                raise ValueError("Invalid glyph bbox height")
            return y_offset, height
        except Exception:
            try:
                ascent, descent = font.getmetrics()
                height = int(ascent + descent)
                return 0, height if height > 0 else _s(body_font_size)
            except Exception:
                return 0, _s(body_font_size)

    _KEY_ICON_SCALE = 0.75

    def _icon_scale_for_spec(icon_spec: str) -> float:
        spec = (icon_spec or "").casefold()
        if "dice_key" in spec:
            return _KEY_ICON_SCALE
        return 1.0

    def _icon_target_height(icon_spec: str, base_height_px: int) -> int:
        scale = _icon_scale_for_spec(icon_spec)
        return max(1, int(round(base_height_px * scale)))

    def _measure_rich_token(token: str, font, italic_font, bold_font, bolditalic_font) -> int:
        kind, payload, trailing, font_to_use = _parse_rich_token(token, font, italic_font, bold_font, bolditalic_font)
        if kind == "icon":
            _, base_icon_height = _icon_layout_for_font(font)
            icon_height = _icon_target_height(payload, base_icon_height)
            icon_img = _load_icon(payload, icon_height)
            main_width = icon_img.width if icon_img is not None else int(icon_height)
        else:
            main_bbox = draw.textbbox((0, 0), payload, font=font_to_use)
            main_width = main_bbox[2] - main_bbox[0]
        if trailing:
            trailing_bbox = draw.textbbox((0, 0), trailing, font=font)
            main_width += trailing_bbox[2] - trailing_bbox[0]
        return main_width

    def wrap_text(text, font, italic_font, bold_font, bolditalic_font, max_width):
        paragraphs = text.split("\n")
        wrapped_lines = []
        for para in paragraphs:
            if not para.strip():
                wrapped_lines.append("")
                continue
            words = para.strip().split()
            current_line_words = []
            current_line_width = 0

            for idx, word in enumerate(words):
                word_width = _measure_rich_token(word, font, italic_font, bold_font, bolditalic_font)
                space_width = draw.textbbox((0, 0), " ", font=font)[2]
                additional_width = word_width if idx == 0 else word_width + space_width

                if current_line_width + additional_width <= max_width:
                    current_line_words.append(word)
                    current_line_width += additional_width
                else:
                    wrapped_lines.append(" ".join(current_line_words))
                    current_line_words = [word]
                    current_line_width = word_width

            if current_line_words:
                wrapped_lines.append(" ".join(current_line_words))

        return wrapped_lines

    def draw_rich_text(draw, text, font, italic_font, bold_font, bolditalic_font, x, y, max_width, line_height):
        line_height = line_height * (body_font_size / 18)
        words = text.split(" ")
        current_x = x
        current_y = y

        try:
            base_ascent = font.getmetrics()[0]
        except Exception:
            base_ascent = None

        def _baseline_adjust(font_to_use):
            if base_ascent is None:
                return 0
            try:
                ascent = font_to_use.getmetrics()[0]
            except Exception:
                return 0
            return base_ascent - ascent

        for word in words:
            kind, payload, trailing, font_to_use = _parse_rich_token(word, font, italic_font, bold_font, bolditalic_font)
            if kind == "icon":
                icon_y_offset, base_icon_height = _icon_layout_for_font(font)
                icon_height = _icon_target_height(payload, base_icon_height)
                icon_img = _load_icon(payload, icon_height)
                icon_width = icon_img.width if icon_img is not None else int(icon_height)

                # Bottom-align to the line's baseline box even when scaled.
                icon_y = current_y + icon_y_offset + (base_icon_height - icon_height)

                if icon_img is not None:
                    base_img.paste(icon_img, (int(current_x), int(icon_y)), icon_img)
                else:
                    draw.rectangle(
                        (int(current_x), int(icon_y), int(current_x + icon_width), int(icon_y + icon_height)),
                        outline="black",
                        width=max(1, _s(1)),
                    )

                current_x += icon_width
            else:
                adjust_y = _baseline_adjust(font_to_use)

                word_bbox = draw.textbbox((0, 0), payload, font=font_to_use)
                word_width = word_bbox[2] - word_bbox[0]
                draw.text((current_x, current_y + adjust_y), payload, font=font_to_use, fill="black")
                current_x += word_width

            if trailing:
                trailing_bbox = draw.textbbox((0, 0), trailing, font=font)
                trailing_width = trailing_bbox[2] - trailing_bbox[0]
                draw.text((current_x, current_y), trailing, font=font, fill="black")
                current_x += trailing_width

            space_width = draw.textbbox((0, 0), " ", font=font)[2]
            current_x += space_width

        return current_y + line_height

    body_text = input_data.get("body", "")
    current_y = line_y + _s(18)
    for line in wrap_text(body_text, body_font, italic_font, bold_font, bolditalic_font, text_width):
        # Support explicit vertical-space token in the body: "{vspace:N}"
        # Example: "{vspace:6}" adds _s(6) pixels of vertical space. The token
        # must occupy the line by itself (leading spaces allowed).
        stripped = line.strip()
        if stripped.startswith("{vspace:") and stripped.endswith("}"):
            try:
                inner = stripped[len("{vspace:"):-1].strip()
                n = int(inner)
                current_y += _s(n)
                continue
            except Exception:
                pass
        if not stripped:
            current_y += _s(10)
            continue
        current_y = draw_rich_text(
            draw,
            line,
            body_font,
            italic_font,
            bold_font,
            bolditalic_font,
            text_x0,
            current_y,
            text_width,
            _s(22),
        )

    # Footer paper overlay and footer text
    try:
        footer_img = Image.open(footer_image_path).convert("RGBA")
        if render_scale != 1:
            footer_img = footer_img.resize(_s(footer_img.size), Image.Resampling.LANCZOS)
        footer_x = (card_width - footer_img.width) // 2
        footer_y = card_height - footer_img.height
        base_img.paste(footer_img, (footer_x, footer_y), footer_img)
        draw = ImageDraw.Draw(base_img)
    except FileNotFoundError:
        print("Warning: Footer image not found. Proceeding without footer image.")

    footer_left = input_data.get("footer_left", "")
    footer_center = input_data.get("footer", "")
    footer_right = input_data.get("footer_right", "")

    footer_y = card_height - _s(45)
    footer_margin = _s(45)

    def _text_width(text: str) -> int:
        bbox = draw.textbbox((0, 0), text, font=footer_font)
        return bbox[2] - bbox[0]

    def _x_centered_like_one_char_left(text: str) -> int:
        placeholder = (text or "G")[0]
        single_w = _text_width(placeholder)
        target_center = footer_margin + single_w / 2
        return int(round(target_center - _text_width(text) / 2))

    def _x_centered_like_one_char_right(text: str) -> int:
        placeholder = "0"
        single_w = _text_width(placeholder)
        right_edge = card_width - footer_margin + _s(2)
        target_center = right_edge - single_w / 2
        return int(round(target_center - _text_width(text) / 2))

    if footer_left:
        footer_left_str = str(footer_left)
        x = footer_margin if len(footer_left_str) <= 1 else _x_centered_like_one_char_left(footer_left_str)
        draw.text((x, footer_y), footer_left_str, fill="black", font=footer_font)

    if footer_center:
        footer_center_str = str(footer_center)
        bbox = draw.textbbox((0, 0), footer_center_str, font=footer_font)
        footer_width = bbox[2] - bbox[0]
        footer_x = (card_width - footer_width) // 2
        draw.text((footer_x, footer_y), footer_center_str, fill="white", font=footer_font)

    if footer_right:
        footer_right_str = str(footer_right)
        if len(footer_right_str) <= 1:
            footer_x = card_width - footer_margin - _text_width(footer_right_str) + _s(2)
        else:
            footer_x = _x_centered_like_one_char_right(footer_right_str)
        draw.text((footer_x, footer_y), footer_right_str, fill="black", font=footer_font)

    # Raid overlay is the very top layer
    base_img.paste(raid_overlay, (0, 0), raid_overlay)

    def final_crop(image, bleed_mm=3, card_width_mm=70, card_height_mm=120):
        width, height = image.size
        left = int((bleed_mm / card_width_mm) * width)
        top = int((bleed_mm / card_height_mm) * height)
        right = width - left
        bottom = height - top
        return image.crop((left, top, right, bottom))

    os.makedirs(result_path, exist_ok=True)

    final_img = final_crop(base_img)

    # Ensure final output matches desired card dimensions.
    # Target logical size is 744x1039 at render_scale=2. Scale proportionally for other render_scale values.
    try:
        target_base_w = 744
        target_base_h = 1039
        target_w = max(1, int(round(target_base_w * (render_scale / 2.0))))
        target_h = max(1, int(round(target_base_h * (render_scale / 2.0))))
        if final_img.size != (target_w, target_h):
            final_img = final_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    except Exception:
        # If anything goes wrong, fall back to saving the cropped image as-is.
        pass

    final_img.save(output_image_path, dpi=_DEFAULT_OUTPUT_DPI)

    print(f"Guild card saved at {output_image_path}")
    print(f"Settings used: render_scale={render_scale}, allow_upscale={allow_upscale}, resource={_normalize_resource(resource)}")

    return output_image_path


def main(argv):
    parser = argparse.ArgumentParser(description="Generate guild cards.")
    parser.add_argument(
        "--render-scale",
        type=int,
        dest="render_scale",
        default=2,
        help="Render the whole card at this scale (1-4).",
    )
    upscale_group = parser.add_mutually_exclusive_group()
    upscale_group.add_argument(
        "--allow-upscale",
        action="store_true",
        dest="allow_upscale",
        help="Allow upscaling low-res artwork (may look blurry). Overrides per-card setting.",
    )
    upscale_group.add_argument(
        "--no-allow-upscale",
        action="store_false",
        dest="allow_upscale",
        help="Disallow upscaling low-res artwork. Overrides per-card setting.",
    )
    parser.set_defaults(allow_upscale=None)

    parser.add_argument(
        "names",
        nargs="*",
        help="Optional guild card names to generate (case-insensitive). If omitted, generates all guild cards.",
    )

    parser.add_argument(
        "--source-module",
        dest="source_module",
        default=None,
        help="Optional Python module path to import guild_cards from (e.g. scripts.guild_deck_formatted).",
    )

    parser.add_argument(
        "--source-file",
        dest="source_file",
        default=None,
        help="Optional path to a .py file to load guild_cards from.",
    )

    parser.add_argument(
        "--last",
        type=int,
        dest="last",
        default=None,
        help="Only generate the last N guild cards from the selected set.",
    )

    parser.add_argument(
        "--number-start",
        type=int,
        dest="number_start",
        default=1,
        help=(
            "Starting number for guild cards. The first card in guildCardsFormatted.py will be this number, "
            "the next card will be +1, etc. This value is written into footer_right (bottom-right) unless already set."
        ),
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        dest="no_numbers",
        help="Do not override footer_right numbering.",
    )

    args = parser.parse_args(argv[1:])

    # Allow loading guild cards from an alternate module or file if requested.
    cards_source = guild_cards
    if args.source_module or args.source_file:
        try:
            if args.source_module:
                mod = importlib.import_module(args.source_module)
            else:
                spec = importlib.util.spec_from_file_location("custom_guild_module", args.source_file)
                if spec is None or spec.loader is None:
                    print(f"Error: cannot load source file: {args.source_file}")
                    return 3
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

            if hasattr(mod, "guild_cards"):
                cards_source = getattr(mod, "guild_cards")
            else:
                print("Error: source does not define 'guild_cards'.")
                return 3
        except Exception as e:
            print(f"Failed to import guild cards from source: {e}")
            return 3

    selected, missing = _select_cards(cards_source, args.names)
    index_by_name = {c.get("name", "").casefold(): idx for idx, c in enumerate(cards_source)}

    if missing:
        print("Warning: unknown guild name(s): " + ", ".join(missing))

    if args.last is not None:
        if args.last <= 0:
            print("Error: --last must be a positive integer")
            return 2
        if len(selected) > args.last:
            selected = selected[-args.last:]

    if not selected:
        print("No guild cards selected. Nothing to do.")
        return 1

    success = 0
    errors = 0

    for card in selected:
        try:
            payload = dict(card)
            payload["render_scale"] = args.render_scale
            if args.allow_upscale is not None:
                payload["allow_upscale"] = args.allow_upscale

            if not args.no_numbers:
                existing_footer_right = payload.get("footer_right")
                has_explicit_footer_right = existing_footer_right is not None and str(existing_footer_right).strip() != ""
                if not has_explicit_footer_right:
                    idx = index_by_name.get(payload.get("name", "").casefold())
                    if idx is not None:
                        payload["footer_right"] = str(args.number_start + idx)

            name = payload.get("name", "<unknown>")
            print(f"Creating guild card for: {name}")
            create_guild_card(payload)
            success += 1
        except Exception as e:
            print(f"Error generating guild card '{card.get('name', 'Unknown')}': {e}")
            errors += 1

    print("\nGuild creation complete.")
    print(f"Guild processed successfully: {success}")
    print(f"Guild with errors: {errors}")
    return 0 if errors == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
