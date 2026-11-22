import numpy as np
from pathlib import Path

from audio.audio_extractor import strip_audio
from audio.volume_measurer import measure_volume

SAMPLE_RATE = 16000 # TODO: Choose a suitable sample rate

def main():
    file_name = input("Enter file name (from inside input file): ").strip() # TODO: Maybe a UI or something where I can drag and drop rather than filename
    file_path = Path("input") / f"{file_name}.mp4"

    if not file_path.is_file():
        print("Not a file")
        return

    stripped = strip_audio(file_path, SAMPLE_RATE)
    samples = np.frombuffer(stripped.stdout, dtype="<f4") # Little endian 4 byte (32 bit) float
    
    results = measure_volume(samples, SAMPLE_RATE)

    if not results:
        print("No audio windows found.")
        return

    loudest = max(results, key=lambda x: x["db"])

    print("\nLoudest section:")
    print(f"Start: {loudest['start']:.2f}s")
    print(f"End: {loudest['end']:.2f}s")
    print(f"Volume: {loudest['db']:.2f} dBFS")

if __name__ == "__main__":
    main()