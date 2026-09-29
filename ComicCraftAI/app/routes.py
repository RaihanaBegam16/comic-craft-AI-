from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .workflow import generate_comic


router = APIRouter()

templates = Jinja2Templates(
    directory="templates"
)


@router.get(
    "/",
    response_class=HTMLResponse
)
async def home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post(
    "/generate",
    response_class=HTMLResponse
)
async def generate(
    request: Request,

    story_idea: str = Form(...),

    main_character: str = Form(...),

    setting: str = Form(...),

    tone: str = Form(...),

    art_style: str = Form(...)
):

    try:

        comic = generate_comic(
            story_idea=story_idea,
            main_character=main_character,
            setting=setting,
            tone=tone,
            art_style=art_style
        )

        return templates.TemplateResponse(
            request=request,
            name="comic_preview.html",
            context={
                "comic": comic,
                "panels": comic["panels"]
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={
                "error": str(e)
            }
        )