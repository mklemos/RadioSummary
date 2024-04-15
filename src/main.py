# main.py
"""
This module controls the overall operation of capturing, transcribing, and summarizing
radio streams. It handles user input for station selection, captures audio streams,
transcribes the audio, and provides a summary of the transcribed text.
"""

import os
from openai import OpenAI
from stream_utils import get_radio_stream_url
from stream_capture import capture_audio
from transcribe import transcribe_audio
from summarize import summarize_text

# Global variable to store transcriptions
transcriptions = []

def summarize_large_text(transcriptions, chunk_size, summarizer):
    """
    Summarizes large text by dividing it into chunks and summarizing each chunk.

    :param transcriptions: List of transcription segments.
    :param chunk_size: Number of segments to include in each chunk for summarization.
    :param summarizer: Function to use for summarizing text.
    :return: A string that is the final summary of all chunks.
    """
    final_summary = ""
    for i in range(0, len(transcriptions), chunk_size):
        chunk = " ".join(" ".join(words) for words in transcriptions[i:i+chunk_size])
        summary = summarizer(chunk)
        final_summary += summary + "\n"
    return final_summary.strip()

def create_summarizer(client):
    """
    Creates a summarization function using a given OpenAI client.

    :param client: The OpenAI client used for generating summaries.
    :return: A function that takes text and returns its summary.
    """
    def summarizer(text):
        return summarize_text(text, client)
    return summarizer

def main():
    """
    Main function to run the radio analysis project. Handles user input, stream capture,
    audio transcription, and text summarization.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("No API key found. Set the OPENAI_API_KEY environment variable.")
        return

    client = OpenAI(api_key=api_key)

    # Get user input for station or set a default
    station_name = input("Enter the station name (e.g., jazz, rock, classical, pop, bbc): ").strip()
    duration = 10  # Duration in seconds to capture audio
    file_path = "recordings/captured_audio.mp3"

    # Ensure recordings directory exists
    os.makedirs('recordings', exist_ok=True)

    # Continuous operation to capture and transcribe audio
    try:
        while True:
            # Get radio stream URL
            stream_url = get_radio_stream_url(station_name)
            if not stream_url:
                print("Failed to find a stream for the station.")
                continue

            # Capture audio
            capture_audio(stream_url, file_path, duration)

            # Check if the file was created before proceeding
            if not os.path.exists(file_path):
                print("Audio file was not created. Check VLC capture.")
                continue

            # Transcribe audio
            transcript = transcribe_audio(file_path, client)
            if transcript:
                print("Transcript:", transcript)
                transcriptions.append(transcript.split())  # Store the transcription as a list of words
            else:
                print("Failed to transcribe audio")
                continue

    except KeyboardInterrupt:
        # Summarize the accumulated transcriptions before exiting
        if transcriptions:
            chunk_size = 1000  # Define your chunk size
            summarizer = create_summarizer(client)  # Create summarization function
            final_summary = summarize_large_text(transcriptions, chunk_size, summarizer)
            print("Final Summary:", final_summary)
        print("Exiting...")
        return

if __name__ == "__main__":
    main()
