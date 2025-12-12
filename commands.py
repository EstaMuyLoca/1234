import os, webbrowser, sys, requests, subprocess, voice
from pathlib import Path
import win32api
import win32gui

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
        voice.speaker_silero(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
        if not responce:
            raise
        w = responce.json()
    except:
        voice.speaker_silero('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

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
    
    voice.speaker_silero(speech_text)

def setRussLayout():
    # переключение на рускую раскладку
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050,0,0x04190419)
    return(result)

def setEngLayout():
    # переключение на английскую раскладку
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050,0,0x04090409)
    return(result)



def passive():
    pass