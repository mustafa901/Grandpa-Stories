import librosa
import soundfile as sf

def enhance_audio(path):
    y, sr = librosa.load(path, sr=None)
    y_clean = librosa.effects.preemphasis(y)
    cleaned_path = f"cleaned_{path}"
    sf.write(cleaned_path, y_clean, sr)
    return cleaned_path
