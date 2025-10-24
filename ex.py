import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
engine=pyttsx3.init(driverName='nsss')
def speak(text):
    

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(e)

with sr.Microphone() as source:
    print("listening")
    audio=r.listen(source, timeout=5, phrase_time_limit=5)
    word=r.recognize_google(audio)
    print(f"heard: {word}")
    try:
        if(word.lower()=="kundan"):
            speak("yes deep papa")
    except Exception as e:
        print(e)

