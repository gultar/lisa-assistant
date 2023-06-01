from langchain.agents import Tool, load_tools
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI as OpenAI
from langchain.prompts import BaseChatPromptTemplate
from langchain import LLMChain
from langchain.llms import OpenAI as OA
from langchain.schema import HumanMessage, AIMessage
from langchain.tools import Tool
from dotenv import dotenv_values, load_dotenv
from typing import List

from src.speak import speak
from src.attention import Attention
from src.listen import listen
from tools.make_tools import make_tools
from src.create_agent import create_agent
from src.parse_arguments import parse_arguments

args = parse_arguments()

is_text = args.text
is_silent = args.silent

tools = make_tools()

# The text-davinci-003 model is used since it has a higher token rate limit, and seems to respond faster,
# yet it also gives very decent and well-reflected answers when given an adequate prompt
agent = create_agent()


def ask_lisa(query):
    answer = agent.run(query)
    return answer

def lisa_answers(answer):
     if is_silent:
          print(answer)
     else:
          speak(answer)

def receive_query(message):
    
    if is_text:
        
        query = input(message)
    else:
        lisa_answers(message)
        query = listen("")

    return query


def start():
     
    print("Hi! I'm Lisa, your personal assistant")
    attention = Attention()
    while True:
        if not is_text:
            woken_up = attention.listen_for_wake_word()
        else:
            woken_up = "Lisa is ready for commands"
        if woken_up == "Lisa is ready for commands":
            query = receive_query("What can I do for you?\n")
            
            if not is_text:
                confirm = receive_query("Did you say '"+query+"'?")
                print('Confirm?', confirm)
            elif is_text:
                confirm = "yes"
            
            while "no" in confirm:
                query = receive_query("I'm listening")
                confirm = receive_query("Did you say '"+query+"'?")
                if "stop" in confirm:
                    break

            if not is_text : lisa_answers("Okay, let me check")

            output = ask_lisa(query)
            lisa_answers(output)
            
        elif woken_up == "Cancelled":
            break


start()
