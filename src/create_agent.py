from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import dotenv_values, load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.agents import initialize_agent
from make_tools import make_tools
from langchain.agents import AgentType

def create_agent(model_name="text-davinci-003", verbose=True):
    load_dotenv()
    env = dotenv_values(".env")

    memory = ConversationBufferMemory(memory_key="chat_history")
    llm = OpenAI(temperature=0, model_name=model_name, openai_api_key=env['OPENAI_API_KEY'])

    tools = make_tools()

    agent = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=verbose, memory=memory)

    return agent
