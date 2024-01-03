
import requests
import json

def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=mfhIIacaGZlm9UILr7uQ6LIR&client_secret=hgh2a1TOTqWZGO0Z95YeduGlYG4MKpGN"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def main():   

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/qianfan_chinese_llama_2_13b?access_token=" + get_access_token()
    
    payload = json.dumps({
         "messages": [
            {
                "role": "user",
                "content": "介绍下文心千帆"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

if __name__ == '__main__':
    main()