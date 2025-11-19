import torch
from transformers import AutoModelForCTC, AutoProcessor

processor = AutoProcessor.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-arabic")
model = AutoModelForCTC.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-arabic")

def transcribe_audio(path):
    import librosa
    audio, sr = librosa.load(path, sr=16000)
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
    logits = model(inputs.input_values).logits
    pred_ids = torch.argmax(logits, dim=-1)[0]
    transcription = processor.decode(pred_ids)
    return transcription
