#services/vision_service.py
from services.settings_service import ( load_settings )
from PIL import Image, UnidentifiedImageError
from io import BytesIO
# Função para descrever a imagem
def describe_image(
        image_bytes,
        prompt=None,
        image_type="image/jpeg"):

    settings = load_settings()
    provider = settings["VISION_PROVIDER"]

    if provider == "gemini":
        from providers.vision.gemini_vision \
            import describe_image
    elif provider == "azure":
        from providers.vision.azure_vision \
            import describe_image
    elif provider == "groq":
        from providers.vision.groq_vision \
            import describe_image
    elif provider == "ollama":
        from providers.vision.ollama_vision \
            import describe_image
    else:
        return "Provider não configurado."
    return describe_image(
        image_bytes,
        prompt,
        image_type
    )

def detect_image_mimetype(data: bytes) -> str | None:
    try:
        with Image.open(BytesIO(data)) as img:
            img.verify()

        with Image.open(BytesIO(data)) as img:
            return img.get_format_mimetype()

    except (UnidentifiedImageError, OSError):
        return None
