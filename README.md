# subtitle-generator
Generate subtitles from audio or video files using OpenAI's Speech-to-Text API.

This project uses FFmpeg to preprocess video input into a smaller speech-oriented audio format before sending it for transcription. The goal is to keep the workflow simple while reducing upload size and end-to-end latency.

API reference: [OpenAI Whisper models and supported languages](https://github.com/openai/whisper#available-models-and-languages)

## Quick setup (Windows)

1. Clone the repository and go to the project folder.
2. Create and activate a virtual environment:

```bat
python -m venv .venv
.venv\Scripts\activate
```

3. Install Python dependencies:

```bat
pip install -r source\requirements.txt
```

4. Install FFmpeg:

```bat
winget install Gyan.FFmpeg
```

5. Close and reopen the terminal (to refresh PATH).

6. Validate that FFmpeg is available:

```bat
ffmpeg -version
ffprobe -version
```

7. Create the file `source/.env` with your key:

```env
OPENAI_API_KEY=your_key_here
```

8. Put the `video.mp4` file inside the `source` folder.

9. Run the script:

```bat
python source\main.py
```

The output file will be generated as `source/subtitle.srt`.

## Technical choices

### Why use 16 kHz, OGG/Opus, and mono audio?

1. 16 kHz sample rate
    - Human speech is mostly concentrated in lower frequencies, so 16 kHz is usually enough for accurate speech transcription.
    - Compared to 44.1 kHz or 48 kHz, 16 kHz reduces the amount of audio data significantly, which can decrease upload time.
    - Smaller uploads often reduce end-to-end latency, especially on slower connections.

2. OGG container with Opus codec
    - Opus is a modern codec optimized for speech and low-bitrate streaming.
    - It provides very good intelligibility at small file sizes, helping reduce transfer time without a large quality penalty.
    - The transcription API accepts OGG/Opus, so this is a practical format for this workflow.

3. Mono (single channel)
    - Mono stores one channel instead of two, so file size is roughly half of equivalent stereo audio.
    - For speech transcription, stereo is usually unnecessary unless channel separation carries important information.

In short, this configuration is a trade-off: lower file size and faster transfer, while preserving enough speech quality for reliable subtitles.
