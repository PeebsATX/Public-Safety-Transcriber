import subprocess
import os
import time
import openai
import threading

# Set your OpenAI API key here
OPENAI_API_KEY = "your_open_api_key"

# Create a new OpenAI API instance
openai.api_key = OPENAI_API_KEY

# Set the chunk length in seconds
CHUNK_LENGTH = 120

# Set the name of the output directory
OUTPUT_DIR = "output"

# Create the output directory if it does not exist
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

# Set the format for the output MP3 files
FORMAT = "mp3"

# Set the OpenAI transcription model
MODEL = "whisper-1"

# Prompt the user for the input URL
input_url = input("Enter the input URL: ")

# Function to transcribe a chunk of audio
def transcribe_chunk(filename, chunk_count):
    os.rename(filename, filename + '.wav')
    with open(filename + '.wav', "rb") as f:
        response = openai.Audio.transcribe(MODEL, f)
        transcription = response["text"]

    print(f"Chunk {chunk_count}: {transcription}")
    os.remove(filename + '.wav')

    # Write the transcription to the 'transcriptions.txt' file
    with open("transcriptions.txt", "a") as transcription_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(chunk_count * CHUNK_LENGTH))
        transcription_file.write(f"Chunk {chunk_count} - Timestamp: {timestamp}\n{transcription}\n\n")

# Start recording chunks of audio
chunk_count = 0
while True:
    # Generate the filename for the current chunk
    filename = os.path.join(OUTPUT_DIR, f"chunk{chunk_count:04d}.{FORMAT}")

    # Use ffmpeg to record the next chunk of audio
    cmd = f"ffmpeg -y -i {input_url} -t {CHUNK_LENGTH} -acodec {FORMAT} {filename}"
    subprocess.run(cmd, shell=True)

    # Start a new thread to transcribe the current chunk of audio
    transcription_thread = threading.Thread(target=transcribe_chunk, args=(filename, chunk_count))
    transcription_thread.start()

    # Increment the chunk counter
    chunk_count += 1
    transcription_thread.join()

