from PIL import Image, ImageDraw, ImageFont
import os
import math


# ============================================================
# SETTINGS
# ============================================================

WIDTH = 1024
HEIGHT = 650


# ============================================================
# FONT SYSTEM
# ============================================================

FONT_DIR = r"C:\Windows\Fonts"


def get_font(font_name, size):
    """
    Loads Windows font safely.
    If the requested font is not available,
    it automatically uses Arial.
    """

    possible_fonts = [
        os.path.join(FONT_DIR, font_name),
        os.path.join(FONT_DIR, "arial.ttf"),
    ]

    for font_path in possible_fonts:
        if os.path.exists(font_path):
            return ImageFont.truetype(font_path, size)

    return ImageFont.load_default()


# Different font for every panel
PANEL_FONTS = [
    ("segoeuib.ttf", 30),
    ("georgiab.ttf", 30),
    ("comicbd.ttf", 30),
    ("calibrib.ttf", 30),
    ("timesbd.ttf", 30),
]


# ============================================================
# TEXT
# ============================================================

PANEL_TEXT = [
    "A brave fox entered the enchanted forest...",
    "Suddenly, a mysterious light appeared!",
    "The fox followed the glowing path.",
    "Deep inside the forest, a magical secret waited.",
    "The brave fox discovered the heart of the forest!"
]


# ============================================================
# CREATE CLOUD
# ============================================================

def draw_cloud(draw, x, y, scale=1.0):

    white = "#EAF8FF"

    draw.ellipse(
        [
            x,
            y + int(25 * scale),
            x + int(100 * scale),
            y + int(75 * scale)
        ],
        fill=white
    )

    draw.ellipse(
        [
            x + int(25 * scale),
            y,
            x + int(105 * scale),
            y + int(65 * scale)
        ],
        fill=white
    )

    draw.ellipse(
        [
            x + int(75 * scale),
            y + int(20 * scale),
            x + int(155 * scale),
            y + int(75 * scale)
        ],
        fill=white
    )


# ============================================================
# CREATE TREE
# ============================================================

def draw_tree(draw, x, y, size):

    trunk_color = "#315B43"
    leaf_color = "#126B4B"

    draw.rectangle(
        [
            x - int(size * 0.10),
            y,
            x + int(size * 0.10),
            y + int(size * 0.90)
        ],
        fill=trunk_color
    )

    draw.ellipse(
        [
            x - int(size * 0.55),
            y - int(size * 0.55),
            x + int(size * 0.55),
            y + int(size * 0.35)
        ],
        fill=leaf_color
    )

    draw.ellipse(
        [
            x - int(size * 0.40),
            y - int(size * 0.85),
            x + int(size * 0.40),
            y + int(size * 0.15)
        ],
        fill=leaf_color
    )


# ============================================================
# CREATE PINE TREE
# ============================================================

def draw_pine(draw, x, y, height):

    color = "#087C73"

    draw.polygon(
        [
            (x, y - height),
            (x - height * 0.20, y - height * 0.55),
            (x - height * 0.08, y - height * 0.55),

            (x - height * 0.32, y - height * 0.20),
            (x - height * 0.10, y - height * 0.20),

            (x - height * 0.42, y),

            (x + height * 0.42, y),

            (x + height * 0.10, y - height * 0.20),
            (x + height * 0.32, y - height * 0.20),

            (x + height * 0.08, y - height * 0.55),
            (x + height * 0.20, y - height * 0.55),
        ],
        fill=color
    )


# ============================================================
# DRAW SUN
# ============================================================

def draw_sun(draw, x, y, radius):

    draw.ellipse(
        [
            x - radius,
            y - radius,
            x + radius,
            y + radius
        ],
        fill="#FFD66B"
    )

    for angle in range(0, 360, 20):

        rad = math.radians(angle)

        x1 = x + math.cos(rad) * (radius + 20)
        y1 = y + math.sin(rad) * (radius + 20)

        x2 = x + math.cos(rad) * (radius + 55)
        y2 = y + math.sin(rad) * (radius + 55)

        draw.line(
            [x1, y1, x2, y2],
            fill="#BEEFFF",
            width=3
        )


# ============================================================
# DRAW FOX
# ============================================================

def draw_fox(draw, panel_number):

    # Position changes slightly in every panel
    positions = [
        (500, 230),
        (440, 250),
        (520, 240),
        (450, 250),
        (520, 235)
    ]

    cx, cy = positions[panel_number - 1]

    # --------------------------------------------------------
    # TAIL
    # --------------------------------------------------------

    draw.ellipse(
        [
            cx - 210,
            cy + 190,
            cx + 80,
            cy + 350
        ],
        fill="#D87852",
        outline="#A94E3C",
        width=6
    )

    # White tail tip
    draw.ellipse(
        [
            cx - 205,
            cy + 195,
            cx - 85,
            cy + 320
        ],
        fill="#F5F5F5"
    )

    # --------------------------------------------------------
    # BODY
    # --------------------------------------------------------

    draw.ellipse(
        [
            cx - 80,
            cy + 40,
            cx + 180,
            cy + 390
        ],
        fill="#D87852",
        outline="#A94E3C",
        width=6
    )

    # --------------------------------------------------------
    # WHITE BELLY
    # --------------------------------------------------------

    draw.ellipse(
        [
            cx - 25,
            cy + 215,
            cx + 125,
            cy + 370
        ],
        fill="#F4F4F4"
    )

    # --------------------------------------------------------
    # HEAD
    # --------------------------------------------------------

    draw.ellipse(
        [
            cx - 85,
            cy - 110,
            cx + 180,
            cy + 150
        ],
        fill="#D87852",
        outline="#A94E3C",
        width=6
    )

    # --------------------------------------------------------
    # LEFT EAR
    # --------------------------------------------------------

    draw.polygon(
        [
            (cx - 70, cy - 70),
            (cx - 105, cy - 205),
            (cx + 5, cy - 100)
        ],
        fill="#D87852",
        outline="#A94E3C"
    )

    draw.polygon(
        [
            (cx - 65, cy - 85),
            (cx - 88, cy - 170),
            (cx - 5, cy - 105)
        ],
        fill="#F29A9A"
    )

    # --------------------------------------------------------
    # RIGHT EAR
    # --------------------------------------------------------

    draw.polygon(
        [
            (cx + 85, cy - 100),
            (cx + 195, cy - 205),
            (cx + 155, cy - 65)
        ],
        fill="#D87852",
        outline="#A94E3C"
    )

    draw.polygon(
        [
            (cx + 110, cy - 105),
            (cx + 180, cy - 170),
            (cx + 150, cy - 85)
        ],
        fill="#F29A9A"
    )

    # --------------------------------------------------------
    # FACE
    # --------------------------------------------------------

    draw.ellipse(
        [
            cx - 35,
            cy - 5,
            cx + 130,
            cy + 105
        ],
        fill="#F5F5F5"
    )

    # Eyes

    draw.ellipse(
        [
            cx - 25,
            cy - 40,
            cx + 10,
            cy - 5
        ],
        fill="#171717"
    )

    draw.ellipse(
        [
            cx + 90,
            cy - 40,
            cx + 125,
            cy - 5
        ],
        fill="#171717"
    )

    # Eye shine

    draw.ellipse(
        [
            cx - 17,
            cy - 34,
            cx - 8,
            cy - 25
        ],
        fill="white"
    )

    draw.ellipse(
        [
            cx + 98,
            cy - 34,
            cx + 107,
            cy - 25
        ],
        fill="white"
    )

    # Nose

    draw.polygon(
        [
            (cx + 30, cy + 35),
            (cx + 70, cy + 35),
            (cx + 50, cy + 60)
        ],
        fill="#222631"
    )

    # Mouth

    draw.arc(
        [
            cx + 10,
            cy + 45,
            cx + 50,
            cy + 90
        ],
        0,
        180,
        fill="#222631",
        width=3
    )

    draw.arc(
        [
            cx + 50,
            cy + 45,
            cx + 90,
            cy + 90
        ],
        0,
        180,
        fill="#222631",
        width=3
    )


# ============================================================
# MAGIC LIGHTS
# ============================================================

def draw_magic_lights(draw, panel_number):

    positions = [
        [(300, 360), (720, 350)],
        [(250, 330), (780, 380), (850, 290)],
        [(300, 400), (750, 320)],
        [(220, 350), (650, 300), (820, 390)],
        [(330, 330), (700, 350), (850, 300)]
    ]

    for x, y in positions[panel_number - 1]:

        draw.ellipse(
            [x - 14, y - 14, x + 14, y + 14],
            fill="#F5EFA7"
        )

        draw.ellipse(
            [x - 7, y - 7, x + 7, y + 7],
            fill="white"
        )


# ============================================================
# TEXT BOX
# ============================================================

def draw_story_text(draw, panel_number):

    font_file, font_size = PANEL_FONTS[panel_number - 1]

    font = get_font(font_file, font_size)

    text = PANEL_TEXT[panel_number - 1]

    # Text background

    box_x1 = 35
    box_y1 = 30
    box_x2 = WIDTH - 35
    box_y2 = 105

    draw.rounded_rectangle(
        [
            box_x1,
            box_y1,
            box_x2,
            box_y2
        ],
        radius=22,
        fill=(20, 30, 45),
        outline="white",
        width=3
    )

    # Center text

    bbox = draw.textbbox(
        (0, 0),
        text,
        font=font
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (WIDTH - text_width) // 2
    text_y = 67 - text_height // 2

    draw.text(
        [
            text_x + 2,
            text_y + 2
        ],
        text,
        font=font,
        fill="#000000"
    )

    draw.text(
        [
            text_x,
            text_y
        ],
        text,
        font=font,
        fill="#FFFFFF"
    )


# ============================================================
# PANEL NUMBER
# ============================================================

def draw_panel_number(draw, panel_number):

    font = get_font("segoeuib.ttf", 22)

    draw.rounded_rectangle(
        [
            20,
            HEIGHT - 65,
            160,
            HEIGHT - 20
        ],
        radius=12,
        fill="#17202A",
        outline="white",
        width=2
    )

    draw.text(
        [
            45,
            HEIGHT - 55
        ],
        f"PANEL {panel_number}",
        font=font,
        fill="white"
    )


# ============================================================
# MAIN IMAGE GENERATOR
# ============================================================

def generate_image(
    prompt=None,
    output_path="static/generated/panel_1.png",
    panel_number=1
):

    # Detect panel number from filename
    if "panel_2" in output_path:
        panel_number = 2

    elif "panel_3" in output_path:
        panel_number = 3

    elif "panel_4" in output_path:
        panel_number = 4

    elif "panel_5" in output_path:
        panel_number = 5

    # --------------------------------------------------------
    # CREATE IMAGE
    # --------------------------------------------------------

    image = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "#159BD3"
    )

    draw = ImageDraw.Draw(image)

    # --------------------------------------------------------
    # SKY
    # --------------------------------------------------------

    draw.rectangle(
        [0, 0, WIDTH, 430],
        fill="#159BD3"
    )

    # --------------------------------------------------------
    # SUN
    # --------------------------------------------------------

    draw_sun(
        draw,
        830,
        105,
        60
    )

    # --------------------------------------------------------
    # CLOUDS
    # --------------------------------------------------------

    draw_cloud(
        draw,
        120,
        70,
        0.9
    )

    draw_cloud(
        draw,
        410,
        105,
        0.8
    )

    draw_cloud(
        draw,
        650,
        55,
        1.0
    )

    # --------------------------------------------------------
    # BACKGROUND TREES
    # --------------------------------------------------------

    draw_tree(
        draw,
        90,
        270,
        200
    )

    draw_tree(
        draw,
        250,
        275,
        170
    )

    draw_tree(
        draw,
        860,
        260,
        210
    )

    draw_tree(
        draw,
        980,
        280,
        180
    )

    # --------------------------------------------------------
    # PINE TREES
    # --------------------------------------------------------

    draw_pine(
        draw,
        350,
        430,
        230
    )

    draw_pine(
        draw,
        470,
        420,
        270
    )

    draw_pine(
        draw,
        600,
        425,
        250
    )

    draw_pine(
        draw,
        700,
        420,
        270
    )

    # --------------------------------------------------------
    # GRASS
    # --------------------------------------------------------

    draw.rectangle(
        [
            0,
            390,
            WIDTH,
            HEIGHT
        ],
        fill="#268B73"
    )

    # Grass details

    for x in range(20, WIDTH, 45):

        draw.line(
            [
                x,
                450,
                x + 8,
                425
            ],
            fill="#55B99F",
            width=3
        )

        draw.line(
            [
                x + 12,
                490,
                x + 22,
                460
            ],
            fill="#55B99F",
            width=3
        )

    # --------------------------------------------------------
    # MAGIC LIGHTS
    # --------------------------------------------------------

    draw_magic_lights(
        draw,
        panel_number
    )

    # --------------------------------------------------------
    # FOX
    # --------------------------------------------------------

    draw_fox(
        draw,
        panel_number
    )

    # --------------------------------------------------------
    # STORY TEXT
    # --------------------------------------------------------

    draw_story_text(
        draw,
        panel_number
    )

    # --------------------------------------------------------
    # PANEL NUMBER
    # --------------------------------------------------------

    draw_panel_number(
        draw,
        panel_number
    )

    # --------------------------------------------------------
    # BORDER
    # --------------------------------------------------------

    draw.rounded_rectangle(
        [
            5,
            5,
            WIDTH - 5,
            HEIGHT - 5
        ],
        radius=20,
        outline="white",
        width=5
    )

    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------

    folder = os.path.dirname(output_path)

    if folder:
        os.makedirs(
            folder,
            exist_ok=True
        )

    image.save(
        output_path,
        quality=95
    )

    return output_path