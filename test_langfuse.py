from langfuse.openai import OpenAI
import os
 
# Get keys for your project from the project settings page
# https://cloud.langfuse.com
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-df330244-dba5-4201-affb-1deef764599e"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-dcc609b8-1720-4f6d-bf7d-bdc5e3dc2605"
os.environ["LANGFUSE_HOST"] = "http://127.0.0.1:4000/" 

# Configure the OpenAI client to use http://localhost:11434/v1 as base url 
client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)
 
response = client.chat.completions.create(
  model="llama3.2:3b-instruct-q8_0",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who was the first person to step on the moon?"},
    {"role": "assistant", "content": "Neil Armstrong was the first person to step on the moon on July 20, 1969, during the Apollo 11 mission."},
    {"role": "user", "content": "What were his first words when he stepped on the moon?"}
  ]
)
print(response.choices[0].message.content)