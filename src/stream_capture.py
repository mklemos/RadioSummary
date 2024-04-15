# stream_capture.py
import subprocess
import os
import requests

def get_radio_stream_url(station_name):
    """Get the streaming URL for a given radio station name."""
    url = f"http://de1.api.radio-browser.info/json/stations/byname/{station_name}"
    response = requests.get(url)
    stations = response.json()
    if stations:
        return stations[0]['url_resolved']
    return None

def capture_audio(stream_url, file_path, duration=1):
    """Capture audio from a stream URL using ffmpeg and save it to a file."""
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
        print("Failed to capture audio:", e)
