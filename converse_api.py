import os
from openai import OpenAI
import json
import base64

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

print("\n----A basic call to the OpenAI API----\n")

message_list = []

initial_message = {
    "role": "user",
    "content": "How are you today?"
}

message_list.append(initial_message)

response = client.chat.completions.create(
    model="gpt-4o",  # Using GPT-4 with vision capabilities
    messages=message_list,
    max_tokens=2000,
    temperature=0
)

response_message = response.choices[0].message

print(json.dumps(response_message.model_dump(), indent=4))

#
print("\n----Alternating user and assistant messages----\n")

message_list.append(response_message.model_dump())
print(json.dumps(message_list, indent=4))

#
print("\n----Including an image in a message----\n")

with open("image.webp", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

image_message = {
    "role": "user",
    "content": [
        {"type": "text", "text": "Image 1:"},
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/webp;base64,{image_base64}"
            }
        },
        {"type": "text", "text": "Please describe the image."}
    ]
}

message_list.append(image_message)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=message_list,
    max_tokens=2000,
    temperature=0
)

response_message = response.choices[0].message
print(json.dumps(response_message.model_dump(), indent=4))

message_list.append(response_message.model_dump())

#
print("\n----Setting a system prompt----\n")

summary_message = {
    "role": "user",
    "content": "Can you please summarize our conversation so far?"
}

message_list.append(summary_message)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Please respond to all requests in the style of a pirate."},
        *message_list
    ],
    max_tokens=2000,
    temperature=0
)

response_message = response.choices[0].message
print(json.dumps(response_message.model_dump(), indent=4))

message_list.append(response_message.model_dump())

#
print("\n----Getting response metadata and token counts----\n")

print("Finish Reason:", response.choices[0].finish_reason)
print("Usage:", json.dumps(response.usage.model_dump(), indent=4))