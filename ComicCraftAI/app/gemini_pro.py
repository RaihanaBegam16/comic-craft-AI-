from .gemini_client import get_gemini_client


def improve_scene(scene: str) -> str:
    client = get_gemini_client()

    prompt = f"""
Improve this comic scene for visual image generation.

Scene:
{scene}

Make it visually clear.
Describe:
- full body character
- face
- body position
- forest background
- lighting
- atmosphere
- cinematic composition

Do not change the story.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text.strip()