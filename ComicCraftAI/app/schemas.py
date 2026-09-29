from pydantic import BaseModel


class ComicRequest(BaseModel):
    story_idea: str
    main_character: str
    setting: str
    tone: str
    art_style: str


class Panel(BaseModel):
    number: int
    scene: str
    dialogue: str = ""
    image_path: str = ""


class ComicResponse(BaseModel):
    title: str
    panels: list[Panel]