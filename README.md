**OpenAI API Interaction with GPT-4 (Vision) Example**
This repository provides an example of how to interact with OpenAI's GPT-4 model (with vision capabilities) using Python. The script demonstrates a basic chat, image processing, and message history management using OpenAI's chat completion API. It also showcases how to set a system prompt and retrieve response metadata and token usage.
**Features**
1.	Basic Chat Completion: Sends a basic message ("How are you today?") to the OpenAI API and retrieves a response.
2.	Alternating Messages: Demonstrates how to alternate between user and assistant messages in a conversation.
3.	Image Integration: Sends an image (in base64 format) along with a text request and retrieves a response describing the image.
4.	System Prompts: Changes the assistant's behavior by setting a system prompt (e.g., asking for responses in a pirate style).
5.	Response Metadata: Retrieves and displays response metadata and token usage.
**Prerequisites**
•	Python 3.7+
•	An OpenAI API key (you can get one from OpenAI)
•	An image file (image.webp) to include in your requests
**Installation**
1.	Clone the repository:
git clone https://github.com/bdeva1975/openai-gpt4-vision-example.git
cd openai-gpt4-vision-example
2.	Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3.	Install the required dependencies:
pip install openai python-dotenv
4.	Create a .env file in the root of the project with your OpenAI API key:
OPENAI_API_KEY=your-openai-api-key
5.	Place an image file named image.webp in the same directory as the script.
**Usage**
1.	Run the script:
python openai_gpt4_vision_example.py
2.	The script will:
o	Send an initial message to the GPT-4 model
o	Alternate between user and assistant messages
o	Send an image and ask the model to describe it
o	Set a system prompt to change the assistant's response style
o	Retrieve and display response metadata and token usage
**Example Output**
Here is an example of what the output might look like:
----A basic call to the OpenAI API----

{
    "role": "assistant",
    "content": "I'm doing well, thank you for asking! How can I assist you today?"
}

----Alternating user and assistant messages----

[    {"role": "user", "content": "How are you today?"},    {"role": "assistant", "content": "I'm doing well, thank you for asking! How can I assist you today?"}]

----Including an image in a message----

{
    "role": "assistant",
    "content": "It looks like an image with bright colors and intricate details. Please provide more context if needed."
}

----Setting a system prompt----

{
    "role": "assistant",
    "content": "Arrr! A fine summary it be! Ye asked how I be doin', sent me a fine image, and now I be ready for more adventures! What be next, matey?"
}

----Getting response metadata and token counts----

Finish Reason: stop
Usage: {
    "prompt_tokens": 123,
    "completion_tokens": 45,
    "total_tokens": 168
}
**Customization**
•	System Prompt: You can modify the behavior of the assistant by changing the system prompt (e.g., asking it to speak like a pirate or any other custom role).
•	Image Format: Ensure that the image is in a valid format (image.webp), and you can replace it with other image formats if needed.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
For any questions or issues, feel free to reach out by creating an issue on GitHub or contacting me at [bdeva1975@gmail.com].


