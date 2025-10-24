
import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import google.generativeai as genai

apikey = "apna daal bhnchod ruddha"
genai.configure(api_key=apikey)

model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()


recognizer=sr.Recognizer()
engine=pyttsx3.init(driverName='nsss')  

def ai(command):
    apikey = "apna daal bhnchod ruddha"
    genai.configure(api_key=apikey)

    model=genai.GenerativeModel("gemini-2.0-flash")
    chat=model.start_chat()

    reponse=chat.send_message(command)
    reply_text = reponse.text if hasattr(reponse, "text") else str(reponse)
    print(f"AI: {reply_text}")
    #speak(reply_text)

    return reply_text   

    

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")
    

def process_command(c):
    if c.lower()=="open youtube":
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif c.lower()=="open google":
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music.music[song]
        webbrowser.open(link)
    else:
        output=ai(c)
        speak(output)



if __name__=="__main__":
    speak("initializing jarvis")
    r=sr.Recognizer()
    while True:
    # Take microphone input from the user
    #listens for the wake word
          
        
    
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source, timeout=3, phrase_time_limit=5)
            # Recognize speech using Google Speech Recognition
                word=r.recognize_google(audio)
                print(f"heard..{word}")

                if(word.lower()=="jarvis"):
                    speak("yes deep sir")
                    #listen to command
                    with sr.Microphone() as source:
                        print("jarvis active..")
                        audio=r.listen(source, timeout=3, phrase_time_limit=5)
                        command=r.recognize_google(audio)
                        process_command(command)

        except Exception as e:
            import traceback
            print(f"Could not understand the audio, please try again. Error: {e}")
            traceback.print_exc()



  