import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from stream_utils import get_radio_stream_url
from stream_capture import capture_audio
from transcribe import transcribe_audio
from summarize import summarize_text

app = Flask(__name__)

# Print the template folder path for debugging
print("Template folder path:", app.template_folder)

# Enable Flask debugging
app.config['DEBUG'] = True

# Global variable to store transcriptions
transcriptions = []

def summarize_large_text(transcriptions, chunk_size, summarizer):
    final_summary = ""
    for i in range(0, len(transcriptions), chunk_size):
        chunk = " ".join(" ".join(words) for words in transcriptions[i:i+chunk_size])
        summary = summarizer(chunk)
        final_summary += summary + "\n"
    return final_summary.strip()

def create_summarizer(client):
    def summarizer(text):
        return summarize_text(text, client)
    return summarizer

def start_capture_process(station_name):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "No API key found. Set the OPENAI_API_KEY environment variable.", 400

    client = OpenAI(api_key=api_key)

    duration = 60  # Duration in seconds to capture audio
    file_path = "recordings/captured_audio.mp3"

    os.makedirs('recordings', exist_ok=True)

    stream_url = get_radio_stream_url(station_name)
    if not stream_url:
        return "Failed to find a stream for the station.", 400

    capture_audio(stream_url, file_path, duration)
    if not os.path.exists(file_path):
        return "Audio file was not created. Check VLC capture.", 500

    transcript = transcribe_audio(file_path, client)
    if transcript:
        transcriptions.append(transcript.split())
        return transcript, 200
    else:
        return "Failed to transcribe audio", 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/capture-and-summarize', methods=['POST'])
def capture_and_summarize():
    data = request.json
    station = data['station']

    result, status = start_capture_process(station)
    if status != 200:
        return jsonify({'error': result}), status

    chunk_size = 1000  # Define your chunk size
    summarizer = create_summarizer(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))  # Create summarization function
    final_summary = summarize_large_text(transcriptions, chunk_size, summarizer)

    return jsonify({'transcription': result, 'summary': final_summary})

if __name__ == '__main__':
    app.run(debug=True)
