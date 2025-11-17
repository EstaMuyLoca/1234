import speech_recognition

sr = speech_recognition.Recognizer()
def greet():
    return"Hello"



with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.7)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data= audio, language='ru-RU').lower()
if query == "Привет друг":
    print(greet())
else:
    print(query)
