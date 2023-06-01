from langchain.tools import Tool
from tools.search_duckduckgo import search_ddg
from tools.get_weather import get_weather
from langchain.utilities import WikipediaAPIWrapper

wikipedia = WikipediaAPIWrapper()

print()

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
    ]
    return tools
