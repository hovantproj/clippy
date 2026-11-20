import numpy as np

from audio.audio_extractor import strip_audio
from audio.volume_measurer import measure_volume

SAMPLE_RATE = 16000 # TODO: Choose a suitable sample rate

def main():
    file_name = input("Enter file name (from inside input file): ") # TODO: Maybe a UI or something where I can drag and drop rather than filename
    file_path = str("input/"+file_name+".mp4")

    stripped = strip_audio(file_path, SAMPLE_RATE)
    samples = np.frombuffer(stripped.stdout, dtype="<f4") # Little endian 4 byte (32 bit) float
    
    results = measure_volume(samples, SAMPLE_RATE)

    print(results)

if __name__ == "__main__":
    main()