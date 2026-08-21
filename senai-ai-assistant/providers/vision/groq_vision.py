# providers/vision/groq_vision.py
from openai import OpenAI
import base64

from services.settings_service import load_settings

settings = load_settings()

client = OpenAI(
    api_key=settings["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def describe_image(image_bytes, prompt=None, image_type="image/jpeg") ->str:

    if prompt == None: prompt = """Descreva detalhadamente a imagem"""

    image_base64 = base64.b64encode(
        image_bytes
    ).decode()

    response = client.chat.completions.create(
        model=settings["GROQ_VISION_MODEL"],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{image_type};base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content