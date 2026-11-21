class AIAssistant:
    def __init__(self, name, model, temperature):
        self.name = name
        self.model = model
        self.temperature = temperature
        self.count = 0

    def chat(self, question):
        self.count += 1
        print(f"模型:{self.model} | 温度:{self.temperature} 助手{self.name}正在回答:{question}")

if __name__ == '__main__':
    ai_assistant = AIAssistant("小明", "deepseek", 0.7)
    ai_assistant.chat("什么是Python?")
    ai_assistant.chat("Python有哪些应用?")
    print(f"助手{ai_assistant.name}共回答了{ai_assistant.count}个问题")
