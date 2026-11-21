from pathlib import Path

#拿到当前目录
current_dir = Path(".")
print(current_dir.absolute())

#遍历当前目录的所有txt文件
for file in current_dir.glob("*.txt"):
    old_name = file.stem
    new_name = f"new_{old_name}.txt"
    file.rename(new_name)
    print(f"Renamed {file.name} to {new_name}")
