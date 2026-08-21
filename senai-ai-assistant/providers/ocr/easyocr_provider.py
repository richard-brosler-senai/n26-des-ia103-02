#providers/ocr/easyocr_provider.py
import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(["pt"])

def extract_text(uploaded_file) -> str:

    image = Image.open(uploaded_file)

    image_np = np.array(image)

    result = reader.readtext(
        image_np,
        detail=0
    )

    return "\n".join(result)