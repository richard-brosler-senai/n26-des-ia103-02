import os
from pathlib import Path
from playsound3 import playsound
from dotenv import load_dotenv

# import namespaces
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

def main():
    try:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Get Configuration Settings
        load_dotenv()
        endpoint = os.getenv("MODEL_ENDPOINT")
        model_deployment = os.getenv("MODEL_NAME")
        file_path = Path(__file__).parent / "speech.wav"
        
        # Play the speech file
        playsound(file_path)
        
        # Create the Azure OpenAI client
        token_provider = get_bearer_token_provider(                    
            DefaultAzureCredential(), "https://ai.azure.com/.default"
        )

        client = AzureOpenAI(
            azure_endpoint=endpoint,
            azure_ad_token_provider = token_provider,
            api_version="2025-03-01-preview"
        )

        # Generate speech and save to file
        speech_file_path = Path(__file__).parent / "speech.mp3"
        with client.audio.speech.with_streaming_response.create(
                    model='gpt-4o-mini-tts',
                    voice="jade-hardy",
                    input="Minha voz é meu passaporte?",
                    instructions="Fale em um tom sarcástico",
                ) as response:
            response.stream_to_file(speech_file_path)
        
    
        # Play the generated speech file
        playsound(speech_file_path)

        
        # Call model to transcribe audio file
        audio_file = open(speech_file_path, "rb")
        transcription = client.audio.transcriptions.create(
            model=model_deployment,
            file=audio_file,
            response_format="text"
        )
            
        print(transcription)
        audio_file = open(file_path, "rb")
        transcription = client.audio.transcriptions.create(
            model=model_deployment,
            file=audio_file,
            response_format="text"
        )
            
        print(transcription)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()