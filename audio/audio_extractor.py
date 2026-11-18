# TODO: Make it run ffmpeg strip audio, ignore video

import subprocess

def strip_audio(vid_path, sample_rate):
    result = subprocess.run(
        [ # Refer to https://ffmpeg.org/ffmpeg.html
            "ffmpeg", "-i", str(vid_path), 
            "-vn", # Ignore video
            "-ac", "1", # Mono audio true
            "output/stripped.wav"
        ]
    )