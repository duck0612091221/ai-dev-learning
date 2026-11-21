from pathlib import Path

p = Path(".")
print(p.absolute())


file_path = Path("test.txt")

if file_path.exists():
    print("文件存在，可以读取！")
else:
    print("哎呀，电脑里根本没有这个文件！")