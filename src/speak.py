import pyttsx3

from gtts import gTTS
import playsound

def speak(text):
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()
    speech = gTTS(text=text, lang="en",slow=False,tld="com.in")
    speech.save("test.mp3")
    playsound.playsound("test.mp3")

# def tryout():
#     speech = gTTS(text="Hello there", lang="en", slow=False, tld="com.au")
#     speech.save("test.mp3")
#     playsound.playsound("test.mp3")


# tryout()