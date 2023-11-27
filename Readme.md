# Public Safety Transcriber

## Overview
"Public Safety Transcriber" is a Python script, named `live.py`, that captures and transcribes live public safety audio streams. It records streaming audio, segments it into chunks, and utilizes OpenAI's Whisper-1 model to generate accurate text transcriptions. Ideal for monitoring and transcribing public safety communications, such as police and emergency broadcasts.

## Features
- Captures live audio streams from specified URLs.
- Segments audio into preset chunk lengths.
- Utilizes OpenAI's Whisper-1 model for high-accuracy transcription.
- Employs multithreading for simultaneous recording and transcription.

## Dependencies
- Python 3.x
- OpenAI Python Library
- FFmpeg for audio recording and processing
- Standard Python libraries: `os`, `time`, `threading`, `queue`, `subprocess`

## Installation
1. Ensure Python 3.x is installed.
2. Install OpenAI Python library:
**PIP install openai**

3. Install FFmpeg as per your OS instructions.

## Usage
1. Run the script:
**python3 live.py**

2. Enter the URL of the audio stream when prompted.
3. The script begins recording and transcribing the stream.

## Notes
- Required permissions for accessing and transcribing the audio stream.
- Designed for `.mp3` audio formats. Adjust recording format in the script if needed.

