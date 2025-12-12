import os
import re
import torch
import sounddevice as sd
import numpy as np

# URL моделей
models_urls = [
    'https://models.silero.ai/models/tts/en/v3_en.pt',
    'https://models.silero.ai/models/tts/ru/v5_ru.pt'
]

# Пути к локальным моделям
model_ru_path = 'silero_models/ru/model.pt'
model_en_path = 'silero_models/en/model.pt'

# Создаем директории, если их нет
os.makedirs('silero_models/ru', exist_ok=True)
os.makedirs('silero_models/en', exist_ok=True)


device = torch.device('cpu')
torch.set_num_threads(4)


if not os.path.isfile(model_ru_path):
    torch.hub.download_url_to_file(models_urls[1], model_ru_path)


if not os.path.isfile(model_en_path):
    torch.hub.download_url_to_file(models_urls[0], model_en_path)


model_ru = torch.package.PackageImporter(model_ru_path).load_pickle("tts_models", "model")
model_en = torch.package.PackageImporter(model_en_path).load_pickle("tts_models", "model")

model_ru.to(device)
model_en.to(device)

# Настройки
ru_sample_rate = 48000
en_sample_rate = 24000  # Английская модель 
ru_speaker = 'baya'  # aidar, baya, kseniya, xenia, eugene
en_speaker = 'en_6'  # от 0 до 117

def detect_language(text):
    """Определяет язык текста"""
    
    cyrillic_count = len(re.findall(r'[а-яА-ЯёЁ]', text))
    latin_count = len(re.findall(r'[a-zA-Z]', text))
    
    if cyrillic_count > latin_count:
        return 'ru'
    elif latin_count > cyrillic_count:
        return 'en'
    else:
        
        return 'ru'

def split_text_by_language(text):
    """Разделяет текст на части по языкам"""
    parts = []
    current_part = ""
    current_lang = None
    
    for char in text:
        # Определяем язык текущего символа
        if re.match(r'[а-яА-ЯёЁ]', char):
            char_lang = 'ru'
        elif re.match(r'[a-zA-Z]', char):
            char_lang = 'en'
        else:
            
            char_lang = current_lang if current_lang else 'ru'
        
        
        if current_lang and char_lang != current_lang:
            if current_part.strip():  
                parts.append((current_part, current_lang))
            current_part = char
        else:
            current_part += char
        
        current_lang = char_lang
    
    
    if current_part.strip():
        parts.append((current_part, current_lang or 'ru'))
    
    return parts

def synthesize_mixed_text(text):
    
    parts = split_text_by_language(text)
    
    if not parts:
        return np.array([])
    
    audio_parts = []
    
    for part_text, lang in parts:
        try:
            if lang == 'ru':
                # Синтез русского текста
                audio = model_ru.apply_tts(
                    text=part_text,
                    speaker=ru_speaker,
                    sample_rate=ru_sample_rate
                )
            else:  # lang == 'en'
                # Синтез английского текста
                audio = model_en.apply_tts(
                    text=part_text,
                    speaker=en_speaker,
                    sample_rate=en_sample_rate
                )
                
                audio = np.repeat(audio, 2)
            
            audio_parts.append(audio)
        except Exception as e:
            print(f"Ошибка синтеза части '{part_text}': {e}")
            continue
    
    if not audio_parts:
        return np.array([])
    
    
    combined_audio = np.concatenate(audio_parts)
    return combined_audio

def speaker_silero(text):
    
    audio = synthesize_mixed_text(text)
    
    if len(audio) > 0:
        # Используем частоту дискретизации 48000 Гц
        sd.play(audio, ru_sample_rate, blocking=True)
        return "Текст успешно озвучен"
    else:
        return "Не удалось озвучить текст"