from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

from audio_utils import extract_audio_from_video

load_dotenv()
client = OpenAI()

context_prompt = "Esse áudio está em português do Brasil."

base_dir = Path(__file__).parent
video_path = base_dir / "video.mp4"
# audio_path = base_dir / "audio.mp3"
subtitle_path = base_dir / "subtitle.srt"
audio = None

try:
    audio = extract_audio_from_video(video_path)

    transcription = client.audio.transcriptions.create(
        file=audio,
        model="whisper-1",
        language="pt",
        response_format="srt",
        prompt=context_prompt
    )
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if audio is not None:
        audio.close()  # Ensure the audio buffer is closed after use

print(transcription)

with open(subtitle_path, "w", encoding="utf-8") as srt_file:
    srt_file.write(transcription)
