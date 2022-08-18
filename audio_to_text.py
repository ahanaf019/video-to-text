import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer



model_name = "facebook/wav2vec2-base-960h"
tokenizer = Wav2Vec2Tokenizer.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)


def transcribe(filename):

    speech, rate = librosa.load(filename, sr=16000)

    input_values = tokenizer(speech, return_tensors='pt').input_values
    logits = model(input_values).logits
    # print(logits)
    predicted_ids = torch.argmax(logits, dim=-1)

    transcriptions = tokenizer.decode(predicted_ids[0])
    # print(transcriptions)
    return transcriptions