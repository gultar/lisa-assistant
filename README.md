# Lisa - Personal AI Assistant

## Introduction
Lisa is a personal AI assistant that provides a conversational interface for users to interact with. It utilizes natural language processing and conversation management to understand user queries and provide relevant responses.

## Requirements
Before running the script, make sure you have the following dependencies installed:
- `langchain` library
- `dotenv` library
- `pyttsx3` library
- `duckduckgo_search` library
- `geocoder` library

You can install the dependencies using the following command:
```
pip install -r requirements.txt
```

## Setup
1. Clone the repository and navigate to the project directory.
2. Create a `.env` file in the project directory and set the following environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key obtained from the OpenAI website.
   - `GOOGLE_CSE_ID`: Your Google Custom Search Engine ID.
   - `GOOGLE_API_KEY`: Your Google API key.
3. Run the assistant using the command:
   ```
   python assistant.py
   ```

## Usage
Once the script is running, you can interact with Lisa through the command line or voice commands, depending on the chosen mode.

## Flags
The script supports the following flags:
- `-t` or `--text`: Enables text-based interaction.
- `-s` or `--silent`: Disables speech synthesis for responses.

### Text Interaction
If you prefer text-based interaction, follow these steps:
1. When prompted with "What can I do for you?", type your query or command.
2. Lisa will process your input and provide a response.

### Voice Interaction
If you prefer voice-based interaction, follow these steps:
1. Ensure that your microphone is set up and working.
2. Say "Hey," "Attention," or "Lisa" to wake up Lisa and wait for the acknowledgement sound.
3. Speak your query or command clearly.
4. Lisa will process your speech and provide a response.

### Confirmation
After receiving a query or command, Lisa will confirm what it understood. If the confirmation is incorrect, you can respond with "no" to provide the correct query or command.

### Exiting the Program
To stop the script and exit the program, say "cancel" or press `CTRL+C`.

## Additional Information
- Lisa uses the `gpt-3.5-turbo` model from OpenAI to generate responses.
- The Langchain library is utilized for conversation management and NLP tasks.
- The `Agent` class from Langchain manages the conversation flow and generates responses.
- The `Attention` class handles voice commands and wakes up Lisa.
- The `speak()` function outputs responses in voice form.
- The `listen()` function converts voice input into text.
- The `make_tools()` function initializes the tools used by the Agent for various tasks.
- The `create_agent()` function initializes the Langchain agent with the `gpt-3.5-turbo` model and conversation tools.
- The `ask_lisa()` function takes a query as input and generates a response using the Langchain agent.
- The `lisa_answers()` function handles the output of Lisa's responses based on the user's preference (text or voice).
- The `receive_query()` function manages user queries or commands based on the input mode (text or voice).
- The `start()` function serves as the entry point of the script and handles the main conversation loop.

Please note that this implementation is a simplified version and may not cover all possible use cases. It can be extended and modified to suit specific requirements for building a more sophisticated personal assistant.