from langchain.llms import OpenAI
from dotenv import dotenv_values, load_dotenv

load_dotenv()
env = dotenv_values(".env")

def create_openai_llm(model_name="gpt-3.5-turbo", temperature=0):
    llm = OpenAI(temperature=temperature, model_name=model_name, openai_api_key=env['OPENAI_API_KEY'])
    return llm

def redact(seed_prompt="", tone_instructions="formal", creativity=0.9):
    llm = create_openai_llm(temperature=creativity)

    template = f"""
        You are a writing assistant task with redacting all kinds of texts.
        Your mission is redact in a tone that is {tone_instructions}.
        Use these instructions to guide your redaction :
            {seed_prompt}
    """
    text = llm(template)

    llm = None
    return "[Final Answer] "+text

# print(redact("An invitation letter to a wedding between a crocodile and an iguana","very aristocratic"))