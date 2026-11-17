import numpy as np

def calculate_loudness(samples, sample_rate, window_seconds=5, hop_seconds=1):
    window_size = int(window_seconds * sample_rate) # Total samples
    hop_size = int(hop_seconds * sample_rate)

    results = [] # Need to store start time, end time and decibles

    return results