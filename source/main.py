import sys
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

from audio_utils import extract_audio_from_video

# Initialization --------------------------------------------------------------------------------
load_dotenv()
client = OpenAI()

# Variables -------------------------------------------------------------------------------------
context_prompt = "Esse áudio está em português do Brasil."
subtitle_path = Path(__file__).parent / "subtitle.srt"
audio = None

# Input -----------------------------------------------------------------------------------------
input_type = input("Enter the input type (video/audio): ").strip().lower()
while input_type not in ["video", "audio"]:
    print("Invalid input type. Please enter 'video' or 'audio'.")
    input_type = input("Enter the input type (video/audio): ").strip().lower()

file_name = input("Enter the file name (with extension): ").strip()
file_path = Path(__file__).parent / file_name
while not file_path.exists() or not file_path.is_file():
    print(f"File '{file_name}' does not exist. Please check the file name/extension and try again.")
    file_name = input("Enter the file name (with extension): ").strip()
    file_path = Path(__file__).parent / file_name

# Processing ------------------------------------------------------------------------------------
try:
    if input_type == "audio":
        audio = file_path.open("rb")  # Open the audio file in binary mode
    else:
        audio = extract_audio_from_video(file_path)  # Extract audio from the video file

    transcription = client.audio.transcriptions.create(
        file=audio,
        model="whisper-1",
        language="pt",
        response_format="srt",
        prompt=context_prompt
    )
except Exception as e:
    print(f"An error occurred: {e}")
    transcription = None
finally:
    if audio is not None:
        audio.close()  # Ensure the audio buffer is closed after use

# Output ----------------------------------------------------------------------------------------
if transcription is not None:
    with open(subtitle_path, "w", encoding="utf-8") as srt_file:
        srt_file.write(transcription)
    print(transcription)
else:
    print("Transcription failed. No output generated.")
    sys.exit(1)
