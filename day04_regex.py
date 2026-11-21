import re

text = "请把这段文字里的所有邮箱发给我，我的邮箱是 admin@test.com，他的邮箱是 user@ai-dev.cn"

# 正则规则解释：
# [a-zA-Z0-9._%+-]+ 代表邮箱前缀（字母数字等组合）
# @ 就是 @ 符号
# [a-zA-Z0-9.-]+ 代表域名
# \.[a-zA-Z]{2,} 代表后缀，比如 .com 或 .cn
pattern = r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}"

# findall 会找到所有符合规则的字符串，并返回一个列表
emails = re.findall(pattern, text)
print("提取到的邮箱：", emails)