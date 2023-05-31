from duckduckgo_search import DDGS

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
        response += f"Title: {result['title']}\nURL:{result['href']}\nDescription:{result['body']}\n\n"
        # response += f"{result['body']}\n{result['href']}\n\n"

    return response