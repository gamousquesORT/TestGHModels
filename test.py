import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def create_message_item(role, content):
    return {
            "role": role,
            "content": content,
        }
    

chat_log_items = []
chat_log_items.append(create_message_item("system", "You are a helpful assistant."))
chat_log_items.append(create_message_item("user", "What is the capital of France?"))



def get_message_content(text):
    message_in = []
    message_in.append(create_message_item("system", "You are a helpful assistant."))
    message_in.append(create_message_item("user", text))

    response = client.chat.completions.create(
    messages=message_in,
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.
    )
    return response.choices[0].message.content

#print(response.choices[0].message.content)