
import queue
import sounddevice as sd
import vosk
import pyttsx3
import json
import voice 
import words
from commands import * 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
q = queue.Queue()

model = vosk.Model('vosk-model-small-ru-0.22')
try:

    device = sd.default.device= 1, 3 #sd.default.device = 1, 3 /////input, output[1, 4]
    samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
except:
    voice.speaker_silero('Включи Микрофон')
    sys.exit(1)


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, vectorizer, clf):
    trg = words.triggers.intersection(data.split())

    if not trg :
        return
    data.replace(list(trg)[0], '')

    #получаем вектор полученного текста
    #сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    
    func_name = answer.split()[0]
    voice.speaker_silero(answer.replace(func_name, ''))
    exec(func_name + '()')


def main():

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set
    with sd.RawInputStream(samplerate=samplerate, blocksize = 48000, device=device[0],
            dtype="int16", channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
            

if __name__=='__main__':
    main()
