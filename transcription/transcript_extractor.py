import whisper

def transcribe(samples):
    model = whisper.load_model("tiny", "cpu")

    text = model.transcribe(samples, verbose=False, word_timestamps=True)
    return text

