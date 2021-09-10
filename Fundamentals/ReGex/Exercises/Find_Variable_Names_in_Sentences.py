import re

pattern = r"(?<=\b_)([a-zA-Z0-9]+)\b"
text = input()
result = re.findall(pattern, text)
print(*result, sep=',')
