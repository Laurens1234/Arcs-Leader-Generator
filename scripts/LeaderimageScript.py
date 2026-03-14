import os

from PIL import Image, ImageDraw, ImageFont

_DEFAULT_OUTPUT_DPI = (300, 300)


def _clamp_int(value, minimum, maximum, default):
    try:
        value = int(value)
    except Exception:
        return default
    return max(minimum, min(maximum, value))


def create_card(input_data):
    # File paths
    base_path = os.path.dirname(os.path.dirname(__file__))
    custom_font_path = os.path.join(base_path, "fonts", "FMBolyarPro-900.ttf")
    neue_kabel_font_path = os.path.join(base_path, "fonts", "neue-kabel.otf")
    neue_kabel_bold_path = os.path.join(base_path, "fonts", "NeueKabel-Bold.otf")
    neue_kabel_italic_path = os.path.join(base_path, "fonts", "NeueKabel-Italic.otf")
    neue_kabel_bolditalic_path = os.path.join(base_path, "fonts", "NeueKabel-BoldItalic.otf")

    result_path = os.path.join(base_path, "results")
    leader_image_path = os.path.join(base_path, "cardAssets", "CardAssets-Tarot-Leader.png")
    text_box_image_path = os.path.join(base_path, "cardAssets", "CardAssets-Tarot-Fate-Text-Box.png")

    resource_fuel_path = os.path.join(base_path, "cardAssets/captured", "leader-resource-fuel.png")
    resource_material_path = os.path.join(base_path, "cardAssets/captured", "leader-resource-material.png")
    resource_psionic_path = os.path.join(base_path, "cardAssets/captured", "leader-resource-psionic.png")
    resource_relic_path = os.path.join(base_path, "cardAssets/captured", "leader-resource-relic.png")
    resource_weapon_path = os.path.join(base_path, "cardAssets/captured", "leader-resource-weapon.png")

    output_image_path = os.path.join(result_path, f"{input_data['name']}_Card.png")

    os.makedirs(result_path, exist_ok=True)

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

    base_img = Image.open(leader_image_path).convert("RGBA")
    text_box_img = Image.open(text_box_image_path).convert("RGBA")

    if render_scale != 1:
        base_img = base_img.resize(_s(base_img.size), Image.Resampling.LANCZOS)
        text_box_img = text_box_img.resize(_s(text_box_img.size), Image.Resampling.LANCZOS)

    leader_image_overlay_path = os.path.join(base_path, "cardAssets", "leaderImages", f"{input_data['name']}.png")

    try:
        overlay_img = Image.open(leader_image_overlay_path).convert("RGBA")

        # Keep the bottom of the leader image aligned to the original location
        # Support an optional `boundary_shift` fractional value in input_data
        # Positive shifts move the top boundary lower (down), negative moves it up.
        default_top_margin = 60
        shift = input_data.get("boundary_shift", 0.0)
        try:
            shift = float(shift)
        except Exception:
            shift = 0.0
        top_margin = max(0, int(_s(default_top_margin) * (1 + shift)))
        # Allow boundary_shift to also move the bottom alignment point
        default_overlay_bottom = 390
        overlay_bottom_y = int(_s(default_overlay_bottom) * (1 + shift))
        # Clamp bottom to image bounds and ensure it's below top_margin
        overlay_bottom_y = max(top_margin + 1, min(base_img.height - 1, overlay_bottom_y))
        max_allowed_height = max(0, overlay_bottom_y - top_margin)

        # Target width respects side margins but allow special-case sizing
        side_margin = _s(60)
        target_width = base_img.width - 2 * side_margin
        if input_data['name'] == "leadername":
            target_width = int(base_img.width / 1.5)

        iw, ih = overlay_img.size
        aspect_ratio = ih / iw
        target_height = int(target_width * aspect_ratio)

        # If height would overflow into the text area or above the margin, scale down
        if max_allowed_height > 0 and target_height > max_allowed_height:
            target_height = max_allowed_height
            target_width = max(1, int(target_height / aspect_ratio))

        # Support an optional zoom multiplier from input_data (e.g., 1.5 for 150%)
        zoom = input_data.get("zoom", 1.0)
        try:
            zoom = float(zoom)
        except Exception:
            zoom = 1.0

        # Apply zoom (allow overflow/cropping of sides as requested)
        target_width = max(1, int(target_width * zoom))
        target_height = max(1, int(target_height * zoom))

        if not allow_upscale:
            # Allow scaling up by up to render_scale (keeps the same logical size as before
            # while still letting higher-res output happen).
            max_w = iw * render_scale
            max_h = ih * render_scale
            if target_width > max_w or target_height > max_h:
                target_width = min(target_width, max_w)
                target_height = min(target_height, max_h)
                print(
                    f"Note: '{input_data['name']}' overlay is smaller than the requested size; "
                    f"clamping to source resolution to avoid blur. "
                    f"Set allow_upscale=True to keep it full-size."
                )

        overlay_img = overlay_img.resize((target_width, target_height), Image.Resampling.LANCZOS)

        overlay_x = (base_img.width - overlay_img.width) // 2
        overlay_y = overlay_bottom_y - overlay_img.height

        base_img.paste(overlay_img, (overlay_x, overlay_y), overlay_img)

    except FileNotFoundError:
        print(f"Warning: Overlay image '{input_data['name']}.png' not found. Proceeding without overlay.")


    # Resize resource images
    resource_size = _s((55, 55))

    def load_and_resize(path):
        return Image.open(path).convert("RGBA").resize(resource_size, Image.Resampling.LANCZOS)

    resources = {
        "Fuel": load_and_resize(resource_fuel_path),
        "Material": load_and_resize(resource_material_path),
        "Psionic": load_and_resize(resource_psionic_path),
        "Relic": load_and_resize(resource_relic_path),
        "Weapon": load_and_resize(resource_weapon_path),
    }

    chosen_resources = input_data['resources']
    resource_1 = resources[chosen_resources[0]]
    resource_2 = resources[chosen_resources[1]]

    # Positioning text box
    text_box_x = (base_img.width - text_box_img.width) // 2
    text_box_y = base_img.height - text_box_img.height
    combined_img = base_img.copy()
    combined_img.paste(text_box_img, (text_box_x, text_box_y), text_box_img)

    draw = ImageDraw.Draw(combined_img)

    # Fonts
    try:
        body_font_size = input_data.get("body_font_size", 18)
        title_font = ImageFont.truetype(custom_font_path, _s(25))
        number_font = ImageFont.truetype(custom_font_path, _s(16))
        body_font = ImageFont.truetype(neue_kabel_font_path, _s(body_font_size))
        italic_font = ImageFont.truetype(neue_kabel_italic_path, _s(body_font_size))
        bold_font = ImageFont.truetype(neue_kabel_bold_path, _s(body_font_size))
        bolditalic_font = ImageFont.truetype(neue_kabel_bolditalic_path, _s(body_font_size))
    except IOError:
        title_font = number_font = body_font = italic_font = bold_font = bolditalic_font = ImageFont.load_default()
        body_font_size = input_data.get("body_font_size", 18)

    # Setup images resize while keeping aspect ratio
    def get_setup_image_path(slot, setup_data):
        building = setup_data["building"]
        ships = setup_data["ships"]
        building_str = building.lower() if building.lower() != "none" else "none"
        file_name = f"{slot}-{building_str}-{ships}ships.png"
        return os.path.join(base_path, "cardAssets", "captured", file_name)

    setup_image_size = _s((50, 50))

    def load_and_resize_setup(path):
        img = Image.open(path).convert("RGBA")
        width, height = img.size
        aspect_ratio = height / width
        new_height = _s(50)
        new_width = int(new_height / aspect_ratio)
        return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    setup_data = input_data["setup"]
    setup_a_img = load_and_resize_setup(get_setup_image_path("A", setup_data["A"]))
    setup_b_img = load_and_resize_setup(get_setup_image_path("B", setup_data["B"]))
    setup_c_img = load_and_resize_setup(get_setup_image_path("C", setup_data["C"]))

    setup_a_building = setup_data["A"]["building"].lower() != "none"
    setup_b_building = setup_data["B"]["building"].lower() != "none"
    
    # Paste resources
    resource_x = _s(100)
    resource_y = combined_img.height - resource_size[1] - _s(22)
    resource_x2 = resource_x + resource_size[0] + _s(5)
    
    setup_start_x = resource_x2 + resource_size[0] - _s(20)
    setup_y = resource_y - setup_image_size[1] // 2
    setup_spacing = _s(25)

    if not setup_a_building and not setup_b_building:
        for x, res in zip([resource_x + _s(20), resource_x2 + _s(20)], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)
        combined_img.paste(setup_a_img, (setup_start_x + _s(20), setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing - _s(10), setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing) - _s(40), setup_y), setup_c_img)
    elif not setup_a_building:
        for x, res in zip([resource_x + _s(10) , resource_x2 + _s(10)], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)        
        combined_img.paste(setup_a_img, (setup_start_x + _s(10) , setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing-_s(20), setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing)-_s(20), setup_y), setup_c_img)
    elif not setup_b_building:
        for x, res in zip([resource_x + _s(10), resource_x2 + _s(10)], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)
        combined_img.paste(setup_a_img, (setup_start_x + _s(10), setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing + _s(12), setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing) - _s(20), setup_y), setup_c_img)
    else:
        for x, res in zip([resource_x, resource_x2], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)
        combined_img.paste(setup_a_img, (setup_start_x, setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing + _s(1), setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing), setup_y), setup_c_img)


    # Title and abilities
    title_text = input_data['name']
    body_text = input_data['abilities']

    text_x0, text_y0 = _s(60), _s(390)
    text_x1, text_y1 = _s(390), _s(645)
    text_width = text_x1 - text_x0

    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = text_x0 + (text_width - (title_bbox[2] - title_bbox[0])) // 2
    title_y = text_y0
    draw.text((title_x, title_y), title_text, fill="black", font=title_font)

    line_y = title_y + (title_bbox[3] - title_bbox[1]) + _s(12)
    draw.line((text_x0, line_y, text_x1, line_y), fill="black", width=_s(3))

    # Text wrapping and rich text rendering
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
                draw.text((current_x, current_y + adjust_y), trailing, font=font, fill="black")
                current_x += trailing_width

            space_width = draw.textbbox((0, 0), " ", font=font)[2]
            current_x += space_width

        return current_y + line_height

    current_y = line_y + _s(10)
    for line in wrap_text(body_text, body_font, italic_font, bold_font, bolditalic_font, text_width):
        if not line.strip():
            current_y += _s(10)
            continue
        current_y = draw_rich_text(draw, line, body_font, italic_font, bold_font, bolditalic_font, text_x0, current_y, text_width, _s(22))

    # Final crop
    def final_crop(image, bleed_mm=3, card_width_mm=70, card_height_mm=120):
        width, height = image.size
        left = int((bleed_mm / card_width_mm) * width)
        top = int((bleed_mm / card_height_mm) * height)
        right = width - left
        bottom = height - top
        return image.crop((left, top, right, bottom))

    combined_img = final_crop(combined_img)

    # Optional card number (small white number near the top-right)
    show_number = bool(input_data.get("show_number", True))
    card_number = input_data.get("card_number")
    if show_number and card_number is not None:
        try:
            number_text = str(int(card_number))
        except Exception:
            number_text = str(card_number)

        number_draw = ImageDraw.Draw(combined_img)
        bbox = number_draw.textbbox((0, 0), number_text, font=number_font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        # Increase margins to move the number down and left.
        right_margin = _s(32)
        top_margin = _s(30)
        x = max(0, combined_img.width - right_margin - text_w)
        y = max(0, top_margin)

        number_draw.text((x, y), number_text, fill="white", font=number_font)

    combined_img.save(output_image_path, dpi=_DEFAULT_OUTPUT_DPI)
    print(f"Combined image saved at {output_image_path}")
    print(f"Settings used: render_scale={render_scale}, allow_upscale={allow_upscale}")
