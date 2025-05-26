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

    script_path = os.path.join(base_path, "scripts")
    result_path = os.path.join(base_path, "results")

    leader_image_path = os.path.join(base_path, "cardAssets","CardAssets-Tarot-Leader.png")
    text_box_image_path = os.path.join(base_path, "cardAssets","CardAssets-Tarot-Fate-Text-Box.png")

    resource_fuel_path = os.path.join(base_path, "icon and punchboard", "arcs dev_icon resource fuel.png")
    resource_material_path = os.path.join(base_path, "icon and punchboard", "arcs dev_icon resource material.png")
    resource_psionic_path = os.path.join(base_path, "icon and punchboard", "arcs dev_icon resource psionic.png")
    resource_relic_path = os.path.join(base_path, "icon and punchboard", "arcs dev_icon resource relic.png")
    resource_weapon_path = os.path.join(base_path, "icon and punchboard", "arcs dev_icon resource weapon.png")

    box_a_image_front_path = os.path.join(base_path, "icon and punchboard", "arcs dev_player piece white starport.png")
    box_a_image_back_path = os.path.join(base_path, "icon and punchboard", "arcs dev_player piece white starport back.png")
    box_b_image_front_path = os.path.join(base_path, "icon and punchboard", "arcs dev_player piece white city.png")
    box_b_image_back_path = os.path.join(base_path, "icon and punchboard", "arcs dev_player piece white city back.png")

    output_image_path = os.path.join(result_path, f"{input_data['name']}_Card.png")

    base_img = Image.open(leader_image_path).convert("RGBA")
    text_box_img = Image.open(text_box_image_path).convert("RGBA")

    resource_size = (50, 50)
    new_size = (int(resource_size[0] * 0.75), int(resource_size[1] * 0.75))
    r_new_size = (int(resource_size[0] * 0.55), int(resource_size[1] * 0.55))

    def load_and_resize(path):
        return Image.open(path).convert("RGBA").resize(r_new_size)

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

    text_box_x = (base_img.width - text_box_img.width) // 2
    text_box_y = base_img.height - text_box_img.height
    combined_img = base_img.copy()
    combined_img.paste(text_box_img, (text_box_x, text_box_y), text_box_img)

    draw = ImageDraw.Draw(combined_img)

    try:
        title_font = ImageFont.truetype(custom_font_path, 25)
        body_font = ImageFont.truetype(neue_kabel_font_path, input_data.get("body_font_size", 18))
        italic_font = ImageFont.truetype(neue_kabel_italic_path, input_data.get("body_font_size", 18))
        bold_font = ImageFont.truetype(neue_kabel_bold_path, input_data.get("body_font_size", 18))
        bolditalic_font = ImageFont.truetype(neue_kabel_bolditalic_path, input_data.get("body_font_size", 18))
        box_label_font = ImageFont.truetype(neue_kabel_font_path, 12)
        box_number_font = ImageFont.truetype(neue_kabel_font_path, 14)
        big_box_number_font = ImageFont.truetype(neue_kabel_font_path, 24)
    except IOError:
        title_font = body_font = italic_font = bold_font = bolditalic_font = box_label_font = box_number_font = big_box_number_font = ImageFont.load_default()

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
        line_height = line_height * (input_data.get("body_font_size", 18) / 18)  # Adjust the line height based on font size

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
        current_y = draw_rich_text(
            draw, line,
            font=body_font,
            italic_font=italic_font,
            bold_font=bold_font,
            bolditalic_font=bolditalic_font,
            x=text_x0,
            y=current_y,
            max_width=text_width,
            line_height=22
        )

    circle_radius = int(new_size[0] * 1.25 / 2)
    resource_x = 80
    resource_y = combined_img.height - new_size[1] - 35
    resource_x2 = resource_x + new_size[0] + 15

    for x, res in zip([resource_x, resource_x2], [resource_1, resource_2]):
        draw.ellipse([x - circle_radius, resource_y - circle_radius, x + circle_radius, resource_y + circle_radius], outline="black", width=1)
        combined_img.paste(res, (x - r_new_size[0] // 2, resource_y - r_new_size[1] // 2), res)

    box_width = 80
    box_height = circle_radius * 2
    box_c_size = circle_radius * 2
    box_a_x = resource_x2 + new_size[0] + 5
    box_b_x = box_a_x + box_width + 5
    box_c_x = box_b_x + box_width + 5
    box_y = resource_y - circle_radius

    def select_box_image(setup):
        building = setup["building"]
        damaged = setup["damaged"]
        if building == "city":
            return box_b_image_back_path if damaged else box_b_image_front_path
        elif building == "starport":
            return box_a_image_back_path if damaged else box_a_image_front_path
        elif building == "None":
            return os.path.join(base_path, "icon and punchboard", "empty_151x135.png")
        return None

    def resize_to_fit_box(image, box_w, box_h):
        ratio = min(box_w / image.width, box_h / image.height)
        return image.resize((int(image.width * ratio), int(image.height * ratio)))

    def reverse_colors(image):
        """Reverses the colors of the image"""
        image = image.convert("RGB")
        inverted_image = Image.eval(image, lambda x: 255 - x)
        return inverted_image.convert("RGBA")

    box_a_img = reverse_colors(Image.open(select_box_image(input_data['setup']['A'])).convert("RGBA"))
    box_b_img = reverse_colors(Image.open(select_box_image(input_data['setup']['B'])).convert("RGBA"))

    box_a_img = resize_to_fit_box(box_a_img, box_width - 10, box_height - 10)
    box_b_img = resize_to_fit_box(box_b_img, box_width - 10, box_height - 10)

    combined_img.paste(box_a_img, (box_a_x + 5, box_y + 5), box_a_img)
    combined_img.paste(box_b_img, (box_b_x + 5, box_y + 5), box_b_img)
    draw.rectangle([box_a_x, box_y, box_a_x + box_width, box_y + box_height], outline="black", width=1)
    draw.rectangle([box_b_x, box_y, box_b_x + box_width, box_y + box_height], outline="black", width=1)
    draw.rectangle([box_c_x, box_y, box_c_x + box_c_size, box_y + box_c_size], outline="black", width=1)

    draw.text((box_a_x + 4, box_y + 4), "A", font=box_label_font, fill="black")
    draw.text((box_b_x + 4, box_y + 4), "B", font=box_label_font, fill="black")
    draw.text((box_c_x + 4, box_y + 4), "C", font=box_label_font, fill="black")

    def draw_box_number(box_x, box_y, box_w, box_h, number, adjust_left=False):
        text_width = draw.textbbox((0, 0), number, font=big_box_number_font)[2]
        x = box_x + (box_w - text_width) // 2 + 15
        if adjust_left:
            x -= 15
        y = box_y + (box_h - 20) // 2
        draw.text((x, y), number, fill="black", font=big_box_number_font)

    draw_box_number(box_a_x, box_y, box_width, box_height, str(input_data['setup']['A']['ships']))
    draw_box_number(box_b_x, box_y, box_width, box_height, str(input_data['setup']['B']['ships']))
    draw_box_number(box_c_x, box_y, box_c_size, box_c_size, str(input_data['setup']['C']['ships']), adjust_left=True)
    
    def final_crop(image, bleed_mm=3, card_width_mm=70, card_height_mm=120):
        width, height = image.size

        # Calculate the % of the bleed relative to final card size
        left = int((bleed_mm / card_width_mm) * width)
        top = int((bleed_mm / card_height_mm) * height)
        right = width - left
        bottom = height - top

        return image.crop((left, top, right, bottom))


    combined_img = final_crop(combined_img, bleed_mm=3, card_width_mm=70, card_height_mm=120)

    combined_img.save(output_image_path)
    print(f"Combined image saved at {output_image_path}")
    

