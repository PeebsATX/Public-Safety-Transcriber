This Python script records audio from a specified URL in chunks and transcribes the audio using OpenAI's transcription API. The transcriptions are saved to a file called transcriptions.txt.

**Prerequisites**

Python 3.x
ffmpeg installed on your system
An OpenAI API key


**Usage**

  Clone or download the script.
  Install the required Python modules by running pip install openai.
  Set your OpenAI API key in the OPENAI_API_KEY variable.
  Set the chunk length in seconds using the CHUNK_LENGTH variable.
  Set the name of the output directory using the OUTPUT_DIR variable.
  Set the output file format using the FORMAT variable.
  Set the OpenAI transcription model using the MODEL variable.
  Run the script by executing python3 live.py in your terminal.
  Enter the input URL when prompted.


**Script Flow**

The script starts by checking if the output directory exists. If it doesn't, the script creates the directory.
The script prompts the user to enter the input URL.
The script starts a loop that records audio in chunks using ffmpeg and transcribes each chunk using the OpenAI transcription API.
Each chunk is saved to the output directory using a filename that includes the chunk number padded with zeros.
A new thread is started for each chunk to perform the transcription asynchronously.
The transcribed text is printed to the console and saved to the transcriptions.txt file along with a timestamp.
The loop continues until the user stops the script.
