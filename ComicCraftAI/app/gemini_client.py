from google import genai
from .config import GEMINI_API_KEY
import time

client = genai.Client(api_key=GEMINI_API_KEY)

# priority order la try pannum
FALLBACK_MODELS = [
    "gemini-3.8-flash",
    "gemini-3.5-flash",
    "gemini-3-flash-preview",
    "gemini-flash-latest",
]

def get_model_response(model_name: str, prompt: str):
    models_to_try = [model_name] + [m for m in FALLBACK_MODELS if m != model_name]
    
    last_error = None
    for m in models_to_try:
        try:
            response = client.models.generate_content(
                model=m,
                contents=prompt
            )
            return response.text
        except Exception as e:
            err_str = str(e)
            last_error = e
            # 503 / UNAVAILABLE na next model try pannu
            if "503" in err_str or "UNAVAILABLE" in err_str:
                print(f"Model {m} busy, next model trying...")
                time.sleep(1)
                continue
            else:
                raise e
    
    raise last_error