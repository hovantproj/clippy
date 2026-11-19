import numpy as np

def measure_volume(samples, sample_rate, window_seconds=5, hop_seconds=1):
    window_size = int(window_seconds * sample_rate) # Total samples
    hop_size = int(hop_seconds * sample_rate)

    results = [] # Need to store start time, end time and decibles

    for start in range(0, len(samples) - window_size + 1, hop_size):
        block = samples[start:start + window_size]

        rms = np.sqrt(np.mean(block ** 2)) # RMS formula
        db = 20 * np.log10(max(float(rms), 1e-10))

        results.append({
            "start": start / sample_rate,
            "end": (start + window_size) / sample_rate,
            "db": float(db)
        })

    return results