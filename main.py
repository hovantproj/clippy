from audio.audio_extractor import strip_audio
from audio.volume_measurer import measure_volume

def main():
    file_path = input("Enter file path: ") # TODO: Maybe a UI or something where I can drag and drop rather than filename

    stripped = strip_audio(file_path, 16000) # TODO: Choose a suitable sample rate
    results = measure_volume()

if __name__ == "__main__":
    main()