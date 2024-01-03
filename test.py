
from typing import List
from openai import OpenAI
import numpy as np
import os
# from tenacity import retry, stop_after_attempt, wait_random_exponential
from utils import *
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

# 根据key的前两位判断应该使用哪个baseurl
if "fk" == openai_api_key[:2]:
   baseurl = "https://stream.api2d.net/v1"
else:
   baseurl = "https://api.openai.com/v1"

client = OpenAI(api_key=openai_api_key,base_url=baseurl)

# openai.api_base = "https://key.aiskt.com/v1"



def ChatGPT_request(prompt): 

  # temp_sleep()
  # try: 
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106", 
  response_format={ "type": "json_object" },
  messages=[{"role": "user", "content": prompt}]
  )
  return completion.choices[0].message.content
  


# wait=wait_random_exponential(min=1, max=20) 表示每次重试之间的等待时间是一个随机的指数增长的数，最小是 1 秒，最大是 20 秒
# stop=stop_after_attempt(2) 表示最多重试 2 次
# @retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(2))
def get_embedding(text: str, model="text-similarity-davinci-001", **kwargs) -> List[float]:

    # replace newlines, which can negatively affect performance.
    text = text.replace("\n", " ")

    response = client.embeddings.create(input = [text], model=model,**kwargs)

    return response.data[0].embedding

def cosine_similarity(x,y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom

if __name__ == "__main__":
    # text = "I enjoy walking with my cute dog, but I don't like walking with my cat.提取这段话中的动物，返回为JSON格式"
    # print(ChatGPT_request(text))
    text = "生命"
    print(get_embedding(text, model = "text-embedding-ada-002"))






