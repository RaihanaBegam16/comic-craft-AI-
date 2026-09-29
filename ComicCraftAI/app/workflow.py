import os

from app.gemini_flash import generate_outline
from app.image_generator import generate_image


def generate_comic(
    story_idea,
    main_character,
    setting,
    tone,
    art_style
):

    # =====================================================
    # OUTPUT FOLDER
    # =====================================================

    output_folder = "static/generated"

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    # =====================================================
    # GET STORY FROM GEMINI
    # If Gemini quota is unavailable, use local story
    # =====================================================

    try:

        story = generate_outline(
            story_idea,
            main_character,
            setting,
            tone
        )

    except Exception as e:

        print("Gemini unavailable. Using local story.")
        print("Gemini error:", e)

        story = f"""
Panel 1:
{main_character} enters the enchanted {setting} and begins a brave adventure.

Panel 2:
{main_character} walks deeper into the magical forest and notices glowing lights.

Panel 3:
A mysterious sound comes from behind the trees. {main_character} looks around bravely.

Panel 4:
{main_character} discovers a beautiful magical place hidden inside the forest.

Panel 5:
{main_character} safely returns from the adventure, happy and proud.
"""

    # =====================================================
    # CREATE 5 PANELS
    # =====================================================

    panels = []

    for i in range(1, 6):

        file_path = os.path.join(
            output_folder,
            f"panel_{i}.png"
        )

        # =================================================
        # PANEL-SPECIFIC STORY
        # =================================================

        if i == 1:
            panel_story = (
                f"{main_character} enters the enchanted {setting} "
                f"and begins a brave adventure."
            )

        elif i == 2:
            panel_story = (
                f"{main_character} walks deeper into the magical "
                f"{setting} and notices glowing lights."
            )

        elif i == 3:
            panel_story = (
                f"A mysterious sound comes from behind the trees. "
                f"{main_character} looks around bravely."
            )

        elif i == 4:
            panel_story = (
                f"{main_character} discovers a beautiful magical "
                f"place hidden inside the forest."
            )

        else:
            panel_story = (
                f"{main_character} safely returns from the adventure, "
                f"happy and proud."
            )

        # =================================================
        # CREATE IMAGE LOCALLY
        # =================================================

        generate_image(

            prompt=f"""
            Create Panel {i} of a 5-panel children's comic.

            Main character:
            {main_character}

            Panel story:
            {panel_story}

            Setting:
            {setting}

            Tone:
            {tone}

            Art style:
            {art_style}

            Character consistency:
            Cute orange fox
            Pointed ears
            White muzzle
            White belly
            Large black eyes
            Big fluffy tail
            Full body visible
            Same character design in every panel

            Background:
            Enchanted green forest
            Bright blue sky
            White fluffy clouds
            Warm yellow sun
            Magical glowing lights
            Green grass
            Colorful children's comic-book appearance

            Make the fox and background clearly visible.
            Do not show only the fox head.
            Show the complete fox body.
            """,

            output_path=file_path,
            panel_number=i
        )

        # =================================================
        # BROWSER IMAGE URL
        # =================================================

        image_url = (
            f"/static/generated/panel_{i}.png"
        )

        # =================================================
        # SAVE PANEL INFORMATION
        # =================================================

        panels.append(
            {
                "number": i,
                "title": f"Panel {i}",
                "image": image_url,
                "text": panel_story
            }
        )

    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {
        "story": story,
        "panels": panels
    }