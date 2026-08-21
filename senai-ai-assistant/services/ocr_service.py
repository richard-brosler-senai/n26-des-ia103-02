#services/ocr_service.py
from providers.ocr.easyocr_provider import extract_text

def process_image(uploaded_file) -> str:
    return extract_text( uploaded_file)