
import speech_recognition

sr = speech_recognition.Recognizer()


def create_task():
    print('Что добавить в список дел?')
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.7)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data= audio, language='ru-RU').lower()
    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'задача {query} добавлена в todo-list'

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.7)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data= audio, language='ru-RU').lower()

if query =='добавить задачу':
    print(create_task())
else:
    print(query)
