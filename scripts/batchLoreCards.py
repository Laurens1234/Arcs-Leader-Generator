import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

from scripts.loreCardsFormatted import lore_cards

_DEFAULT_OUTPUT_DPI = (300, 300)


def _clamp_int(value, minimum, maximum, default):
    try:
        value = int(value)
    except Exception:
        return default
    return max(minimum, min(maximum, value))


def _select_lore_cards(all_cards, requested_names):
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


def create_lore_card(input_data):
    """
    Creates a lore card with the following layers (bottom to top):
    1. Base canvas (white/transparent)
    2. Lore image (top half of the card)
    3. Lore frame overlay
    4. Title text, body text, and footer text
    """
    # File paths
    base_path = os.path.dirname(os.path.dirname(__file__))
    
    # Font paths
    custom_font_path = os.path.join(base_path, "fonts", "FMBolyarPro-900.ttf")
    neue_kabel_font_path = os.path.join(base_path, "fonts", "neue-kabel.otf")
    neue_kabel_bold_path = os.path.join(base_path, "fonts", "NeueKabel-Bold.otf")
    neue_kabel_italic_path = os.path.join(base_path, "fonts", "NeueKabel-Italic.otf")
    neue_kabel_bolditalic_path = os.path.join(base_path, "fonts", "NeueKabel-BoldItalic.otf")

    # Asset paths
    result_path = os.path.join(base_path, "results", "lore")
    lore_frame_path = os.path.join(base_path, "cardAssets", "CardAsset-Frame-Lore.png")
    lore_image_folder = os.path.join(base_path, "cardAssets", "loreImages")
    footer_image_path = os.path.join(base_path, "cardAssets", "CardAsset-Footer-Paper.png")
    
    # Output path
    output_image_path = os.path.join(result_path, f"{input_data['name']}_Lore_Card.png")

    # Rendering scale: render the whole card at a higher resolution so text stays sharp when zoomed.
    # Set render_scale=1 to preserve original pixel dimensions.
    render_scale = _clamp_int(input_data.get("render_scale", 2), 1, 4, 2)

    # By default, prefer keeping artwork full-size even if it requires upscaling.
    # Set allow_upscale=False to clamp to source resolution (avoids blur but may look smaller).
    allow_upscale = bool(input_data.get("allow_upscale", True))

    def _s(value):
        if isinstance(value, tuple):
            return tuple(int(v * render_scale) for v in value)
        return int(value * render_scale)

    # Load the lore frame to get card dimensions
    lore_frame = Image.open(lore_frame_path).convert("RGBA")

    if render_scale != 1:
        lore_frame = lore_frame.resize(_s(lore_frame.size), Image.Resampling.LANCZOS)
    card_width, card_height = lore_frame.size

    # Create base canvas
    base_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 255))

    # Load and paste lore image (top half of the card)
    lore_image_path = os.path.join(lore_image_folder, f"{input_data['name']}.png")
    try:
        lore_img = Image.open(lore_image_path).convert("RGBA")

        # Scale lore image to match card width, maintaining aspect ratio
        target_width = card_width
        aspect_ratio = lore_img.height / lore_img.width
        target_height = int(target_width * aspect_ratio)

        # Support optional zoom multiplier (like leaders). Values >1 crop sides/top; <1 letterbox.
        zoom = input_data.get("zoom", 1.0)
        try:
            zoom = float(zoom)
        except Exception:
            zoom = 1.0
        target_width = max(1, int(target_width * zoom))
        target_height = max(1, int(target_height * zoom))

        if not allow_upscale:
            max_w = lore_img.width * render_scale
            max_h = lore_img.height * render_scale
            if target_width > max_w or target_height > max_h:
                target_width = min(target_width, max_w)
                target_height = int(target_width * aspect_ratio)
                print(
                    f"Note: '{input_data['name']}' lore art is smaller than the frame width; "
                    f"not upscaling to avoid blur. Set allow_upscale=True to keep it full-size."
                )

        lore_img = lore_img.resize((target_width, target_height), Image.Resampling.LANCZOS)

        # Positioning: keep artwork bottom aligned to the text boundary by default.
        # Optional `boundary_shift` behaves like leader cards: positive shifts move the boundary down.
        image_bottom_y = int(card_height * 0.545)
        shift = input_data.get("boundary_shift", 0.0)
        try:
            shift = float(shift)
        except Exception:
            shift = 0.0
        overlay_bottom_y = int(image_bottom_y * (1 + shift))
        overlay_bottom_y = max(1, min(card_height - 1, overlay_bottom_y))

        lore_x = (card_width - lore_img.width) // 2
        lore_y = overlay_bottom_y - lore_img.height

        base_img.paste(lore_img, (lore_x, lore_y), lore_img)
        
    except FileNotFoundError:
        print(f"Warning: Lore image '{input_data['name']}.png' not found in loreImages folder. Proceeding without image.")

    # Paste the lore frame on top
    base_img.paste(lore_frame, (0, 0), lore_frame)

    # Create drawing context
    draw = ImageDraw.Draw(base_img)

    # Load fonts
    try:
        title_font_size = input_data.get("title_font_size", 25)
        footer_font_size = input_data.get("footer_font_size", 14)
        body_font_size = input_data.get("body_font_size", 18)

        title_font = ImageFont.truetype(custom_font_path, _s(title_font_size))
        footer_font = ImageFont.truetype(custom_font_path, _s(footer_font_size))
        number_font = ImageFont.truetype(custom_font_path, _s(14))
        body_font = ImageFont.truetype(neue_kabel_font_path, _s(body_font_size))
        italic_font = ImageFont.truetype(neue_kabel_italic_path, _s(body_font_size))
        bold_font = ImageFont.truetype(neue_kabel_bold_path, _s(body_font_size))
        bolditalic_font = ImageFont.truetype(neue_kabel_bolditalic_path, _s(body_font_size))
    except IOError as e:
        print(f"Font loading error: {e}")
        title_font = body_font = italic_font = bold_font = bolditalic_font = footer_font = number_font = ImageFont.load_default()
        body_font_size = input_data.get("body_font_size", 18)

    # Text area dimensions (adjust these based on the lore frame layout)
    text_margin = _s(40)
    text_x0 = text_margin
    text_x1 = card_width - text_margin
    text_width = text_x1 - text_x0
    
    # Title position (below the image area)
    text_y0 = int(card_height * 0.545)  # Start below the top half
    
    # Draw title text (centered)
    title_text = input_data.get('title', input_data['name'])
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = text_x0 + (text_width - (title_bbox[2] - title_bbox[0])) // 2
    title_y = text_y0
    draw.text((title_x, title_y), title_text, fill="black", font=title_font)

    # Calculate line_y for body text positioning (no line drawn)
    line_y = title_y + (title_bbox[3] - title_bbox[1]) + _s(12)

    # Text wrapping function
    _TRAILING_PUNCT = set(",.;:!?)]}\"'”’»")

    def _split_trailing_punct(token: str) -> tuple[str, str]:
        trailing = ""
        while token and token[-1] in _TRAILING_PUNCT:
            trailing = token[-1] + trailing
            token = token[:-1]
        return token, trailing

    def _parse_rich_token(token: str, font, italic_font, bold_font, bolditalic_font):
        core, trailing = _split_trailing_punct(token)

        font_to_use = font
        text_to_draw = core
        adjust_y = 0

        if core.startswith("***") and core.endswith("***") and len(core) > 6:
            text_to_draw = core[3:-3]
            font_to_use = bolditalic_font
            adjust_y = _s(4)
        elif core.startswith("**") and core.endswith("**") and len(core) > 4:
            text_to_draw = core[2:-2]
            font_to_use = bold_font
            adjust_y = _s(4)
        elif core.startswith("*") and core.endswith("*") and len(core) > 2:
            text_to_draw = core[1:-1]
            font_to_use = italic_font
            adjust_y = _s(3)

        return text_to_draw, trailing, font_to_use, adjust_y

    def _measure_rich_token(token: str, font, italic_font, bold_font, bolditalic_font) -> int:
        text_to_draw, trailing, font_to_use, _adjust_y = _parse_rich_token(
            token, font, italic_font, bold_font, bolditalic_font
        )
        main_bbox = draw.textbbox((0, 0), text_to_draw, font=font_to_use)
        main_width = main_bbox[2] - main_bbox[0]
        if trailing:
            trailing_bbox = draw.textbbox((0, 0), trailing, font=font)
            main_width += trailing_bbox[2] - trailing_bbox[0]
        return main_width

    def wrap_text(text, font, italic_font, bold_font, bolditalic_font, max_width):
        paragraphs = text.split('\n')
        wrapped_lines = []
        for para in paragraphs:
            if not para.strip():
                wrapped_lines.append("")  # Preserve empty lines for paragraph breaks
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

    # Rich text rendering function
    def draw_rich_text(draw, text, font, italic_font, bold_font, bolditalic_font, x, y, max_width, line_height):
        line_height = line_height * (body_font_size / 18)
        words = text.split(" ")
        current_x = x
        current_y = y

        for word in words:
            text_to_draw, trailing, font_to_use, adjust_y = _parse_rich_token(
                word, font, italic_font, bold_font, bolditalic_font
            )

            word_bbox = draw.textbbox((0, 0), text_to_draw, font=font_to_use)
            word_width = word_bbox[2] - word_bbox[0]
            draw.text((current_x, current_y + adjust_y), text_to_draw, font=font_to_use, fill="black")
            current_x += word_width

            if trailing:
                trailing_bbox = draw.textbbox((0, 0), trailing, font=font)
                trailing_width = trailing_bbox[2] - trailing_bbox[0]
                # Trailing punctuation is outside the rich marker (e.g. "**tax**,")
                # so it should use the normal font *and* the normal baseline.
                draw.text((current_x, current_y), trailing, font=font, fill="black")
                current_x += trailing_width

            space_width = draw.textbbox((0, 0), " ", font=font)[2]
            current_x += space_width

        return current_y + line_height

    # Draw body text
    body_text = input_data.get('body', '')
    current_y = line_y + _s(18)
    for line in wrap_text(body_text, body_font, italic_font, bold_font, bolditalic_font, text_width):
        if not line.strip():
            current_y += _s(10)
            continue
        current_y = draw_rich_text(draw, line, body_font, italic_font, bold_font, bolditalic_font, text_x0, current_y, text_width, _s(22))

    # Load and paste footer image on top of everything
    try:
        footer_img = Image.open(footer_image_path).convert("RGBA")
        if render_scale != 1:
            footer_img = footer_img.resize(_s(footer_img.size), Image.Resampling.LANCZOS)
        # Position footer at the bottom center
        footer_x = (card_width - footer_img.width) // 2
        footer_y = card_height - footer_img.height
        base_img.paste(footer_img, (footer_x, footer_y), footer_img)
        # Need to recreate draw context after pasting
        draw = ImageDraw.Draw(base_img)
    except FileNotFoundError:
        print(f"Warning: Footer image not found. Proceeding without footer image.")

    # Draw footer text (centered at bottom, on top of footer image)
    footer_left = input_data.get('footer_left', '')
    footer_center = input_data.get('footer', '')  # Keep 'footer' as center for backwards compatibility
    footer_right = input_data.get('footer_right', '')
    
    footer_y = card_height - _s(45)  # Position near bottom
    footer_margin = _s(45)  # Margin from edges
    
    # Draw left footer text (black)
    if footer_left:
        draw.text((footer_margin, footer_y), footer_left, fill="black", font=footer_font)
    
    # Draw center footer text (white)
    if footer_center:
        footer_bbox = draw.textbbox((0, 0), footer_center, font=footer_font)
        footer_width = footer_bbox[2] - footer_bbox[0]
        footer_x = (card_width - footer_width) // 2
        draw.text((footer_x, footer_y), footer_center, fill="white", font=footer_font)
    
    # Draw right footer text (black)
    if footer_right:
        footer_bbox = draw.textbbox((0, 0), footer_right, font=footer_font)
        footer_width = footer_bbox[2] - footer_bbox[0]
        footer_x = card_width - footer_margin - footer_width + _s(5)
        draw.text((footer_x, footer_y), footer_right, fill="black", font=footer_font)

    # Final crop (same as leader cards for consistency)
    def final_crop(image, bleed_mm=3, card_width_mm=70, card_height_mm=120):
        width, height = image.size
        left = int((bleed_mm / card_width_mm) * width)
        top = int((bleed_mm / card_height_mm) * height)
        right = width - left
        bottom = height - top
        return image.crop((left, top, right, bottom))

    # Ensure results directory exists
    os.makedirs(result_path, exist_ok=True)

    final_img = final_crop(base_img)

    # Optional card number (small white number near the top-right), like leader cards.
    show_number = bool(input_data.get("show_number", True))
    card_number = input_data.get("card_number")
    if show_number and card_number is not None:
        try:
            number_text = str(int(card_number))
        except Exception:
            number_text = str(card_number)

        number_draw = ImageDraw.Draw(final_img)
        bbox = number_draw.textbbox((0, 0), number_text, font=number_font)
        text_w = bbox[2] - bbox[0]

        right_margin = _s(32)
        top_margin = _s(30)
        x = max(0, final_img.width - right_margin - text_w)
        y = max(0, top_margin)
        number_draw.text((x, y), number_text, fill="white", font=number_font)

    final_img.save(output_image_path, dpi=_DEFAULT_OUTPUT_DPI)
    print(f"Lore card saved at {output_image_path}")
    print(f"Settings used: render_scale={render_scale}, allow_upscale={allow_upscale}")
    
    return output_image_path


def generate_all_lore_cards(render_scale=None, allow_upscale=None):
    """Generate all lore cards defined in the lore_cards list."""
    for lore_card in lore_cards:
        try:
            lore_payload = dict(lore_card)
            if render_scale is not None:
                lore_payload["render_scale"] = render_scale
            if allow_upscale is not None:
                lore_payload["allow_upscale"] = allow_upscale
            create_lore_card(lore_payload)
        except Exception as e:
            print(f"Error generating lore card '{lore_card.get('name', 'Unknown')}': {e}")


def main(argv):
    parser = argparse.ArgumentParser(description="Generate lore cards.")
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
        help="Disallow upscaling low-res artwork (default behavior). Overrides per-card setting.",
    )
    parser.set_defaults(allow_upscale=None)

    parser.add_argument(
        "names",
        nargs="*",
        help="Optional lore card names to generate (case-insensitive). If omitted, generates all lore cards.",
    )

    parser.add_argument(
        "--number-start",
        type=int,
        dest="number_start",
        default=1,
        help=(
            "Starting number for lore cards. The first lore card in loreCardsFormatted.py will be this number, "
            "the next lore card will be +1, etc. Drawn as a small top-right number."
        ),
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        dest="no_numbers",
        help="Disable drawing the small top-right lore card number.",
    )

    args = parser.parse_args(argv[1:])

    requested_names = args.names
    selected_cards, missing = _select_lore_cards(lore_cards, requested_names)

    lore_index_by_name = {c.get("name", "").casefold(): idx for idx, c in enumerate(lore_cards)}

    if missing:
        print("Warning: unknown lore name(s): " + ", ".join(missing))

    if not selected_cards:
        print("No lore cards selected. Nothing to do.")
        return 1

    success_count = 0
    error_count = 0

    for card in selected_cards:
        try:
            lore_payload = dict(card)
            lore_payload["render_scale"] = args.render_scale
            if args.allow_upscale is not None:
                lore_payload["allow_upscale"] = args.allow_upscale

            if args.no_numbers:
                lore_payload["show_number"] = False
            else:
                idx = lore_index_by_name.get(lore_payload.get("name", "").casefold())
                if idx is not None:
                    lore_payload["card_number"] = args.number_start + idx

            name = lore_payload.get("name", "<unknown>")
            print(f"Creating lore card for: {name}")
            create_lore_card(lore_payload)
            success_count += 1
        except Exception as e:
            print(f"Error generating lore card '{card.get('name', 'Unknown')}': {e}")
            error_count += 1

    print(f"\nLore creation complete.")
    print(f"Lore processed successfully: {success_count}")
    print(f"Lore with errors: {error_count}")
    return 0 if error_count == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
