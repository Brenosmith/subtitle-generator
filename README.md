# subtitle-generator
This project generates subtitles from audio and video using OpenAI's Speech-to-Text tool.

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
