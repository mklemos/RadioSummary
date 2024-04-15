import os
from openai import OpenAI

def transcribe_audio(file_path, client):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            return transcription.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
