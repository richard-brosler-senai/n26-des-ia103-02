# providers/vision/azure_vision.py
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from services.settings_service import load_settings

# Logando na Azure
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(credential, "https://ai.azure.com/.default")

settings = load_settings()
client = OpenAI(
    base_url=settings["AZURE_OPENIA_URL"],
    api_key=token_provider()
)

import base64

def describe_image(image_bytes, prompt=None, image_type="image/jpeg") -> str:

    if prompt == None: prompt = """Descreva detalhadamente a imagem"""

    img_base64 = base64.b64encode(
        image_bytes
    ).decode()

    response = client.chat.completions.create(
        model=settings["AZURE_LLM_MODEL"],
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
                            "url":
                            f"data:{image_type};base64,{img_base64}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content