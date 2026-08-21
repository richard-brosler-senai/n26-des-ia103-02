# tools/vision_tool.py
from services.vision_service import describe_image
def execute(
        image,
        prompt,
        image_type):

    return describe_image(
        image,
        prompt,
        image_type
    )