from langchain.tools import Tool
from tools.search_duckduckgo import search_ddg
from tools.get_weather import get_weather
from langchain.utilities import WikipediaAPIWrapper
from src.receive_query import receive_query
from langchain.utilities import GoogleSearchAPIWrapper
from tools.search_yt import search_yt
import os
from dotenv import dotenv_values, load_dotenv
from tools.builder import build_application
from tools.scrape_and_summarize import scrape_and_summarize
# from langchain.tools import ShellTool


load_dotenv()
env = dotenv_values(".env")

wikipedia = WikipediaAPIWrapper()
search = GoogleSearchAPIWrapper()


os.environ["GOOGLE_CSE_ID"] = env["GOOGLE_CSE_ID"]
os.environ["GOOGLE_API_KEY"] = env["GOOGLE_API_KEY"]


def make_tools():
    tools = [
        Tool(
            name = "Search",
            func=search_ddg,
            description="useful for when you need to answer questions about current events"
        ),
        Tool(
            name = "Weather",
            func=get_weather,
            description="""
            useful for when you need to answer questions about the weather. 
            The API returns data at the latitude and longitude of the location, 
            and weather data over time. You need to pass a city name to the function.
            Otherwise, the city by default is Quebec.
            """
        ),
        Tool(
            name="Wikipedia",
            func=wikipedia.run,
            description="""
            Useful for when you need to answer questions about general knowledge, or when you 
            need to look for information about a general topic
            """
        ),
        Tool(
            name="Youtube Search",
            description="Search Youtube for a relevant video.",
            func=search_yt
        ),
        Tool(
            name="Visit URL",
            description="Useful for when you need to research a topic in depth. This tool only takes a url as argument.",
            func=scrape_and_summarize
        ),
        # Tool(
        #     name="Application Builder",
        #     func=build_application,
        #     description="""
        #     A tool that enables the AI Assistant to build applications based on very
        #     specific, and detailled instructions to be passed to an AI model.
        #     Describe the application to be created in rich detail, and 
        #     you must specify exclusions, and custom details.
        #     """
        # )

    ]
    return tools
