import os

from loreCardsFormatted import lore_cards
from PIL import Image, ImageDraw, ImageFont


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

    # Load the lore frame to get card dimensions
    lore_frame = Image.open(lore_frame_path).convert("RGBA")
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
        
        lore_img = lore_img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        # Position at top left (full width)
        lore_x = 0
        lore_y = 0
        
        base_img.paste(lore_img, (lore_x, lore_y), lore_img)
        
    except FileNotFoundError:
        print(f"Warning: Lore image '{input_data['name']}.png' not found in loreImages folder. Proceeding without image.")

    # Paste the lore frame on top
    base_img.paste(lore_frame, (0, 0), lore_frame)

    # Create drawing context
    draw = ImageDraw.Draw(base_img)

    # Load fonts
    try:
        title_font = ImageFont.truetype(custom_font_path, 25)
        footer_font = ImageFont.truetype(custom_font_path, input_data.get("footer_font_size", 14))
        body_font = ImageFont.truetype(neue_kabel_font_path, input_data.get("body_font_size", 18))
        italic_font = ImageFont.truetype(neue_kabel_italic_path, input_data.get("body_font_size", 18))
        bold_font = ImageFont.truetype(neue_kabel_bold_path, input_data.get("body_font_size", 18))
        bolditalic_font = ImageFont.truetype(neue_kabel_bolditalic_path, input_data.get("body_font_size", 18))
    except IOError as e:
        print(f"Font loading error: {e}")
        title_font = body_font = italic_font = bold_font = bolditalic_font = footer_font = ImageFont.load_default()

    # Text area dimensions (adjust these based on the lore frame layout)
    text_margin = 40
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
    line_y = title_y + (title_bbox[3] - title_bbox[1]) + 12

    # Text wrapping function
    def wrap_text(text, font, max_width):
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
                word_width = draw.textbbox((0, 0), word, font=font)[2]
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
        line_height = line_height * (input_data.get("body_font_size", 18) / 18)
        words = text.split(" ")
        current_x = x
        current_y = y

        for word in words:
            font_to_use = font
            text_to_draw = word

            if word.startswith("***") and word.endswith("***") and len(word) > 6:
                text_to_draw = word[3:-3]
                font_to_use = bolditalic_font
                adjust_y = 4
            elif word.startswith("**") and word.endswith("**") and len(word) > 4:
                text_to_draw = word[2:-2]
                font_to_use = bold_font
                adjust_y = 4
            elif word.startswith("*") and word.endswith("*") and len(word) > 2:
                text_to_draw = word[1:-1]
                font_to_use = italic_font
                adjust_y = 3
            else:
                adjust_y = 0

            word_bbox = draw.textbbox((0, 0), text_to_draw, font=font_to_use)
            word_width = word_bbox[2] - word_bbox[0]
            draw.text((current_x, current_y + adjust_y), text_to_draw, font=font_to_use, fill="black")
            space_width = draw.textbbox((0, 0), " ", font=font)[2]
            current_x += word_width + space_width

        return current_y + line_height

    # Draw body text
    body_text = input_data.get('body', '')
    current_y = line_y + 18
    for line in wrap_text(body_text, body_font, text_width):
        if not line.strip():
            current_y += 10
            continue
        current_y = draw_rich_text(draw, line, body_font, italic_font, bold_font, bolditalic_font, text_x0, current_y, text_width, 22)

    # Load and paste footer image on top of everything
    try:
        footer_img = Image.open(footer_image_path).convert("RGBA")
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
    
    footer_y = card_height - 45  # Position near bottom
    footer_margin = 45  # Margin from edges
    
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
        footer_x = card_width - footer_margin - footer_width + 5
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
    final_img.save(output_image_path)
    print(f"Lore card saved at {output_image_path}")
    
    return output_image_path


def generate_all_lore_cards():
    """Generate all lore cards defined in the lore_cards list."""
    for lore_card in lore_cards:
        try:
            create_lore_card(lore_card)
        except Exception as e:
            print(f"Error generating lore card '{lore_card.get('name', 'Unknown')}': {e}")


if __name__ == "__main__":
    generate_all_lore_cards()
