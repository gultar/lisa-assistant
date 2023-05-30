from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit
from langchain.chat_models import ChatOpenAI as OpenAI
from langchain.tools.playwright.utils import (
    create_async_playwright_browser,
)
from langchain.agents import initialize_agent, AgentType
from dotenv import dotenv_values, load_dotenv
import nest_asyncio 
from langchain.tools import tool
from langchain.agents import load_tools
from langchain.tools import StructuredTool

# tools[0].name = "Google Search"
# print(tools)
from duckduckgo_search import DDGS
from typing import Optional, Type
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun


load_dotenv()
env = dotenv_values(".env")

nest_asyncio.apply()
async_browser = create_async_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()
# 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
llm = OpenAI(temperature=0, openai_api_key=env['OPENAI_API_KEY'])
tools_by_name = {tool.name: tool for tool in tools}
navigate_tool = tools_by_name["navigate_browser"]
get_elements_tool = tools_by_name["get_elements"]

agent_chain = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True, 
    max_iterations=5
    )



class CustomSearchTool(BaseTool):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events"

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""
        return search_ddg(query)
    
    async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")


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


tool = Tool.from_function(
        func=search_ddg,
        name = "Search",
        return_direct=True,
        verbose=True,
        description="useful for when you need to answer questions about current events"
        # coroutine= ... <- you can specify an async method if desired as well
    ),

agent = initialize_agent(tool, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
output = agent.run("navigate to the following address and return the HTML code for the element id #chatbot: https://huggingface.co/spaces/Intel/Q8-Chat")
# print(agent.run(" Give me a summary of theses results: "+output))
# async def main():
#     result = await agent_chain.arun("""
#     Can you tell me about LangChain by looking on https://www.duckduckgo.com?
#     The selector for the search bar is #search_form_input_homepage, and the selector the search button is #search_button_homepage
#     """)
#     print(result)

# asyncio.run(main())

