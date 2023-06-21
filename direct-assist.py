from src.create_agent import create_agent

# The text-davinci-003 model is used since it has a higher token rate limit, and seems to respond faster,
# yet it also gives very decent and well-reflected answers when given an adequate prompt
agent = create_agent()


def ask_lisa(query):
    answer = agent.run(query)
    return answer



prompt = """
Please build a short course to learn how to create a text embedding model with Tensorflow and Python.
Provide all of the steps required in a Jupyter Notebook. Explain in detail each of the steps needed.
Start by explaining word embeddings, pre-trained models, training and fine-tuning, and practical applications
"""

print(ask_lisa(prompt))