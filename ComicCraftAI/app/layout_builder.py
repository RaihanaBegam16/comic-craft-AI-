from PIL import Image, ImageDraw, ImageFont
import os

from .config import EXPORTS_DIR


def build_comic_page(panel_paths):

    print("Building final comic page...")

    canvas_width = 1440
    canvas_height = 900

    canvas = Image.new(
        "RGB",
        (canvas_width, canvas_height),
        "white"
    )

    draw = ImageDraw.Draw(canvas)

    # -------------------------
    # PANEL POSITIONS
    # -------------------------

    positions = [
        (30, 30),
        (750, 30),
        (30, 460),
        (750, 460),
        (390, 245)
    ]

    panel_width = 660
    panel_height = 390

    # -------------------------
    # ADD PANELS
    # -------------------------

    for index, panel_path in enumerate(panel_paths):

        if not os.path.exists(panel_path):
            print(
                f"Panel not found: {panel_path}"
            )
            continue

        image = Image.open(
            panel_path
        ).convert("RGB")

        image.thumbnail(
            (
                panel_width,
                panel_height
            )
        )

        x, y = positions[index]

        # Center image
        paste_x = (
            x +
            (panel_width - image.width) // 2
        )

        paste_y = (
            y +
            (panel_height - image.height) // 2
        )

        canvas.paste(
            image,
            (paste_x, paste_y)
        )

        # Border
        draw.rectangle(
            [
                x,
                y,
                x + panel_width,
                y + panel_height
            ],
            outline="black",
            width=5
        )

        # -------------------------
        # PANEL LABEL
        # -------------------------

        try:

            font = ImageFont.truetype(
                "arial.ttf",
                24
            )

        except:

            font = ImageFont.load_default()

        draw.rounded_rectangle(
            [
                x + 15,
                y + 15,
                x + 150,
                y + 55
            ],
            radius=10,
            fill=(25, 35, 45)
        )

        draw.text(
            [
                x + 30,
                y + 25
            ],
            f"PANEL {index + 1}",
            fill="white",
            font=font
        )

    # -------------------------
    # SAVE FINAL COMIC
    # -------------------------

    os.makedirs(
        EXPORTS_DIR,
        exist_ok=True
    )

    output_path = os.path.join(
        EXPORTS_DIR,
        "comic_page.png"
    )

    canvas.save(
        output_path
    )

    print(
        f"Comic page created: {output_path}"
    )

    return output_path