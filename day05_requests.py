import requests
from datetime import datetime, timedelta

print("发送GET请求")

#目标网址
url = "https://httpbin.org/get"

#获取当前时间
current_time = datetime.now()
format = "%Y-%m-%d"
current_time_str = current_time.strftime(format)

#准备参数
params = {
    "city": "Xiamen",
    "date": current_time_str
}

response_get = requests.get(url, params=params, timeout=5)
print(response_get.status_code)
data = response_get.json()
print(data["args"])


print("发送POST请求")
url = "https://httpbin.org/post"

payload = {
    "username": "duck",
    "action": "learn_requests",
    "progress": "Day 5"
}

response_post = requests.post(url, json=payload, timeout=5)

print(response_post.status_code)
data = response_post.json()
print(data["json"])










