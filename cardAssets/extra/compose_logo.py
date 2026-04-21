#!/usr/bin/env python3
"""
compose_logo.py

Create a composite image by placing `Planet.png` over
`celestial-nagivation-scaled.jpg`, then placing `Arcs-Logo.PNG` on top.

Defaults assume this file lives in `cardAssets/extra/` alongside the images.

Usage:
    python compose_logo.py
    python compose_logo.py --bg path/to/bg.jpg --planet path/to/Planet.png --logo path/to/Arcs-Logo.PNG --output out.png
"""
import argparse
import io
import os

from PIL import Image, ImageDraw, ImageFont


def load_rgba(path):
    return Image.open(path).convert("RGBA")


def resize_to_width(im, width):
    w, h = im.size
    if w == width:
        return im
    new_h = int(h * (width / float(w)))
    return im.resize((int(width), new_h), Image.LANCZOS)


def parse_offset(text):
    if isinstance(text, tuple):
        return text
    try:
        parts = text.split(",")
        x = int(parts[0].strip())
        y = int(parts[1].strip())
        return x, y
    except Exception:
        raise argparse.ArgumentTypeError("offset must be 'x,y' with integer values")


def compute_position(base_size, layer_size, alignment, offset=(0, 0)):
    bw, bh = base_size
    lw, lh = layer_size
    if alignment == "center":
        x = (bw - lw) // 2
        y = (bh - lh) // 2
    elif alignment == "top-left":
        x, y = 0, 0
    elif alignment == "top-right":
        x, y = bw - lw, 0
    elif alignment == "bottom-left":
        x, y = 0, bh - lh
    elif alignment == "bottom-right":
        x, y = bw - lw, bh - lh
    elif alignment == "custom":
        # For custom, offset is treated as absolute position
        x, y = offset
        return x, y
    else:
        x = (bw - lw) // 2
        y = (bh - lh) // 2

    dx, dy = offset
    return x + dx, y + dy


def paste_with_alignment(base, layer, alignment="center", offset=(0, 0)):
    pos = compute_position(base.size, layer.size, alignment, offset)
    base.paste(layer, pos, layer)


def _flatten_for_jpeg(im, background=(255, 255, 255)):
    """Return an RGB image suitable for JPEG (no alpha)."""
    if im.mode in ("RGBA", "LA") or ("A" in im.getbands()):
        alpha = im.split()[-1]
        bg = Image.new("RGB", im.size, background)
        bg.paste(im.convert("RGBA"), mask=alpha)
        return bg
    return im.convert("RGB")


def _find_best_jpeg_quality(img, target_bytes, min_q=20, max_q=95):
    """Binary-search JPEG quality to get file <= target_bytes; returns (quality, bytes)."""
    # quick check at max quality
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=max_q, optimize=True)
    data = buf.getvalue()
    if len(data) <= target_bytes:
        # If the max-quality result is much smaller than the target, try a maximal-entropy save
        if len(data) < int(target_bytes * 0.9):
            # try quality=100, no subsampling, no optimize to increase file size
            buf2 = io.BytesIO()
            try:
                img.save(buf2, format="JPEG", quality=100, subsampling=0, optimize=False)
                data2 = buf2.getvalue()
                if data2 <= target_bytes and data2 > len(data):
                    return 100, data2
                # if data2 is still less than target but larger than previous, prefer it
                if len(data2) > len(data):
                    return 100, data2
            except Exception:
                pass
        return max_q, data

    lo, hi = min_q, max_q
    best = None
    while lo <= hi:
        mid = (lo + hi) // 2
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=mid, optimize=True)
        data = buf.getvalue()
        size = len(data)
        if size <= target_bytes:
            best = (mid, data)
            lo = mid + 1
        else:
            hi = mid - 1

    if best:
        return best
    # fallback: return lowest quality available
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=min_q, optimize=True)
    return min_q, buf.getvalue()


def _maximal_jpeg_bytes(img):
    """Return bytes for a near-maximal JPEG encoding (quality=100, no subsampling)."""
    buf = io.BytesIO()
    try:
        img.save(buf, format="JPEG", quality=100, subsampling=0, optimize=False)
        return buf.getvalue()
    except Exception:
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=95, optimize=True)
        return buf.getvalue()


def make_compressed_version(img, original_path, max_size_kb=2000, suffix="_compressed"):
    """Save a JPEG version of `img` that is <= max_size_kb kilobytes.

    Returns the path of the compressed file or None on failure.
    """
    target = int(max_size_kb * 1024)
    flat = _flatten_for_jpeg(img)
    quality, data = _find_best_jpeg_quality(flat, target)
    base, _ext = os.path.splitext(original_path)
    out_path = f"{base}{suffix}.jpg"
    try:
        with open(out_path, "wb") as f:
            f.write(data)
        return out_path
    except Exception:
        return None


# In-file configuration: edit these values to set defaults without using CLI
CONFIG = {
    "paths": {
        "bg": "celestial-nagivation-scaled.jpg",
        "planet": "Planet.png",
        "logo": "Arcs-Logo.PNG",
        "believer": "Believer.png",
        "output": "composed.png",
    },
    # if True, crop the longer background dimension centered to make a square
    "crop_square": True,
    "planet": {
        "scale":1,
        "width": None,
        "pos": "center",
        "offset": (0, 0),
    },
    "logo": {
        "scale": 1,
        "width": None,
        "pos": "center",
        "offset": (0, -200),
    },
        "believer": {
            "enabled": True,
            "scale": 0.25,
            "width": None,
            "pos": "top-right",
            "offset": (80, -30),
            "rotate": 55.0,
        },
    "text": {
        # set to empty string to disable by default
        "content": "Celestial Edition",
        # relative path from repo root: adjust if your fonts live elsewhere
        "font": os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "fonts", "FMBolyarPro-900.ttf")),
        # font size as fraction of background width (used if font_size not set)
        "size_ratio": 0.08,
        "size": None,
        "color": "#FFFFFF",
        "stroke_color": "#000000",
        "stroke_width": 0,
        "pos": "center",
        "offset": (-10, 200),
    },
}


def main():
    script_dir = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(description="Compose images: bg <- planet <- logo")
    parser.add_argument("--bg", default=os.path.join(script_dir, CONFIG["paths"]["bg"]), help="Background image path")
    parser.add_argument("--planet", default=os.path.join(script_dir, CONFIG["paths"]["planet"]), help="Planet image path")
    parser.add_argument("--logo", default=os.path.join(script_dir, CONFIG["paths"]["logo"]), help="Logo image path")
    parser.add_argument("--output", default=os.path.join(script_dir, CONFIG["paths"]["output"]), help="Output path")

    # planet sizing and placement (defaults come from CONFIG)
    parser.add_argument("--planet-scale", type=float, default=CONFIG["planet"]["scale"], help="Planet width as fraction of background width (0-1)")
    parser.add_argument("--planet-width", type=int, default=CONFIG["planet"]["width"], help="Planet width in pixels (overrides --planet-scale)")
    parser.add_argument("--planet-pos", choices=["center", "top-left", "top-right", "bottom-left", "bottom-right", "custom"], default=CONFIG["planet"]["pos"], help="Planet alignment on the background")
    parser.add_argument("--planet-offset", type=parse_offset, default=CONFIG["planet"]["offset"], help="Planet offset as 'x,y' (pixels). For 'custom' alignment this is absolute position")

    # logo sizing and placement (defaults come from CONFIG)
    parser.add_argument("--logo-scale", type=float, default=CONFIG["logo"]["scale"], help="Logo width as fraction of background width (0-1)")
    parser.add_argument("--logo-width", type=int, default=CONFIG["logo"]["width"], help="Logo width in pixels (overrides --logo-scale)")
    parser.add_argument("--logo-pos", choices=["center", "top-left", "top-right", "bottom-left", "bottom-right", "custom"], default=CONFIG["logo"]["pos"], help="Logo alignment on the background")
    parser.add_argument("--logo-offset", type=parse_offset, default=CONFIG["logo"]["offset"], help="Logo offset as 'x,y' (pixels). For 'custom' alignment this is absolute position")

    # believer layer options
    parser.add_argument("--believer-enable", action="store_true", default=CONFIG["believer"]["enabled"], help="Enable pasting the believer image")
    parser.add_argument("--believer", default=os.path.join(script_dir, CONFIG["paths"]["believer"]), help="Believer image path")
    parser.add_argument("--believer-scale", type=float, default=CONFIG["believer"]["scale"], help="Believer width as fraction of background width (0-1)")
    parser.add_argument("--believer-width", type=int, default=CONFIG["believer"]["width"], help="Believer width in pixels (overrides --believer-scale)")
    parser.add_argument("--believer-pos", choices=["center", "top-left", "top-right", "bottom-left", "bottom-right", "custom"], default=CONFIG["believer"]["pos"], help="Believer alignment on the background")
    parser.add_argument("--believer-offset", type=parse_offset, default=CONFIG["believer"]["offset"], help="Believer offset as 'x,y' (pixels). For 'custom' alignment this is absolute position")
    parser.add_argument("--believer-rotate", type=float, default=CONFIG["believer"]["rotate"], help="Rotation angle for believer layer (degrees, clockwise)")

    # text options
    parser.add_argument("--text", default=CONFIG["text"]["content"], help="Text to render on the image (empty disables)")
    parser.add_argument("--font", default=CONFIG["text"]["font"], help="Path to TTF font file")
    parser.add_argument("--font-size", type=int, default=CONFIG["text"]["size"], help="Font size in pixels (overrides font-size-ratio)")
    parser.add_argument("--font-size-ratio", type=float, default=CONFIG["text"]["size_ratio"], help="Font size as fraction of background width")
    parser.add_argument("--font-color", default=CONFIG["text"]["color"], help="Font color")
    parser.add_argument("--stroke-color", default=CONFIG["text"]["stroke_color"], help="Stroke color for text")
    parser.add_argument("--stroke-width", type=int, default=CONFIG["text"]["stroke_width"], help="Stroke width for text (0 disables outline)")
    parser.add_argument("--text-pos", choices=["center", "top-left", "top-right", "bottom-left", "bottom-right", "custom"], default=CONFIG["text"]["pos"], help="Text alignment on the background")
    parser.add_argument("--text-offset", type=parse_offset, default=CONFIG["text"]["offset"], help="Text offset as 'x,y' (pixels). For 'custom' alignment this is absolute position")
    parser.add_argument("--max-size-kb", type=int, default=2000, help="Maximum size (KB) for compressed output")
    parser.add_argument("--compressed-suffix", default="_compressed", help="Suffix for compressed output file")

    args = parser.parse_args()

    bg = load_rgba(args.bg)
    # Optionally crop background to square by trimming the longer dimension centered
    if CONFIG.get("crop_square"):
        bw, bh = bg.size
        if bw > bh:
            new_w = bh
            left = (bw - new_w) // 2
            right = left + new_w
            bg = bg.crop((left, 0, right, bh))
        elif bh > bw:
            new_h = bw
            top = (bh - new_h) // 2
            bottom = top + new_h
            bg = bg.crop((0, top, bw, bottom))
    planet = load_rgba(args.planet)
    logo = load_rgba(args.logo)

    # Resize planet and logo relative to background width or explicit pixel widths
    if args.planet_width and args.planet_width > 0:
        planet = resize_to_width(planet, args.planet_width)
    elif 0 < args.planet_scale <= 1:
        new_w = int(bg.width * args.planet_scale)
        planet = resize_to_width(planet, new_w)

    if args.logo_width and args.logo_width > 0:
        logo = resize_to_width(logo, args.logo_width)
    elif 0 < args.logo_scale <= 1:
        new_w = int(bg.width * args.logo_scale)
        logo = resize_to_width(logo, new_w)

    believer = None
    if args.believer_enable:
        try:
            believer = load_rgba(args.believer)
        except Exception:
            believer = None

    if believer is not None:
        if args.believer_width and args.believer_width > 0:
            believer = resize_to_width(believer, args.believer_width)
        elif 0 < args.believer_scale <= 1:
            new_w = int(bg.width * args.believer_scale)
            believer = resize_to_width(believer, new_w)

        # apply rotation (Pillow rotates counter-clockwise for positive angles,
        # we negate to treat input as clockwise as documented)
        if args.believer_rotate:
            believer = believer.rotate(-float(args.believer_rotate), expand=True)

    out = bg.copy().convert("RGBA")

    # paste believer below the planet (so planet sits on top of believer)
    if believer is not None:
        paste_with_alignment(out, believer, alignment=args.believer_pos, offset=args.believer_offset)

    paste_with_alignment(out, planet, alignment=args.planet_pos, offset=args.planet_offset)
    paste_with_alignment(out, logo, alignment=args.logo_pos, offset=args.logo_offset)

    # Draw text if requested
    if args.text:
        draw = ImageDraw.Draw(out)
        # determine font size
        if args.font_size and args.font_size > 0:
            fsize = args.font_size
        else:
            fsize = int(out.width * args.font_size_ratio) if args.font_size_ratio and args.font_size_ratio > 0 else 40
        try:
            font = ImageFont.truetype(args.font, fsize)
        except Exception:
            font = ImageFont.load_default()

        # measure text
        try:
            bbox = draw.textbbox((0, 0), args.text, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
        except Exception:
            tw, th = draw.textsize(args.text, font=font)

        # compute position using same compute_position helper
        tx, ty = compute_position(out.size, (tw, th), args.text_pos, args.text_offset)

        # draw stroke then text for readability
        draw.text((tx, ty), args.text, font=font, fill=args.font_color, stroke_width=args.stroke_width, stroke_fill=args.stroke_color)

    # Ensure parent dir exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    out.save(args.output)
    print(f"Saved composite to {args.output}")

    # create a compressed JPEG below target size (if requested)
    if args.max_size_kb and args.max_size_kb > 0:
        comp = make_compressed_version(out, args.output, max_size_kb=args.max_size_kb, suffix=args.compressed_suffix)
        if comp:
            size_kb = os.path.getsize(comp) / 1024.0
            print(f"Saved compressed version to {comp} ({size_kb:.1f} KB)")
        else:
            print("Failed to create compressed version")


if __name__ == "__main__":
    main()
