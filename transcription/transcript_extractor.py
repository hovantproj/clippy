import whisper

def transcribe(samples):
    model = whisper.load_model("tiny", "cpu") # Tiny appeared to have better average performance than base and was faster

    text = model.transcribe(samples, verbose=False, word_timestamps=True)
    return text

