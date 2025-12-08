
import os
import torch
import sounddevice as sd
models_urls = ['https://models.silero.ai/models/tts/en/v3_en.pt',
            'https://models.silero.ai/models/tts/ru/v5_ru.pt']

model_ru = 'silero_models/ru/model.pt'
model_en = 'silero_models/en/model.pt'

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = model_ru

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file(models_urls[1],
                                local_file)  

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

sample_rate = 48000
speaker='en_6'   #aidar, baya, kseniya, xenia, eugene
en_speaker = 'en_6' # от 0 до 117


def speaker_silero(text):
    audio = model.apply_tts(text=text,
                                speaker=speaker,
                                sample_rate=sample_rate)

    sd.play(audio, blocking=True)
print(speaker_silero("Привет, Silero работает!"))