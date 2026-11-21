import json

# 1. 准备一个 Python 字典（比如大模型的配置）
config = {
    "model_name": "deepseek-chat",
    "temperature": 0.7,
    "is_active": True,
    "tools": ["web_search", "calculator"]
}

#1将字典转换为JSON字符串
json_str = json.dumps(config, indent=4, ensure_ascii=False)
print(json_str)
print(type(json_str))

#2将JSON字符串转换为Python字典
config_dict = json.loads(json_str)
print(config_dict)
print(type(config_dict))

#3将字典写入json文件
with open("config.json", mode = "w", encoding = "utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)
    print("配置已写入config.json文件")

#4从json文件读取配置
with open("config.json", mode = "r", encoding = "utf-8") as f:
    config_dict = json.load(f)
    print(config_dict)
