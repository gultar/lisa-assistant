import requests
from bs4 import BeautifulSoup
import textwrap
from dotenv import dotenv_values, load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

load_dotenv()

def scrape_and_summarize(url):
    # Load the web page
    try:
        response = requests.get(url)
        content = response.text
        
        # Extract relevant text using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        relevant_text = soup.get_text()
        
        # Break the text into smaller chunks
        chunk_size = 4000  # Adjust the chunk size as needed
        chunks = textwrap.wrap(relevant_text, width=chunk_size)
        
        # Summarize each chunk using ChatGPT
        summarized_chunks = []
        summaries = ""
        for chunk in chunks:
            print(chunk)
            summarized_chunk = chatgpt_summarize(chunk)
            summarized_chunks.append(summarized_chunk)

            summaries += summarized_chunk+"\n\n"
        
        return summaries
    except:
        return "Oops, an error occurred"



def chatgpt_summarize(text):
    # Your code to send the text to ChatGPT for summarization
    env = dotenv_values(".env")

    # Creating an instance of the ChatOpenAI class
    llm = OpenAI(model_name="gpt-3.5-turbo-16k", temperature=0.7)
    template="""
    {text}
    You are a world-class journalist, and you will try to summarize the text above
    Format the output using Markdown
    SUMMARY:
    """

    prompt = PromptTemplate(input_variables=["text"], template=template)

    summarizer_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    # Dummy implementation (truncate the text)
    return summarizer_chain.predict(text=text)
