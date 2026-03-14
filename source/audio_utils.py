import io
import subprocess
from pathlib import Path


def extract_audio_from_video(video_path: str | Path) -> io.BytesIO:
    """Extracts audio from a video file and returns it as a BytesIO object in Ogg format with Opus codec, suitable for transcription.
    Args:
        video_path (str | Path): The path to the input video file.
    Returns:
        io.BytesIO: A BytesIO object containing the extracted audio data in Ogg format.
    Raises:
        subprocess.CalledProcessError: If the ffmpeg command fails.
    Note:
        This function uses ffmpeg to extract audio from the video. Ensure that ffmpeg is installed and accessible in the system's PATH.
    """

    cmd = [
        "ffmpeg",               # Call the ffmpeg executable
        "-i", str(video_path),  # Input video file
        "-vn",                  # Ignore the video stream and keep audio only
        "-acodec", "libopus",   # Use the Opus codec for audio encoding
        "-ar", "16000",         # Set the audio sample rate to 16 kHz
        "-ac", "1",             # Set the number of audio channels to 1 (mono)
        "-f", "ogg",            # Output format: Ogg container
        "pipe:1"                # Output to stdout
    ]

    proc = subprocess.run(
        cmd,                     # Run the ffmpeg command
        stdout=subprocess.PIPE,  # Capture the output audio data
        stderr=subprocess.PIPE,  # Capture any error messages
        check=True               # Raise an exception if the command fails
    )

    audio_buffer = io.BytesIO(proc.stdout)  # Create a BytesIO object from the output audio data
    audio_buffer.name = "audio.ogg"         # Set a name attribute for the buffer (optional)
    audio_buffer.seek(0)                    # Reset the buffer's position to the beginning

    return audio_buffer
