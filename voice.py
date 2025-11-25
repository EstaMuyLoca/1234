import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 180)
# выберите нужный voice.id для русского голоса
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')
def speaker(text):

    engine.say(text)
    engine.runAndWait()