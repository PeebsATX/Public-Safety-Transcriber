Public Safety Transcriber

Overview

"Public Safety Transcriber" is a Python application designed to capture and transcribe live public safety audio streams. This tool records streaming audio, segments it into chunks, and utilizes OpenAI's Whisper-1 model to generate accurate text transcriptions. It's an ideal solution for monitoring and transcribing public safety communications, such as police and emergency services broadcasts.

Features

Captures live audio streams from specified URLs.
Automatically segments the audio into preset chunk lengths.
Utilizes OpenAI's Whisper-1 model for high-accuracy transcription.
Employs multithreading to handle simultaneous recording and transcription tasks.
Dependencies

Python 3.x
OpenAI Python Library
FFmpeg for audio recording and processing
Standard Python libraries: os, time, threading, queue, subprocess
Installation

Ensure Python 3.x is installed on your system.
Install the OpenAI Python library using pip:
Copy code
pip install openai
Install FFmpeg, following the instructions for your specific operating system.
Usage

Start the script with Python:
Copy code
python public_safety_transcriber.py
Enter the URL of the public safety audio stream when prompted.
The script will start recording and transcribing the stream automatically.
Notes

Ensure you have the necessary permissions to access and transcribe the target audio stream.
The script is set to handle .mp3 audio formats. Adjust the recording format in the script if necessary.
