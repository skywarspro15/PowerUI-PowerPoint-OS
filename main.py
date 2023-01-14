import speech_recognition as sr 
from gtts import gTTS 
from flask import * 

r = sr.Recognizer()
app = Flask(__name__)


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
    tts = gTTS(request.args.get("m"), lang="en")
    print(request.args.get("m"))
    tts.save("audio.wav")
    return send_file(
         "audio.wav", 
         mimetype="audio/wav", 
         as_attachment=False, 
         download_name="audio.wav")

if __name__ == "__main__": 
    app.run(debug=True, port=8080)
