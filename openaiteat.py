from openai import OpenAI
import openai
import os
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"
key = "sk-CSRmn1xp9MtIp8bHF0457c308f374121Bd0733FeA3239558"
# os.environ["OPENAI_API_BASE"] = "https://key.aiskt.com"
client = OpenAI(api_key= key, base_url="https://key.aiskt.com")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion)