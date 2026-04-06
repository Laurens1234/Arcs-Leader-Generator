import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

from scripts.voxCardsFormatted import vox_cards

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


def create_vox_card(input_data):
    """Creates a Vox card using the same pipeline as lore cards, but with the Vox frame and higher text placement."""

    base_path = os.path.dirname(os.path.dirname(__file__))

    # Font paths
    custom_font_path = os.path.join(base_path, "fonts", "FMBolyarPro-900.ttf")
    neue_kabel_font_path = os.path.join(base_path, "fonts", "neue-kabel.otf")
    neue_kabel_bold_path = os.path.join(base_path, "fonts", "NeueKabel-Bold.otf")
    neue_kabel_italic_path = os.path.join(base_path, "fonts", "NeueKabel-Italic.otf")
    neue_kabel_bolditalic_path = os.path.join(base_path, "fonts", "NeueKabel-BoldItalic.otf")

    # Asset paths
    result_path = os.path.join(base_path, "results", "vox")
    vox_frame_path = os.path.join(base_path, "cardAssets", "CardAsset-Frame-Vox.png")
    vox_image_folder = os.path.join(base_path, "cardAssets", "voxImages")
    footer_image_path = os.path.join(base_path, "cardAssets", "CardAsset-Footer-Paper.png")

    output_image_path = os.path.join(result_path, f"{input_data['name']}_Vox_Card.png")

    render_scale = _clamp_int(input_data.get("render_scale", 2), 1, 4, 2)
    allow_upscale = bool(input_data.get("allow_upscale", True))

    def _s(value):
        if isinstance(value, tuple):
            return tuple(int(v * render_scale) for v in value)
        return int(value * render_scale)

    vox_frame = Image.open(vox_frame_path).convert("RGBA")
    if render_scale != 1:
        vox_frame = vox_frame.resize(_s(vox_frame.size), Image.Resampling.LANCZOS)

    card_width, card_height = vox_frame.size

    # Base canvas
    base_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 255))

    # Frame overlay
    base_img.paste(vox_frame, (0, 0), vox_frame)

    # Vox artwork layer (on top of the frame).
    # Text is drawn after this, so it remains readable.
    vox_art_path = os.path.join(vox_image_folder, f"{input_data['name']}.png")
    try:
        art_img = Image.open(vox_art_path).convert("RGBA")

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
                    f"Note: '{input_data['name']}' vox art is smaller than the frame width; "
                    f"not upscaling to avoid blur. Set allow_upscale=True to keep it full-size."
                )

        art_img = art_img.resize((target_width, target_height), Image.Resampling.LANCZOS)

        # Place art near the bottom by default; boundary_shift nudges the alignment.
        shift = input_data.get("boundary_shift", 0.0)
        try:
            shift = float(shift)
        except Exception:
            shift = 0.0

        bottom_margin = _s(0)
        art_bottom_y = int((card_height - bottom_margin) * (1 + shift))
        art_bottom_y = max(1, min(card_height, art_bottom_y))

        art_x = (card_width - art_img.width) // 2
        art_y = art_bottom_y - art_img.height
        base_img.paste(art_img, (art_x, art_y), art_img)

    except FileNotFoundError:
        print(
            f"Warning: Vox image '{input_data['name']}.png' not found in voxImages folder. Proceeding without image."
        )

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

    # Text area (higher than lore)
    text_margin = _s(40)
    text_x0 = text_margin
    text_x1 = card_width - text_margin
    text_width = text_x1 - text_x0

    # Vox text starts much higher up than lore cards.
    text_y0 = _s(55)

    title_text = input_data.get("title", input_data["name"])
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = text_x0 + (text_width - (title_bbox[2] - title_bbox[0])) // 2
    title_y = text_y0
    draw.text((title_x, title_y), title_text, fill="black", font=title_font)

    line_y = title_y + (title_bbox[3] - title_bbox[1]) + _s(12)

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

        if core.startswith("***") and core.endswith("***") and len(core) > 6:
            text_to_draw = core[3:-3]
            font_to_use = bolditalic_font
        elif core.startswith("**") and core.endswith("**") and len(core) > 4:
            text_to_draw = core[2:-2]
            font_to_use = bold_font
        elif core.startswith("*") and core.endswith("*") and len(core) > 2:
            text_to_draw = core[1:-1]
            font_to_use = italic_font

        return text_to_draw, trailing, font_to_use

    def _measure_rich_token(token: str, font, italic_font, bold_font, bolditalic_font) -> int:
        text_to_draw, trailing, font_to_use = _parse_rich_token(token, font, italic_font, bold_font, bolditalic_font)
        main_bbox = draw.textbbox((0, 0), text_to_draw, font=font_to_use)
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
            text_to_draw, trailing, font_to_use = _parse_rich_token(word, font, italic_font, bold_font, bolditalic_font)
            adjust_y = _baseline_adjust(font_to_use)

            word_bbox = draw.textbbox((0, 0), text_to_draw, font=font_to_use)
            word_width = word_bbox[2] - word_bbox[0]
            draw.text((current_x, current_y + adjust_y), text_to_draw, font=font_to_use, fill="black")
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
        if not line.strip():
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

    # Footer paper overlay and footer text (same as lore)
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
        placeholder = (text or "V")[0]
        single_w = _text_width(placeholder)
        target_center = footer_margin + single_w / 2
        return int(round(target_center - _text_width(text) / 2))

    def _x_centered_like_one_char_right(text: str) -> int:
        placeholder = (text or "0")[0]
        single_w = _text_width(placeholder)
        right_edge = card_width - footer_margin + _s(5)
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
            footer_x = card_width - footer_margin - _text_width(footer_right_str) + _s(5)
        else:
            footer_x = _x_centered_like_one_char_right(footer_right_str)
        draw.text((footer_x, footer_y), footer_right_str, fill="black", font=footer_font)

    def final_crop(image, bleed_mm=3, card_width_mm=70, card_height_mm=120):
        width, height = image.size
        left = int((bleed_mm / card_width_mm) * width)
        top = int((bleed_mm / card_height_mm) * height)
        right = width - left
        bottom = height - top
        return image.crop((left, top, right, bottom))

    os.makedirs(result_path, exist_ok=True)

    final_img = final_crop(base_img)
    final_img.save(output_image_path, dpi=_DEFAULT_OUTPUT_DPI)

    print(f"Vox card saved at {output_image_path}")
    print(f"Settings used: render_scale={render_scale}, allow_upscale={allow_upscale}")

    return output_image_path


def main(argv):
    parser = argparse.ArgumentParser(description="Generate Vox cards.")
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
        help="Optional Vox card names to generate (case-insensitive). If omitted, generates all Vox cards.",
    )

    parser.add_argument(
        "--number-start",
        type=int,
        dest="number_start",
        default=1,
        help=(
            "Starting number for Vox cards. The first card in voxCardsFormatted.py will be this number, "
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

    selected, missing = _select_cards(vox_cards, args.names)
    index_by_name = {c.get("name", "").casefold(): idx for idx, c in enumerate(vox_cards)}

    if missing:
        print("Warning: unknown Vox name(s): " + ", ".join(missing))

    if not selected:
        print("No Vox cards selected. Nothing to do.")
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
            print(f"Creating Vox card for: {name}")
            create_vox_card(payload)
            success += 1
        except Exception as e:
            print(f"Error generating Vox card '{card.get('name', 'Unknown')}': {e}")
            errors += 1

    print("\nVox creation complete.")
    print(f"Vox processed successfully: {success}")
    print(f"Vox with errors: {errors}")
    return 0 if errors == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
