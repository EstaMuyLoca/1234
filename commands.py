import os, webbrowser, sys, requests, subprocess, voice, app
from pathlib import Path


def browser():
    webbrowser.open('https://www.youtube.com', new =2)
    #print('браузер запущен')

def game():
    subprocess.Popen('C:/Program Files')
    #print("игра запущена")

def offpc():
    #os.system('shutdown /s')
    print("пк выключен")

def weather():
    try:
        params= {"q": "Kazan", "appid": '9e1551e8704efdd171e53c2db37c21c5',"units":"metric", "lang": "ru"} 
        responce = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params=params)
        app.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
        if not responce:
            raise
        w = responce.json()
    except:
        app.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

def offBot():
    sys.exit()
def show_desktop_items():
    """
    Возвращает текст для озвучивания объектов на рабочем столе.
    Вызывай voice.speaker(result) для голосового вывода.
    """
    desktop_path = Path.home() / "Desktop"
    
    speech_text = "Объекты на рабочем столе. "
    
    for item in sorted(desktop_path.iterdir()):
        if item.is_dir():
            speech_text += f"Папка {item.name}. "
        elif item.is_file():
            name_without_ext = item.stem
            speech_text += f"Файл {name_without_ext}. "
        else:
            speech_text += f"{item.name}. "
    
    print("Объекты на рабочем столе:")
    print("-" * 40)
    for item in sorted(desktop_path.iterdir()):
        if item.is_dir():
            print(f"📁 Папка: {item.name}")
        elif item.is_file():
            name_without_ext = item.stem
            print(f"📄 Файл: {name_without_ext}")
        else:
            print(f"🔗 {item.name}")
    
    app.speaker(speech_text)
    



def passive():
    pass