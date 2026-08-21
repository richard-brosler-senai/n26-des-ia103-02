# providers/vision/ollama_vision.py
from openai import OpenAI
import base64

from services.settings_service import load_settings
settings = load_settings()

client = OpenAI(
    base_url=settings["OLLAMA_VISION_BASE_URL"],
    api_key="ollama"
)


def describe_image(image_bytes, prompt=None, image_type="image/jpeg") ->str:

    if prompt == None: prompt = """Descreva detalhadamente a imagem"""

    image_base64 = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    response = client.chat.completions.create(
        model=settings["OLLAMA_VISION_MODEL"],

        messages=[
            {
                "role": "system",
                "content": "Você responde exclusivamente em português do Brasil. Nunca responda em inglês."
            },
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