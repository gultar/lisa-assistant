from langchain.agents import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI as OpenAI
from langchain.prompts import BaseChatPromptTemplate
from langchain import LLMChain
from langchain.schema import HumanMessage
from langchain.tools import Tool
from dotenv import dotenv_values, load_dotenv
from typing import List
from listen import listen
from speak import speak
from make_tools import make_tools
from tools.get_weather import get_weather
import argparse

load_dotenv()
env = dotenv_values(".env")

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", help="Interact with Lisa by typing",
                    action='store_true')
parser.add_argument("-s", "--silent", help="Lisa doesn't speak; she writes instead.",
                    action='store_true')
args = parser.parse_args()

is_text = args.text
is_silent = args.silent

print("Hi! I'm Lisa, your personal assistant")

class CustomPromptTemplate(BaseChatPromptTemplate):
        # The template to use
        template: str
        # The list of tools available
        tools: List[Tool]
        
        def format_messages(self, **kwargs) -> str:
            # Get the intermediate steps (AgentAction, Observation tuples)
            # Format them in a particular way
            intermediate_steps = kwargs.pop("intermediate_steps")
            thoughts = ""
            for action, observation in intermediate_steps:
                thoughts += action.log
                thoughts += f"\nObservation: {observation}\nThought: "
            # Set the agent_scratchpad variable to that value
            kwargs["agent_scratchpad"] = thoughts
            # Create a tools variable from the list of tools provided
            kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])
            # Create a list of tool names for the tools provided
            kwargs["tool_names"] = ", ".join([tool.name for tool in self.tools])
            formatted = self.template.format(**kwargs)
            return [HumanMessage(content=formatted)]


tools = make_tools()
  
template = """Complete the objective as best you can. You have access to the following tools:

    {tools}
    If you get a better understanding of a topic, please don't mention it.
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    These were previous tasks you completed:

    Begin!

    Question: {input}
    {agent_scratchpad}
"""

prompt = CustomPromptTemplate(
    template=template,
    tools=tools,
    # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
    # This includes the `intermediate_steps` variable because that is needed
    input_variables=["input", "intermediate_steps"]
)   

llm = OpenAI(temperature=0, openai_api_key=env['OPENAI_API_KEY'])
llm_chain = LLMChain(llm=llm, prompt=prompt)

tool_names = [tool.name for tool in tools]

memory = ConversationSummaryBufferMemory(llm=llm, memory_key="chat_history", return_messages=True)
memory.load_memory_variables({})
agent2 = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

def ask_lisa(query):
    answer = agent2.run(query)
    return answer

def give_answer(answer):
     if is_silent:
          print(answer)
     else:
          speak(answer)

def receive_query():
    if is_text:
        query = input("Lisa: What can I do for you?\n")
    else:
        query = listen()

    return query

while True:
    query = receive_query()
    confirm = input("User: You said '"+query+"'\nIs it correct? (Y/n)")

    if confirm == 'n':
        continue

    elif confirm == 'y' or confirm == '':
        output = ask_lisa(query)
        give_answer(output)
        memory.save_context({"input": query}, {"output": output})
           

