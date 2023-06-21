from langchain.tools import YouTubeSearchTool
import ast

tool = YouTubeSearchTool()

def search_yt(query):
    results_str = tool.run(query)  # Assuming results is a string representation of a list
    results = ast.literal_eval(results_str)

    prefix = "https://youtube.com"

    links = [prefix + res for res in results]

    return links
