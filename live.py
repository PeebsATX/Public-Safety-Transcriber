import subprocess
import os
import time
from openai import OpenAI
from threading import Thread
from queue import Queue

def transcribe_audio(client, file_path):
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
    return transcript

def record_stream(url, chunk_length, queue, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_index = 0
    while True:
        filename = os.path.join(output_dir, f"chunk_{file_index:04d}.mp3")
        # Record approximately chunk_length seconds of data
        cmd = [
            "ffmpeg", "-y", "-i", url, 
            "-t", str(chunk_length), 
            "-acodec", "mp3", 
            filename
        ]
        subprocess.run(cmd, check=True)
        queue.put(filename)
        file_index += 1

def process_chunks(client, queue):
    while True:
        file_path = queue.get()
        transcript = transcribe_audio(client, file_path)
        print(f"Transcription of {file_path}:\n{transcript}")
        os.remove(file_path)  # Remove file after processing

def main():
    client = OpenAI()  # Initialize the OpenAI client
    stream_url = input("Enter the Icecast stream URL: ")
    chunk_length = 120  # Length of each audio chunk in seconds
    output_dir = "recorded_chunks"

    queue = Queue()
    record_thread = Thread(target=record_stream, args=(stream_url, chunk_length, queue, output_dir))
    process_thread = Thread(target=process_chunks, args=(client, queue))

    record_thread.start()
    process_thread.start()

    try:
        record_thread.join()
        process_thread.join()
    except KeyboardInterrupt:
        print("Transcription process stopped.")

if __name__ == "__main__":
    main()
