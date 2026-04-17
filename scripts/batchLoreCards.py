import argparse
import importlib
import importlib.util
import os
import sys
import random

from PIL import Image, ImageDraw, ImageFont

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

# Prefer YAML data files in `scripts/data/` but fall back to importing the existing
# formatted Python module for compatibility. Allow overriding via `ADK_DATA_DIR`.
data_dir_env = os.environ.get("ADK_DATA_DIR")
if data_dir_env:
    data_dir = data_dir_env
else:
    data_dir = os.path.join(script_dir, "scripts", "data")

# Allow the caller to request a specific data filename (e.g. edifice.yml)
data_name_env = os.environ.get("ADK_DATA_FILENAME")
if data_name_env:
    full_path = os.path.join(data_dir, data_name_env)
    stem = os.path.splitext(data_name_env)[0]
    single_path = os.path.join(data_dir, f"{stem}_single.yml")
else:
    full_path = os.path.join(data_dir, "lore.yml")
    single_path = os.path.join(data_dir, "lore_single.yml")

lore_cards = None
chosen_path = None
try:
    import yaml

    if os.path.exists(single_path):
        chosen_path = single_path
    elif os.path.exists(full_path):
        chosen_path = full_path

    if chosen_path:
        try:
            with open(chosen_path, encoding="utf-8") as f:
                lore_cards = yaml.safe_load(f)
        except Exception as e:
            print(f"[loreCards] Failed to load YAML at {chosen_path}: {e}")
            sys.exit(2)

        if lore_cards is None and data_dir_env:
            print(f"[loreCards] YAML at {chosen_path} is empty or invalid")
            sys.exit(2)
except Exception:
    lore_cards = None

if lore_cards is None:
    # No YAML present -> fall back to legacy .py module
    from scripts.legacy.loreCardsFormatted import lore_cards

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
    # Use unified per-card artwork folder under cardAssets/cardImages
    lore_image_folder = os.path.join(base_path, "cardAssets", "cardImages")
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
    # Determine variant early so we can choose the card background
    variant = (input_data.get("variant") or "").casefold()

    # Load the lore frame to get card dimensions (or use Edifice background for edifice variant)
    if variant == "edifice":
        edifice_asset_path = os.path.join(base_path, "cardAssets", "Edifice.png")
        try:
            edifice_img = Image.open(edifice_asset_path).convert("RGBA")
            if render_scale != 1:
                edifice_img = edifice_img.resize(_s(edifice_img.size), Image.Resampling.LANCZOS)
            card_width, card_height = edifice_img.size
            base_img = edifice_img.copy()
        except FileNotFoundError:
            print(f"Warning: Edifice asset not found at {edifice_asset_path}. Falling back to normal lore frame.")
            lore_frame = Image.open(lore_frame_path).convert("RGBA")
            if render_scale != 1:
                lore_frame = lore_frame.resize(_s(lore_frame.size), Image.Resampling.LANCZOS)
            card_width, card_height = lore_frame.size
            base_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 255))
            variant = ""  # fallback to normal behavior
    else:
        lore_frame = Image.open(lore_frame_path).convert("RGBA")
        if render_scale != 1:
            lore_frame = lore_frame.resize(_s(lore_frame.size), Image.Resampling.LANCZOS)
        card_width, card_height = lore_frame.size
        # Prefer the small background image (use it as-is, no random crop/zoom).
        small_bg_path = os.path.join(base_path, "cardAssets", "arcs_star_background_small.png")
        # Per-card override: set `use_large_bg: true` to force the large background
        # even when the small background file exists.
        if not input_data.get("use_large_bg", False) and os.path.exists(small_bg_path):
            try:
                small_bg = Image.open(small_bg_path).convert("RGBA")
                sb_w, sb_h = small_bg.size
                # Scale so the small background is at least as wide as the card
                # and at least as tall as the top half, preserving aspect ratio.
                target_half_h = card_height // 2
                scale_w = card_width / float(sb_w)
                scale_h = target_half_h / float(sb_h)
                scale = max(scale_w, scale_h, 1.0)
                new_w = max(1, int(round(sb_w * scale)))
                new_h = max(1, int(round(sb_h * scale)))
                small_bg = small_bg.resize((new_w, new_h), Image.Resampling.LANCZOS)

                base_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 255))
                paste_x = int(round((card_width - new_w) / 2))
                paste_y = 0  # align top so it covers the top half
                base_img.paste(small_bg, (paste_x, paste_y), small_bg)
            except Exception:
                base_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 255))
        else:
            # Try to use the themed background image with a configurable zoom and optional seed.
            bg_path = os.path.join(base_path, "cardAssets", "arcs_stars_background.png")
            try:
                bg_img = Image.open(bg_path).convert("RGBA")

                # Background zoom: default 1.5x (less extreme than previous defaults).
                # Can be overridden per-card via `bg_zoom` or globally via env `ADK_BG_ZOOM`.
                try:
                    zoom = float(input_data.get("bg_zoom", os.environ.get("ADK_BG_ZOOM", 1.5)))
                except Exception:
                    zoom = 1.5
                if zoom < 1.0:
                    zoom = 1.0

                # Optional deterministic seed: `bg_seed` or env `ADK_BG_SEED`.
                seed_val = input_data.get("bg_seed", os.environ.get("ADK_BG_SEED"))
                rng = random.Random()
                try:
                    if seed_val is not None:
                        rng.seed(int(seed_val))
                except Exception:
                    pass

                crop_w = max(1, int(round(card_width / zoom)))
                crop_h = max(1, int(round(card_height / zoom)))

                bg_w, bg_h = bg_img.size
                # Ensure background is at least as big as the desired crop by scaling up if necessary
                if bg_w < crop_w or bg_h < crop_h:
                    scale = max(crop_w / bg_w, crop_h / bg_h)
                    new_w = max(bg_w, int(round(bg_w * scale)))
                    new_h = max(bg_h, int(round(bg_h * scale)))
                    bg_img = bg_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                    bg_w, bg_h = bg_img.size

                max_x = max(0, bg_w - crop_w)
                max_y = max(0, bg_h - crop_h)
                left = rng.randint(0, max_x)
                top = rng.randint(0, max_y)
                cropped = bg_img.crop((left, top, left + crop_w, top + crop_h))
                base_img = cropped.resize((card_width, card_height), Image.Resampling.LANCZOS)
            except Exception:
                base_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 255))

    # Load and paste lore image (top half of the card), skip for edifice variant
    if variant != "edifice":
        # Prefer any session-uploaded image (from the web UI) before falling back
        # to the repo `cardAssets/cardImages` folder.
        # Determine which basename to use for artwork: honor explicit image_name
        # (or legacy 'image_name:') if present, otherwise use the card `name` field
        image_basename = input_data.get("image_name") or input_data.get("image_name:") or input_data.get("name")
        uploaded_dir = os.environ.get("ADK_UPLOAD_DIR")
        uploaded_path = os.path.join(uploaded_dir, f"{image_basename}.png") if uploaded_dir and image_basename else None
        lore_image_path = os.path.join(lore_image_folder, f"{image_basename}.png")
        lore_img = None
        paths_to_try = [p for p in (uploaded_path, lore_image_path) if p]
        for pth in paths_to_try:
            try:
                lore_img = Image.open(pth).convert("RGBA")
                lore_image_path = pth
                break
            except FileNotFoundError:
                lore_img = None
        try:
            if lore_img is None:
                raise FileNotFoundError()

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
            print(f"Warning: Lore image '{image_basename}.png' not found in cardAssets/cardImages folder or upload dir. Proceeding without image.")

    # Paste the lore frame on top (skip for edifice since edifice is the full background)
    if variant != "edifice":
        base_img.paste(lore_frame, (0, 0), lore_frame)

    # Create drawing context
    draw = ImageDraw.Draw(base_img)

    # Load fonts
    try:
        # Default sizes: preserve original lore card defaults
        title_font_size = input_data.get("title_font_size", 25)
        footer_font_size = input_data.get("footer_font_size", 14)
        body_font_size = input_data.get("body_font_size", 18)
        # Increase sizes for edifice variant (twice as big)
        if variant == "edifice":
            try:
                title_font_size = int(title_font_size * 2)
            except Exception:
                title_font_size = title_font_size
            try:
                body_font_size = int(body_font_size * 2)
            except Exception:
                body_font_size = body_font_size

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

    # Text area dimensions (adjust these based on the lore frame layout)
    # Allow per-card override for text margins. Values are in logical pixels
    # before scaling. If not provided, defaults are used. Edifice default is wider.
    if input_data.get("text_margin") is not None:
        try:
            text_margin = _s(int(input_data.get("text_margin")))
        except Exception:
            text_margin = _s(40)
    else:
        if variant == "edifice":
            text_margin = _s(int(input_data.get("text_margin_edifice", 48)))
        else:
            text_margin = _s(40)
    text_x0 = text_margin
    text_x1 = card_width - text_margin
    text_width = text_x1 - text_x0
    
    # Title position (below the image area)
    text_y0 = int(card_height * 0.545)  # Start below the top half
    
    # Determine text color (white for edifice variant)
    text_color = "white" if variant == "edifice" else "black"

    # Draw title text (centered)
    # Card title is now the `name` field; fall back to legacy `title` if absent
    title_text = input_data.get('name') or input_data.get('title') or input_data['name']
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = text_x0 + (text_width - (title_bbox[2] - title_bbox[0])) // 2
    # Slightly raise the title (less downward offset); smaller for default, reduced for edifice
    # For edifice variant, use a smaller downward offset so the title sits higher.
    title_y = text_y0 + (_s(16) if variant == "edifice" else _s(0))
    draw.text((title_x, title_y), title_text, fill=text_color, font=title_font)

    # Calculate line_y for body text positioning (no line drawn)
    line_y = title_y + (title_bbox[3] - title_bbox[1]) + _s(12)

    icon_assets_dir = os.path.join(base_path, "icon and punchboard")
    _icon_cache = {}
    _missing_icon_warned = set()

    # Text wrapping function
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
                wrapped_lines.append([])  # Preserve empty lines for paragraph breaks
                continue
            words = para.strip().split()

            # Combine words into rich tokens so formatting markers can span spaces
            tokens: list[str] = []
            i = 0
            while i < len(words):
                w = words[i]
                core, _ = _split_trailing_punct(w)
                # Icon tokens remain single-word
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
                    # Try to preserve outer rich markers
                    if (t.startswith('***') and t.endswith('***')) or (t.startswith('**') and t.endswith('**')) or (t.startswith('*') and t.endswith('*')):
                        # find the marker used
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

    # Rich text rendering function
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
                draw.text((current_x, current_y + adjust_y), payload, font=font_to_use, fill=text_color)
                current_x += word_width

            if trailing:
                trailing_bbox = draw.textbbox((0, 0), trailing, font=font)
                trailing_width = trailing_bbox[2] - trailing_bbox[0]
                # Trailing punctuation is outside the rich marker (e.g. "**tax**,")
                # so it should use the normal font *and* the normal baseline.
                draw.text((current_x, current_y), trailing, font=font, fill=text_color)
                current_x += trailing_width

            space_width = draw.textbbox((0, 0), " ", font=font)[2]
            current_x += space_width

        return current_y + line_height

    # Draw body text
    body_text = input_data.get('body', '')
    # Move body a bit lower; edifice variant gets a larger offset
    # Increase edifice offset slightly so its body sits lower on the background
    current_y = line_y + (_s(96) if variant == "edifice" else _s(24))
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

        current_y = draw_rich_text(draw, line, body_font, italic_font, bold_font, bolditalic_font, text_x0, current_y, text_width, _s(22))

    # Variant-specific footer/edifice handling
    variant = (input_data.get("variant") or "").casefold()

    if variant != "edifice":
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
    else:
        # Edifice variant: no footer at bottom; draw number in top-right on the Edifice background
        footer_left = input_data.get('footer_left', '')
        footer_center = input_data.get('footer', '')
        footer_right = input_data.get('footer_right', '')
        footer_y = card_height - _s(45)  # still define for compatibility with helpers
        footer_margin = _s(45)

        draw = ImageDraw.Draw(base_img)
        # Prefer explicit edifice field `edifice_top_right`; fall back to `footer_right` for compatibility
        ed_number = str(input_data.get('edifice_top_right', input_data.get('footer_right', '')))
        if ed_number:
            try:
                num_font_size = input_data.get('ed_number_font_size', 60)
                num_font = ImageFont.truetype(custom_font_path, _s(num_font_size))
            except Exception:
                num_font = footer_font

            num_bbox = draw.textbbox((0, 0), ed_number, font=num_font)
            num_w = num_bbox[2] - num_bbox[0]
            num_h = num_bbox[3] - num_bbox[1]
            # Place near top-right with increased size and padding; no dark background
            padding = _s(96)
            center_x = card_width - padding
            center_y = _s(72)
            # Use bbox bearings so glyphs with different left bearings (e.g. '1') center properly.
            num_x = int(center_x - (num_bbox[0] + num_bbox[2]) / 2)
            num_y = int(center_y - (num_bbox[1] + num_bbox[3]) / 2)
            draw = ImageDraw.Draw(base_img)
            try:
                draw.text((num_x, num_y), ed_number, font=num_font, fill="white", stroke_width=_s(1), stroke_fill="black")
            except TypeError:
                draw.text((num_x, num_y), ed_number, fill="white", font=num_font)

    def _text_width(text: str) -> int:
        bbox = draw.textbbox((0, 0), text, font=footer_font)
        return bbox[2] - bbox[0]

    def _x_centered_like_one_char_left(text: str) -> int:
        # Existing behavior draws at x=footer_margin.
        # Anchor the *center* to where a single character would be centered.
        placeholder = (text or "L")[0]
        single_w = _text_width(placeholder)
        target_center = footer_margin + single_w / 2
        return int(round(target_center - _text_width(text) / 2))

    def _x_centered_like_one_char_right(text: str) -> int:
        # Existing behavior is right-aligned with a small tweak.
        # Anchor the *center* to where a single character would be centered.
        placeholder = "0"
        single_w = _text_width(placeholder)
        right_edge = card_width - footer_margin + _s(2)
        target_center = right_edge - single_w / 2
        return int(round(target_center - _text_width(text) / 2))
    
    # Draw footer texts only for non-edifice variant
    if variant != "edifice":
        # Draw left footer text (black)
        if footer_left:
            x = footer_margin if len(str(footer_left)) <= 1 else _x_centered_like_one_char_left(str(footer_left))
            draw.text((x, footer_y), str(footer_left), fill="black", font=footer_font)
        
        # Draw center footer text (white)
        if footer_center:
            footer_bbox = draw.textbbox((0, 0), footer_center, font=footer_font)
            footer_width = footer_bbox[2] - footer_bbox[0]
            footer_x = (card_width - footer_width) // 2
            draw.text((footer_x, footer_y), footer_center, fill="white", font=footer_font)
        
        # Draw right footer text (black)
        if footer_right:
            footer_right_str = str(footer_right)
            if len(footer_right_str) <= 1:
                footer_x = card_width - footer_margin - _text_width(footer_right_str) + _s(2)
            else:
                footer_x = _x_centered_like_one_char_right(footer_right_str)
            draw.text((footer_x, footer_y), footer_right_str, fill="black", font=footer_font)

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

    # For edifice variant, do not remove bleed by cropping — keep full background intact.
    if variant == "edifice":
        final_img = base_img
    else:
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
        pass

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
        "--last",
        type=int,
        dest="last",
        default=None,
        help="Only generate the last N lore cards from the selected set.",
    )

    parser.add_argument(
        "--number-start",
        type=int,
        dest="number_start",
        default=1,
        help=(
            "Starting number for lore cards. The first lore card in loreCardsFormatted.py will be this number, "
            "the next lore card will be +1, etc. This value is written into footer_right (bottom-right)."
        ),
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        dest="no_numbers",
        help="Do not override footer_right numbering.",
    )

    parser.add_argument(
        "--source-module",
        dest="source_module",
        default=None,
        help="Optional Python module path to import lore_cards from (e.g. scripts.some_lore_module).",
    )

    parser.add_argument(
        "--source-file",
        dest="source_file",
        default=None,
        help="Optional path to a .py file to load lore_cards from.",
    )

    parser.add_argument(
        "--yaml-file",
        dest="yaml_file",
        default=None,
        help="Optional path to a YAML file containing lore cards (list).",
    )

    args = parser.parse_args(argv[1:])

    requested_names = args.names

    # Support loading lore_cards from alternate module/file
    cards_source = lore_cards
    if args.source_module or args.source_file:
        try:
            if args.source_module:
                mod = importlib.import_module(args.source_module)
            else:
                spec = importlib.util.spec_from_file_location("custom_lore_module", args.source_file)
                if spec is None or spec.loader is None:
                    print(f"Error: cannot load source file: {args.source_file}")
                    return 3
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

            if hasattr(mod, "lore_cards"):
                cards_source = getattr(mod, "lore_cards")
            else:
                print("Error: source does not define 'lore_cards'.")
                return 3
        except Exception as e:
            print(f"Failed to import lore cards from source: {e}")
            return 3

    # Allow loading lore cards directly from a YAML file provided on the CLI.
    if args.yaml_file:
        try:
            import yaml as _yaml
        except Exception:
            print("Error: loading YAML requires PyYAML (pip install pyyaml)")
            return 3

        if not os.path.exists(args.yaml_file):
            print(f"Error: YAML file not found: {args.yaml_file}")
            return 3

        try:
            with open(args.yaml_file, encoding="utf-8") as f:
                loaded = _yaml.safe_load(f)
        except Exception as e:
            print(f"Failed to load YAML file {args.yaml_file}: {e}")
            return 3

        if loaded is None or not isinstance(loaded, list):
            print(f"Error: YAML at {args.yaml_file} did not contain a list of cards.")
            return 3

        cards_source = loaded
        print(f"[loreCards] Loaded {len(cards_source)} entries from {args.yaml_file}")

    selected_cards, missing = _select_lore_cards(cards_source, requested_names)

    lore_index_by_name = {c.get("name", "").casefold(): idx for idx, c in enumerate(cards_source)}

    if missing:
        print("Warning: unknown lore name(s): " + ", ".join(missing))

    if args.last is not None:
        if args.last <= 0:
            print("Error: --last must be a positive integer")
            return 2
        if len(selected_cards) > args.last:
            selected_cards = selected_cards[-args.last:]

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

            if not args.no_numbers:
                existing_footer_right = lore_payload.get("footer_right")
                has_explicit_footer_right = existing_footer_right is not None and str(existing_footer_right).strip() != ""

                if not has_explicit_footer_right:
                    idx = lore_index_by_name.get(lore_payload.get("name", "").casefold())
                    if idx is not None:
                        lore_payload["footer_right"] = str(args.number_start + idx)

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
