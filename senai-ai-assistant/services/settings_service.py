#services/settings_service.py
from dotenv import dotenv_values, set_key, load_dotenv

ENV_FILE = ".env"

def load_settings():

    return dotenv_values(
        ENV_FILE
    )

def save_settings(
        key,
        value):

    set_key(
        ENV_FILE,
        key,
        value
    )
    # depois de salvar as keys recarregamos as variáveis
    load_dotenv()