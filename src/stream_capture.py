# stream_capture.py
"""
This module provides functions to fetch streaming URLs for radio stations and to
capture audio from these streams using ffmpeg.
"""

import os
import subprocess
import requests

def get_radio_stream_url(station_name):
    """
    Get the streaming URL for a given radio station name.

    :param station_name: The name of the radio station.
    :return: Resolved URL of the radio stream if available, otherwise None.
    """
    url = f"http://de1.api.radio-browser.info/json/stations/byname/{station_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        stations = response.json()
        if stations:
            return stations[0]['url_resolved']
    except requests.RequestException as e:
        print(f"Error fetching radio station URL for '{station_name}': {e}")
    return None

def capture_audio(stream_url, file_path, duration=1):
    """
    Capture audio from a stream URL using ffmpeg and save it to a specified file.

    :param stream_url: The URL from which to capture audio.
    :param file_path: The file path where the audio will be saved.
    :param duration: Duration in seconds to capture audio. Defaults to 1 second.
    """
    if not stream_url:
        print("No stream URL provided.")
        return

    # Ensure the directory for the output exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Command to capture audio using ffmpeg
    command = [
        'ffmpeg',
        '-y',  # Overwrite output files without asking
        '-i', stream_url,  # Input URL
        '-t', str(duration),  # Duration to capture in seconds
        '-acodec', 'libmp3lame',  # Convert audio to MP3 using the LAME encoder
        '-ar', '44100',  # Audio sample rate
        '-ab', '128k',  # Audio bitrate
        file_path  # Output file path
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to capture audio: {e}")
