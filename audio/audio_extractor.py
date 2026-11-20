import subprocess

def strip_audio(vid_path, sample_rate):
    result = subprocess.run(
        [ # Refer to https://ffmpeg.org/ffmpeg.html
            "ffmpeg", "-i", str(vid_path),
            "-vn", # Ignore video
            "-ac", "1", # Mono audio true
            "-ar", str(sample_rate),
            "-f", "f32le", # 32 bit float with little endian (what my laptop uses change depending on device)
            "pipe:1" # Pipes to stdout
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True
    )

    return result