
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

def main():
    query = listen_command()
    if query =='добавить задачу':
        print(create_task())
    else:
        print(query)

if __name__=='__main__':
    main()