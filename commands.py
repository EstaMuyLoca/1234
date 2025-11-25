import os, webbrowser, sys, requests, subprocess, voice
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speaker(text):
    engine.say(text)
    engine.runAndWait()

def browser():
    webbrowser.open('https://www.youtube.com', new =2)
    #print('браузер запущен')

def game():
    subprocess.Popen('C:/Program Files')
    #print("игра запущена")

def offpc():
    os.system('shutdown /s')
    #print("пк выключен")

def weather():
    try:
        params= {"q": "Kazan", "appid": '9e1551e8704efdd171e53c2db37c21c5',"units":"metric", "lang": "ru"} 
        responce = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params=params)
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
        if not responce:
            raise
        w = responce.json()
    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')
def offBot():
    sys.exit()

def passive():
    pass