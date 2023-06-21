from src.attention import Attention
from src.create_agent import create_agent
from src.parse_arguments import parse_arguments
from src.receive_query import lisa_answers, receive_query

args = parse_arguments()

is_text = args.text
is_silent = args.silent

agent, memory = create_agent()

def ask_lisa(query):
    answer = agent.run(query)
    return answer


def start():
     
    print("Hi! I'm Lisa, your personal assistant")
    attention = Attention()
    while True:
        if not is_text:
            woken_up = attention.listen_for_wake_word()
        else:
            woken_up = "Lisa is ready for commands"
        if woken_up == "Lisa is ready for commands":
            query = receive_query("What can I do for you?\n", is_text)
            
            if not is_text:
                confirm = receive_query("Did you say '"+query+"'?", is_text)
                print('Confirm?', confirm)
            elif is_text:
                confirm = "yes"
            
            while "no" in confirm:
                query = receive_query("I'm listening", is_text)
                confirm = receive_query("Did you say '"+query+"'?", is_text)
                if "stop" in confirm:
                    break

            if not is_text : lisa_answers("Okay, let me check")

            output = ask_lisa(query)
            lisa_answers(output, is_text)
            
        elif woken_up == "Cancelled":
            break


start()
