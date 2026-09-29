from .gemini_client import get_model_response
from .config import TEXT_MODEL


def generate_outline(
    story_idea: str,
    main_character: str,
    setting: str,
    tone: str
):
    prompt = f"""
Create a 5-panel comic story outline.

Story idea:
{story_idea}

Main character:
{main_character}

Setting:
{setting}

Tone:
{tone}

Create exactly 5 panels.

For each panel give:
- Panel number
- Scene description
- Character action
- Short dialogue

Keep the main character consistent throughout all 5 panels.
Make the story flow naturally from Panel 1 to Panel 5.
"""

    return get_model_response(
        TEXT_MODEL,
        prompt
    )