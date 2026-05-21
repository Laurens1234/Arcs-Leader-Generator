import os

from PIL import Image, ImageDraw, ImageFont

_DEFAULT_OUTPUT_DPI = (300, 300)


def _clamp_int(value, minimum, maximum, default):
    try:
        value = int(value)
    except Exception:
        return default
    return max(minimum, min(maximum, value))


def _as_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default


def create_card(input_data):
    # File paths
    base_path = os.path.dirname(os.path.dirname(__file__))
    custom_font_path = os.path.join(base_path, "fonts", "FMBolyarPro-900.ttf")
    neue_kabel_font_path = os.path.join(base_path, "fonts", "neue-kabel.otf")
    neue_kabel_bold_path = os.path.join(base_path, "fonts", "NeueKabel-Bold.otf")
    neue_kabel_italic_path = os.path.join(base_path, "fonts", "NeueKabel-Italic.otf")
    neue_kabel_bolditalic_path = os.path.join(base_path, "fonts", "NeueKabel-BoldItalic.otf")

    result_path = os.path.join(base_path, "results", "leader")
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

    # Prefer an explicit image name if provided; also accept the legacy/mistyped key "image_name:"
    overlay_basename = None
    try:
        overlay_basename = input_data.get("image_name") or input_data.get("image_name:")
    except Exception:
        overlay_basename = None
    if not overlay_basename:
        overlay_basename = input_data.get("name")
    overlay_basename = str(overlay_basename)
    # Prefer per-card artwork from the unified `cardAssets/cardImages` folder
    leader_image_overlay_path = os.path.join(base_path, "cardAssets", "cardImages", f"{overlay_basename}.png")

    # If a session upload directory is provided via env var, prefer that image first
    uploaded_dir = os.environ.get("ADK_UPLOAD_DIR")
    uploaded_overlay_path = None
    if uploaded_dir:
        uploaded_overlay_path = os.path.join(uploaded_dir, f"{overlay_basename}.png")

    overlay_img = None
    paths_to_try = [p for p in (uploaded_overlay_path, leader_image_overlay_path) if p]
    for pth in paths_to_try:
        try:
            overlay_img = Image.open(pth).convert("RGBA")
            leader_image_overlay_path = pth
            break
        except FileNotFoundError:
            overlay_img = None

    if overlay_img is None:
        print(f"Warning: Overlay image '{overlay_basename}.png' not found. Proceeding without overlay.")
    else:
        # Keep the bottom of the leader image aligned to the original location
        # Support an optional `boundary_shift` fractional value in input_data
        # Positive shifts move the top boundary lower (down), negative moves it up.
        default_top_margin = 60
        shift = _as_float(input_data.get("boundary_shift", 0.0), 0.0)
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
        zoom = _as_float(input_data.get("zoom", 1.0), 1.0)

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

        # Optional horizontal art nudge in logical pixels; negative moves left, positive moves right.
        image_shift_x = _as_float(
            input_data.get(
                "image_shift_x",
                input_data.get("art_shift_x", input_data.get("image_offset_x", 0.0)),
            ),
            0.0,
        )
        overlay_x = (base_img.width - overlay_img.width) // 2 + _s(image_shift_x)
        overlay_y = overlay_bottom_y - overlay_img.height

        base_img.paste(overlay_img, (overlay_x, overlay_y), overlay_img)
        


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

    chosen_resources = input_data.get("resources")
    if isinstance(chosen_resources, (list, tuple)):
        chosen_resources_list = list(chosen_resources)
    elif isinstance(chosen_resources, str):
        chosen_resources_list = [chosen_resources]
    else:
        chosen_resources_list = []

    resource_imgs = []
    for res_name in chosen_resources_list:
        if not res_name:
            continue
        img = resources.get(res_name)
        if img is None:
            print(
                f"Warning: Unknown resource '{res_name}' for leader '{input_data.get('name', '<unknown>')}'. "
                "Skipping it."
            )
            continue
        resource_imgs.append(img)
        if len(resource_imgs) >= 2:
            break

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
        number_font = ImageFont.truetype(custom_font_path, _s(14))
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

    has_resources = len(resource_imgs) > 0

    def _paste_resources(center_xs):
        if not has_resources:
            return
        for x, res in zip(center_xs, resource_imgs):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)

    setup_spacing = _s(25)

    if has_resources:
        setup_start_x = resource_x2 + resource_size[0] - _s(20)
    else:
        # If no resources are provided, center the setup icons on the card
        total_setup_width = 2 * setup_spacing + 3 * setup_image_size[0]
        setup_start_x = (base_img.width - total_setup_width) // 2
    setup_y = resource_y - setup_image_size[1] // 2

    if not setup_a_building and not setup_b_building:
        _paste_resources([resource_x + _s(20), resource_x2 + _s(20)])
        combined_img.paste(setup_a_img, (setup_start_x + _s(20), setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing - _s(10), setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing) - _s(40), setup_y), setup_c_img)
    elif not setup_a_building:
        _paste_resources([resource_x + _s(10), resource_x2 + _s(10)])
        combined_img.paste(setup_a_img, (setup_start_x + _s(10) , setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing-_s(20), setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing)-_s(20), setup_y), setup_c_img)
    elif not setup_b_building:
        _paste_resources([resource_x + _s(10), resource_x2 + _s(10)])
        combined_img.paste(setup_a_img, (setup_start_x + _s(10), setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing + _s(12), setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing) - _s(20), setup_y), setup_c_img)
    else:
        _paste_resources([resource_x, resource_x2])
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
        kind, payload, trailing, font_to_use = _parse_rich_token(
            token, font, italic_font, bold_font, bolditalic_font
        )
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
        paragraphs = text.split('\n')
        wrapped_lines = []
        for para in paragraphs:
            if not para.strip():
                wrapped_lines.append([])
                continue
            words = para.strip().split()

            # Combine words into rich tokens so formatting markers can span spaces
            tokens: list[str] = []
            i = 0
            while i < len(words):
                w = words[i]
                core, _ = _split_trailing_punct(w)
                if core.casefold().startswith('{icon:') and w.endswith('}'):
                    tokens.append(w)
                    i += 1
                    continue

                combined = False
                for marker in ("***", "**", "*"):
                    stripped_core = core.rstrip(''.join(_TRAILING_PUNCT))
                    if stripped_core.startswith(marker) and not stripped_core.endswith(marker):
                        buf = [w]
                        j = i + 1
                        closed = False
                        while j < len(words):
                            buf.append(words[j])
                            core_buf = _split_trailing_punct(" ".join(buf))[0]
                            if core_buf.rstrip(''.join(_TRAILING_PUNCT)).endswith(marker):
                                closed = True
                                break
                            j += 1
                        tokens.append(" ".join(buf))
                        i = j + 1 if closed else j
                        combined = True
                        break
                if not combined:
                    tokens.append(w)
                    i += 1

            # Expand any single rich token that is wider than the max width into
            # multiple rich-word tokens so it can wrap across lines.
            expanded_tokens: list[str] = []
            for t in tokens:
                if " " in t and _measure_rich_token(t, font, italic_font, bold_font, bolditalic_font) > max_width:
                    if (t.startswith('***') and t.endswith('***')) or (t.startswith('**') and t.endswith('**')) or (t.startswith('*') and t.endswith('*')):
                        marker = '***' if t.startswith('***') and t.endswith('***') else ('**' if t.startswith('**') and t.endswith('**') else '*')
                        inner = t[len(marker):-len(marker)]
                        parts = inner.split()
                        for p in parts:
                            expanded_tokens.append(f"{marker}{p}{marker}")
                    else:
                        for p in t.split():
                            expanded_tokens.append(p)
                else:
                    expanded_tokens.append(t)

            current_line_tokens: list[str] = []
            current_line_width = 0

            for idx, token in enumerate(expanded_tokens):
                token_width = _measure_rich_token(token, font, italic_font, bold_font, bolditalic_font)
                space_width = draw.textbbox((0, 0), " ", font=font)[2]
                additional_width = token_width if idx == 0 else token_width + space_width

                if current_line_width + additional_width <= max_width:
                    current_line_tokens.append(token)
                    current_line_width += additional_width
                else:
                    wrapped_lines.append(current_line_tokens)
                    current_line_tokens = [token]
                    current_line_width = token_width

            if current_line_tokens:
                wrapped_lines.append(current_line_tokens)

        return wrapped_lines

    def draw_rich_text(draw, tokens, font, italic_font, bold_font, bolditalic_font, x, y, max_width, line_height):
        line_height = line_height * (body_font_size / 18)
        current_x = x
        current_y = y

        # Align baselines across fonts using ascent metrics.
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

        for word in tokens:
            kind, payload, trailing, font_to_use = _parse_rich_token(
                word, font, italic_font, bold_font, bolditalic_font
            )

            if kind == "icon":
                icon_y_offset, base_icon_height = _icon_layout_for_font(font)
                icon_height = _icon_target_height(payload, base_icon_height)
                icon_img = _load_icon(payload, icon_height)
                icon_width = icon_img.width if icon_img is not None else int(icon_height)

                # Bottom-align to the line's baseline box even when scaled.
                icon_y = current_y + icon_y_offset + (base_icon_height - icon_height)

                if icon_img is not None:
                    combined_img.paste(icon_img, (int(current_x), int(icon_y)), icon_img)
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
                # Trailing punctuation is outside the rich marker (e.g. "**tax**,")
                # so it should use the normal font *and* the normal baseline.
                draw.text((current_x, current_y), trailing, font=font, fill="black")
                current_x += trailing_width

            space_width = draw.textbbox((0, 0), " ", font=font)[2]
            current_x += space_width

        return current_y + line_height

    current_y = line_y + _s(8)
    first_body_line = True
    for line in wrap_text(body_text, body_font, italic_font, bold_font, bolditalic_font, text_width):
        # Support explicit vertical-space token in the body: "{vspace:N}"
        # Example: "{vspace:6}" adds _s(6) pixels of vertical space. The token
        # must occupy the line by itself (leading spaces allowed).
        if not line:
            current_y += _s(10)
            continue

        line_str = " ".join(line).strip()
        if line_str.startswith("{vspace:") and line_str.endswith("}"):
            try:
                inner = line_str[len("{vspace:"):-1].strip()
                n = int(inner)
                current_y += _s(n)
                continue
            except Exception:
                pass

        # If the line begins with an italic token whose text ends with a period,
        # add a bit more vertical spacing to separate it from the previous line.
        # Do not add this extra spacing if this is the first non-empty body line on the card.
        try:
            if not first_body_line and line:
                first_word = line[0]
                kind, payload, trailing, font_to_use = _parse_rich_token(
                    first_word, body_font, italic_font, bold_font, bolditalic_font
                )
                if font_to_use is italic_font and isinstance(payload, str) and payload.endswith('.'):
                    current_y += _s(4)
        except Exception:
            pass

        current_y = draw_rich_text(draw, line, body_font, italic_font, bold_font, bolditalic_font, text_x0, current_y, text_width, _s(22))
        first_body_line = False

    # Final crop
    # The base templates include a 3mm bleed on all sides (total size = card + 2*bleed).
    # Crop the bleed away so the exported PNG matches the trimmed card size.
    def final_crop(image, bleed_mm=3, card_width_mm=70, card_height_mm=120):
        width, height = image.size

        total_width_mm = card_width_mm + 2 * bleed_mm
        total_height_mm = card_height_mm + 2 * bleed_mm

        # Compute the trimmed pixel size via proportional scaling from the full-bleed canvas.
        # Using round() avoids systematic undersizing from floor truncation.
        target_w = int(round(width * (card_width_mm / total_width_mm)))
        target_h = int(round(height * (card_height_mm / total_height_mm)))

        # Center-crop; if odd pixels need to be removed, the extra pixel lands on right/bottom.
        left = max(0, (width - target_w) // 2)
        top = max(0, (height - target_h) // 2)
        right = min(width, left + target_w)
        bottom = min(height, top + target_h)
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
