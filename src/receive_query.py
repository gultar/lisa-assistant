from .listen import listen
from .speak import speak

def receive_query(message, is_text=True):
    
    if is_text:
        
        query = input(message)
    else:
        lisa_answers(message)
        query = listen("Listening...")

    return query

def lisa_answers(answer, is_silent=False):
     if is_silent:
          print(answer)
     else:
          speak(answer)