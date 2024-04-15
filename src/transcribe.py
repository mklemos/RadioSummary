import os
from openai import OpenAI

def transcribe_audio(file_path, client):
    """
    Transcribe the audio content from a given file using the OpenAI Whisper model.

    Parameters:
        file_path (str): The path to the audio file to be transcribed.
        client (OpenAI): An instance of the OpenAI client pre-configured with an API key.

    Returns:
        str or None: The transcription of the audio as text if successful, or None if an error occurs.
    
    Raises:
        Exception: Describes the error encountered during the transcription process, if any.
    """
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
