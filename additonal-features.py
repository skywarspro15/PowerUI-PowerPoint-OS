import speech_recognition as sr 
from gtts import gTTS 
from flask import * 
from pygame import mixer
from datetime import datetime

r = sr.Recognizer()
app = Flask(__name__)
mixer.init()


@app.route("/recognize")
def recognizeSpeech():
    try: 
        with sr.Microphone() as source:
            print("Daisy is listening...") 
            r.adjust_for_ambient_noise(source)
            voice = r.listen(source, 4)
            curPhrase = r.recognize_google(voice)
            print(curPhrase)
            return curPhrase
    except Exception as e: 
        print(e)
        return ""

@app.route("/speak")
def speakSomething(): 
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    tts = gTTS(request.args.get("m"), lang="en")
    print(request.args.get("m"))
    tts.save("audio-" + date_string + ".mp3")
    mixer.music.load("audio-" + date_string + ".mp3")
    mixer.music.play()
    return "Successfully said phrase"

if __name__ == "__main__": 
    app.run(debug=True, port=8080)
