import json

class AIAssistant:
    def __init__(self, name, model, temperature):
        self.name = name
        self.model = model
        self.temperature = temperature

#实例化一个对象
my_assistant = AIAssistant("小明", "deepseek", 0.7)

#定义一个对象转字典函数
def obj_to_dict(obj):
    if isinstance(obj, AIAssistant):
        return {
            "name": obj.name,
            "model": obj.model,
            "temperature": obj.temperature,
            #建议加个类型标记方便还原
            "__type__": "AIAssistant"
        }
    raise TypeError("该对象类型不属于AIAssistant类,无法处理")

json_str = json.dumps(my_assistant, default=obj_to_dict, indent=4, ensure_ascii=False)
print(json_str)

#将json重新变成对象
obj_dict = json.loads(json_str)
def dict_to_obj(obj_dict):
    if "__type__" in obj_dict and obj_dict["__type__"] == "AIAssistant":
        return AIAssistant(obj_dict["name"], obj_dict["model"], obj_dict["temperature"])
    raise TypeError("该字典类型不属于AIAssistant类,无法处理")

new_ai_assistant = json.loads(json_str, object_hook=dict_to_obj)
print(new_ai_assistant.name, new_ai_assistant.model, new_ai_assistant.temperature)
