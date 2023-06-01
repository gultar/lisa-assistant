import speech_recognition as sr

def listen(message):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(message)
        # recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except:
            print("Sorry, could not recognize what you said.")
            return ""
        
