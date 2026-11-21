#写文件
with open("note.txt", mode = "w", encoding = "utf-8") as f:
    f.write("Hello, World!\n")
    f.write("这是我写的第一个python笔记")

#读文件
with open("note.txt", mode = "r", encoding = "utf-8") as f:
    content = f.read()
    print(content)
