import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

TEXT_MODEL = "gemini-3.8-flash"
IMAGE_MODEL = "gemini-3.8-flash"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = os.path.join(BASE_DIR, "static")
PANELS_DIR = os.path.join(STATIC_DIR, "panels")
EXPORTS_DIR = os.path.join(STATIC_DIR, "exports")

os.makedirs(PANELS_DIR, exist_ok=True)
os.makedirs(EXPORTS_DIR, exist_ok=True)