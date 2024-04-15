# Radio Analysis Project

## Description
This project automates the process of capturing, transcribing, and summarizing live radio streams. It utilizes OpenAI's Whisper model for transcription and the GPT-4 model for generating summaries of the transcribed text. Additionally, it fetches radio station stream URLs using the Radio Browser API, allowing for detailed analysis and understanding of content from various radio stations.

## Features
- **Stream Capture**: Captures live audio from predefined radio stations using URLs fetched from the Radio Browser API.
- **Audio Transcription**: Utilizes OpenAI's Whisper model to transcribe audio content to text.
- **Text Summarization**: Leverages OpenAI's GPT-4 model to summarize transcribed texts.
- **Continuous Operation**: Designed to run continuously until manually stopped, making it ideal for long-term data collection.

## Prerequisites
Before you run this project, ensure you have the following installed:
- Python 3.8 or higher
- `ffmpeg` for handling audio streams
- Required Python libraries: `openai`, `requests`, `subprocess`

## Installation
Follow these steps to set up the project environment:
1. Clone the repository:
    - `git clone https://github.com/yourusername/radio-analysis-project.git`
    - `cd radio-analysis-project`
2. Install the necessary Python packages:
    - `pip install -r requirements.txt`

## Usage
To start the project, run the following command in the project directory:
 `python main.py`

You will be prompted to enter the name of the radio station. After entering a valid station name, the system will begin processing the stream.

## Configuration
Edit the `config.py` file to add or modify the list of radio stations and other settings such as transcription and summarization preferences.

## Contributing
Contributions to the project are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Thanks to OpenAI for providing the API for transcription and summarization.
- Special thanks to everyone who contributed to the project.



