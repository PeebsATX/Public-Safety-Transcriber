import subprocess
import os
import time
import openai
import threading

# Set your OpenAI API key here
OPENAI_API_KEY = "your_open_api_key"

# Initialize the OpenAI API instance
openai.api_key = OPENAI_API_KEY

# Set the chunk length in seconds
CHUNK_LENGTH = 120

# Set the name of the output directory
OUTPUT_DIR = "output"

# Create the output directory if it does not exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Set the format for the output files
FORMAT = "mp3"

# Set the OpenAI transcription model
MODEL = "whisper-1"

# Prompt the user for the input URL
input_url = input("Enter the input URL: ")

# Function to transcribe a chunk of audio
def transcribe_chunk(filename, chunk_count, done_event):
    with open(filename, "rb") as f:
        response = openai.Audio.transcribe(MODEL, f)
        transcription = response["text"]

    print(f"Chunk {chunk_count}: {transcription}")

    # Write the transcription to the 'transcriptions.txt' file
    with open(os.path.join(OUTPUT_DIR, "transcriptions.txt"), "a") as transcription_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(chunk_count * CHUNK_LENGTH))
        transcription_file.write(f"Chunk {chunk_count} - Timestamp: {timestamp}\n{transcription}\n\n")

    # Signal that transcription is done
    done_event.set()

# Start recording chunks of audio
chunk_count = 0
transcription_threads = []
while True:
    # Generate the filename for the current chunk
    filename = os.path.join(OUTPUT_DIR, f"chunk{chunk_count:04d}.{FORMAT}")

    # Record the next chunk of audio
    cmd = ["ffmpeg", "-y", "-i", input_url, "-t", str(CHUNK_LENGTH), "-acodec", "copy", filename]
    subprocess.Popen(cmd)

    # Create an event object to signal thread completion
    done_event = threading.Event()
    transcription_thread = threading.Thread(target=transcribe_chunk, args=(filename, chunk_count, done_event))
    transcription_thread.start()
    transcription_threads.append((transcription_thread, done_event))

    # Check and remove threads that have completed
    for t, event in transcription_threads:
        if event.is_set():
            t.join()
            transcription_threads.remove((t, event))

    # Increment the chunk counter
    chunk_count += 1

    # Wait a bit before starting the next recording to avoid overlap
    time.sleep(CHUNK_LENGTH)