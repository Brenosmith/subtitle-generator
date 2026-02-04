from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

context_prompt = "Esse áudio está em português."

with open("audio.mp3", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        language="pt",
        response_format="srt",
        prompt=context_prompt
    )

print(transcription)

with open("subtitle.srt", "w", encoding="utf-8") as srt_file:
    srt_file.write(transcription)

