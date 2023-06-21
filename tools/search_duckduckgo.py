from duckduckgo_search import DDGS

def search_ddg(query: str)-> str: 
    """Searches DuckDuckGo and returns the N topmost results"""
    ddgs = DDGS()

    keywords = query
    ddgs_text_gen = ddgs.text(keywords, region='wt-wt', safesearch='Off', timelimit='y')
    results = []
    for r in ddgs_text_gen:
        results.append(r)

    print('Results quantity',len(results))

    top_most = results[0:20]
    response = ""
    for result in top_most:
        response += f"Title: {result['title']}\nURL:{result['href']}\nDescription:{result['body']}\n\n"
        # response += f"{result['body']}\n{result['href']}\n\n"

    return response
