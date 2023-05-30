from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import BaseChatPromptTemplate
from langchain import SerpAPIWrapper, LLMChain
from langchain.chat_models import ChatOpenAI
from typing import List, Union
from langchain.schema import AgentAction, AgentFinish, HumanMessage
from langchain.tools import BaseTool, StructuredTool, Tool
import re
from getpass import getpass
from duckduckgo_search import DDGS
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from typing import Optional, Type
from dotenv import dotenv_values, load_dotenv
from langchain.chat_models import ChatOpenAI as OpenAI
from listen import listen
from speak import speak
from time import sleep

load_dotenv()
env = dotenv_values(".env")

print("Hi! I'm Lisa, your personal assistant")

def search_ddg(query: str)-> str: 
    """Searches DuckDuckGo and returns the five topmost results"""
    ddgs = DDGS()

    keywords = query
    ddgs_text_gen = ddgs.text(keywords, region='wt-wt', safesearch='Off', timelimit='y')
    results = []
    for r in ddgs_text_gen:
        results.append(r)

    five_most = results[0:5]
    response = ""
    for result in five_most:
        # response += f"Title: {result['title']}\nURL:{result['href']}\nDescription:{result['body']}\n\n"
        response += f"{result['body']}\n{result['href']}\n\n"

    return response

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
        
class CustomOutputParser(AgentOutputParser):
        
        def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
            # Check if agent should finish
            if "Final Answer:" in llm_output:
                return AgentFinish(
                    # Return values is generally always a dictionary with a single `output` key
                    # It is not recommended to try anything else at the moment :)
                    return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                    log=llm_output,
                )
            # Parse out the action and action input
            regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
            match = re.search(regex, llm_output, re.DOTALL)
            if not match:
                final = "Final Answer:"+llm_output
                return self.parse(final)
            action = match.group(1).strip()
            action_input = match.group(2)
            # Return the action and action input
            return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)

def ask_lisa(query):

    tools = [
        Tool(
            name = "Search",
            func=search_ddg,
            description="useful for when you need to answer questions about current events"
        )
    ]
    
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
    {agent_scratchpad}"""

    
        
    prompt = CustomPromptTemplate(
        template=template,
        tools=tools,
        # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
        # This includes the `intermediate_steps` variable because that is needed
        input_variables=["input", "intermediate_steps"]
    )
        
    output_parser = CustomOutputParser()
    llm = OpenAI(temperature=0, openai_api_key=env['OPENAI_API_KEY'])
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    tool_names = [tool.name for tool in tools]
    agent = LLMSingleActionAgent(
        llm_chain=llm_chain, 
        output_parser=output_parser,
        stop=["\nObservation:"], 
        allowed_tools=tool_names
    )
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
    answer = agent_executor.run(query)

    return answer

while True:
    query = listen()
    confirm = input("You said : "+query+", correct? (Y/n)")

    if confirm == 'n':
        continue
    else:

        if confirm == 'y' or confirm == '':
            output = ask_lisa(query)
            speak(output)
            break
        
        sleep(3)
        output = ask_lisa(query)
        speak(output)
        break
