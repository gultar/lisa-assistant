from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import dotenv_values, load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.agents import initialize_agent
from make_tools import make_tools
from langchain.agents import AgentType

load_dotenv()
env = dotenv_values(".env")
# text-davinci-003

def _handle_error(error) -> str:
    return str(error)[:50]


def create_agent(model_name="gpt-3.5-turbo-16k", verbose=True, inputs=None, outputs=None):
    
    memory = ConversationBufferMemory(memory_key="chat_history")
    
    if outputs is not None:
        memory.save_context(inputs=inputs, outputs=outputs)
    
    llm = ChatOpenAI(temperature=0.5, model_name=model_name, openai_api_key=env['OPENAI_API_KEY'])

    tools = make_tools()

    agent = initialize_agent(
            tools, 
            llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            verbose=verbose, 
            memory=memory,
            handle_parsing_errors=True,
            max_iterations=99,
            timeout=9999
        )

    return agent, memory

