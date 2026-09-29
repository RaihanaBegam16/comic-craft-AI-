from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import os

from .config import EXPORTS_DIR


def export_comic_pdf(
    title,
    panels,
    comic_page_path
):

    os.makedirs(
        EXPORTS_DIR,
        exist_ok=True
    )

    output_path = os.path.join(
        EXPORTS_DIR,
        "comic_story.pdf"
    )

    pdf = canvas.Canvas(
        output_path,
        pagesize=A4
    )

    page_width, page_height = A4

    # Title
    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawCentredString(
        page_width / 2,
        page_height - 40,
        title
    )

    # Comic image
    if os.path.exists(comic_page_path):

        image = ImageReader(
            comic_page_path
        )

        margin = 25

        available_width = (
            page_width - margin * 2
        )

        available_height = (
            page_height - 100
        )

        pdf.drawImage(
            image,
            margin,
            35,
            width=available_width,
            height=available_height,
            preserveAspectRatio=True,
            anchor="c"
        )

    pdf.showPage()

    pdf.save()

    print(
        f"PDF created: {output_path}"
    )

    return output_path