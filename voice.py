import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speaker(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()