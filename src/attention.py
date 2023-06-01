import speech_recognition as sr
from speech_recognition import UnknownValueError
import time


class Attention:
    def __init__(self, wake_words=["hey","Lisa","hey listen","wake up","attention"]):
        self.wake_words = wake_words
        self.is_listening = True
        

    def listen_for_wake_word(self):
        self.is_listening = True
        def my_callback_function(recognizer, audio):
            # This will be called when audio is recognized
            # no loops in here, it'll be called once every time a chunk of audio is recognized                          
            try:
                
                result = recognizer.recognize_google(audio)
                
                if result in self.wake_words:
                    self.is_listening = False
                    print('Activated')
                    return 'Lisa is listening!'
                else:
                    print(result)
            except UnknownValueError as err:
                print(err)
                print("!")

        try:
            # set up our recognizer
            r = sr.Recognizer()
            # r.recognize_whisper_api()
            microphone = sr.Microphone()
            with microphone as source:
                r.adjust_for_ambient_noise(source)
            # now we pass the name of our callback function as an argument
            stop_bg_listening = r.listen_in_background(microphone, my_callback_function)
            
            # Block forever
            while self.is_listening:
                time.sleep(0.1)

            stop_bg_listening()
            return "Lisa is ready for commands"
        except Exception as err:
            print('Got an error', err)
            return "Cancelled"
