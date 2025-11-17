
import speech

sr = speech.Recognizer()
with speech.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.7)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data= audio, language='ru-RU').lower()
print(query)
