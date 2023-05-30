import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak anything: ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Sorry, could not recognize what you said.")
            return False
