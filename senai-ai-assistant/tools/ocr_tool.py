# tools/ocr_tool.py
from services.ocr_service import process_image
def execute(image) -> str:
    return process_image(image)
