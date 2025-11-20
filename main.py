import os 
import random
import speech_recognition

sr = speech_recognition.Recognizer()

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.7)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data= audio, language='ru-RU').lower()
        
        return query
    except speech_recognition.UnknownValueError:
        return 'не понял'

def create_task():
    print('Что добавить в список дел?')
    query = listen_command()
    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'задача {query} добавлена в todo-list'


def play_music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'vlc-open {random_file}')

    return f'dance {random_file.split("/")[-1]}'

def main():
    query = listen_command()
    if query =='добавить задачу':
        print(create_task())
    elif query =="включить музыку":
        print(play_music())
    else:
        print(query)

if __name__=='__main__':
    main()