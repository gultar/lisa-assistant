# Lisa, a personal AI assistant

## Introduction
This script is a personal assistant named Lisa. It provides a conversational interface for users to interact with. Users can ask questions or give commands, and Lisa will respond accordingly. The script utilizes the Langchain library for natural language processing and conversation management.

## Prerequisites
Before running the script, please ensure that the following dependencies are installed:
- `langchain` library
- `dotenv` library
- `pyttsx3` library
- `pyttsx3` library
- `duckduckgo_search` library
- `geocoder` library

You can install the dependencies using pip:
```
pip install -r requirements.txt

```

## Setup
1. Clone the repository and navigate to the project directory.
2. Create a `.env` file in the project directory and define the following environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key. You can obtain this key by signing up on the OpenAI website.
3. Run the script using the command:
   ```
   python assistant.py
   ```

## Usage
Once the script is running, you can interact with Lisa through the command line or by using voice commands.

## Flags
You can use the following flag to change the script's behaviour:
    -t, --text: to type queries and commands
    -s, --silent: to have Lisa print out her responses, instead of having her speak them

### Text Interaction
If you prefer to use text-based interaction, follow these steps:
1. When prompted with "What can I do for you?", type your query or command.
2. Lisa will process your input and provide a response.

### Voice Interaction
If you prefer to use voice-based interaction, follow these steps:
1. Make sure your microphone is set up and working.
2. Say 'Hey', 'Attention' or 'Lisa', wait for hey acknowledgement, and speak your query or command clearly.
3. Lisa will process your speech and provide a response.

### Confirmation
After receiving your query or command, Lisa will confirm what it understood. If the confirmation is incorrect, you can correct Lisa by responding with "no". Lisa will then ask for the correct query or command.

### Exiting the Program
To stop the script and exit the program, say "cancel" or hit CTRL+C.

## Additional Information
- The script uses the `text-davinci-003` model from OpenAI for generating responses.
- The `Agent` class from Langchain is used to manage the conversation flow and generate responses.
- The `Attention` class is responsible for listening to voice commands and waking up Lisa.
- The `speak()` function is used to output the responses in voice form.
- The `listen()` function is used to convert voice input into text.
- The `make_tools()` function initializes the necessary tools used by the Agent.
- The `create_agent()` function initializes the Langchain agent with the `text-davinci-003` model and the conversation tools.
- The `ask_lisa()` function takes a query as input and generates a response using the Langchain agent.
- The `lisa_answers()` function is used to handle the output of Lisa's responses based on the user's preference (text or voice).
- The `receive_query()` function handles the user's query or command based on the input mode (text or voice).
- The `start()` function is the entry point of the script and handles the main conversation loop.

Please note that this script is a simplified implementation and may not cover all possible use cases. It serves as a starting point for building a more sophisticated personal assistant. Feel free to modify and extend the script to meet your specific requirements.