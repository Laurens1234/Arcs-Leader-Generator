import os

from PIL import Image, ImageDraw, ImageFont


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

    base_img = Image.open(leader_image_path).convert("RGBA")
    text_box_img = Image.open(text_box_image_path).convert("RGBA")

    leader_image_overlay_path = os.path.join(base_path, "cardAssets", "leaderImages", f"{input_data['name']}.png")

    try:
        overlay_img = Image.open(leader_image_overlay_path).convert("RGBA")
        
        overlay_width = base_img.width // 2
        aspect_ratio = overlay_img.height / overlay_img.width
        overlay_height = int(overlay_width * aspect_ratio)
        overlay_img = overlay_img.resize((overlay_width, overlay_height))
        
        overlay_x = (base_img.width - overlay_img.width) // 2 
        overlay_y = 390 - overlay_img.height  

        base_img.paste(overlay_img, (overlay_x, overlay_y), overlay_img)

    except FileNotFoundError:
        print(f"Warning: Overlay image '{input_data['name']}.png' not found. Proceeding without overlay.")


    # Resize resource images
    resource_size = (55, 55)

    def load_and_resize(path):
        return Image.open(path).convert("RGBA").resize(resource_size)

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
        title_font = ImageFont.truetype(custom_font_path, 25)
        body_font = ImageFont.truetype(neue_kabel_font_path, input_data.get("body_font_size", 18))
        italic_font = ImageFont.truetype(neue_kabel_italic_path, input_data.get("body_font_size", 18))
        bold_font = ImageFont.truetype(neue_kabel_bold_path, input_data.get("body_font_size", 18))
        bolditalic_font = ImageFont.truetype(neue_kabel_bolditalic_path, input_data.get("body_font_size", 18))
    except IOError:
        title_font = body_font = italic_font = bold_font = bolditalic_font = ImageFont.load_default()

    # Setup images resize while keeping aspect ratio
    def get_setup_image_path(slot, setup_data):
        building = setup_data["building"]
        ships = setup_data["ships"]
        building_str = building.lower() if building.lower() != "none" else "none"
        file_name = f"{slot}-{building_str}-{ships}ships.png"
        return os.path.join(base_path, "cardAssets", "captured", file_name)

    setup_image_size = (50, 50)

    def load_and_resize_setup(path):
        img = Image.open(path).convert("RGBA")
        width, height = img.size
        aspect_ratio = height / width
        new_height = 50
        new_width = int(new_height / aspect_ratio)
        return img.resize((new_width, new_height))

    setup_data = input_data["setup"]
    setup_a_img = load_and_resize_setup(get_setup_image_path("A", setup_data["A"]))
    setup_b_img = load_and_resize_setup(get_setup_image_path("B", setup_data["B"]))
    setup_c_img = load_and_resize_setup(get_setup_image_path("C", setup_data["C"]))

    setup_a_building = setup_data["A"]["building"].lower() != "none"
    setup_b_building = setup_data["B"]["building"].lower() != "none"
    
    # Paste resources
    resource_x = 100
    resource_y = combined_img.height - resource_size[1] - 22
    resource_x2 = resource_x + resource_size[0] + 5
    
    setup_start_x = resource_x2 + resource_size[0] - 20
    setup_y = resource_y - setup_image_size[1] // 2
    setup_spacing = 25

    if not setup_a_building and not setup_b_building:
        for x, res in zip([resource_x + 20, resource_x2 + 20], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)
        combined_img.paste(setup_a_img, (setup_start_x + 20, setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing - 10, setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing) - 40, setup_y), setup_c_img)
    elif not setup_a_building:
        for x, res in zip([resource_x + 10 , resource_x2 + 10], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)        
        combined_img.paste(setup_a_img, (setup_start_x + 10 , setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing-20, setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing)-20, setup_y), setup_c_img)
    elif not setup_b_building:
        for x, res in zip([resource_x + 10, resource_x2 + 10], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)
        combined_img.paste(setup_a_img, (setup_start_x + 10, setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing + 12, setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing) - 20, setup_y), setup_c_img)
    else:
        for x, res in zip([resource_x, resource_x2], [resource_1, resource_2]):
            combined_img.paste(res, (x - resource_size[0] // 2, resource_y - resource_size[1] // 2), res)
        combined_img.paste(setup_a_img, (setup_start_x, setup_y), setup_a_img)
        combined_img.paste(setup_b_img, (setup_start_x + setup_image_size[0] + setup_spacing +1, setup_y), setup_b_img)
        combined_img.paste(setup_c_img, (setup_start_x + 2 * (setup_image_size[0] + setup_spacing), setup_y), setup_c_img)


    # Title and abilities
    title_text = input_data['name']
    body_text = input_data['abilities']

    text_x0, text_y0 = 60, 390
    text_x1, text_y1 = 390, 645
    text_width = text_x1 - text_x0

    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_x = text_x0 + (text_width - (title_bbox[2] - title_bbox[0])) // 2
    title_y = text_y0
    draw.text((title_x, title_y), title_text, fill="black", font=title_font)

    line_y = title_y + (title_bbox[3] - title_bbox[1]) + 12
    draw.line((text_x0, line_y, text_x1, line_y), fill="black", width=3)

    # Text wrapping and rich text rendering
    def wrap_text(text, font, max_width):
        paragraphs = text.split('\n')
        wrapped_lines = []
        for para in paragraphs:
            if not para.strip():
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

    current_y = line_y + 10
    for line in wrap_text(body_text, body_font, text_width):
        if not line.strip():
            current_y += 10
            continue
        current_y = draw_rich_text(draw, line, body_font, italic_font, bold_font, bolditalic_font, text_x0, current_y, text_width, 22)

    # Final crop
    def final_crop(image, bleed_mm=3, card_width_mm=70, card_height_mm=120):
        width, height = image.size
        left = int((bleed_mm / card_width_mm) * width)
        top = int((bleed_mm / card_height_mm) * height)
        right = width - left
        bottom = height - top
        return image.crop((left, top, right, bottom))

    combined_img = final_crop(combined_img)
    combined_img.save(output_image_path)
    print(f"Combined image saved at {output_image_path}")
