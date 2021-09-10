import re

pattern = r"\b([\d]{2})([-/.])([A-Z][a-z]{2})\2([\d]{4})\b"
result = re.findall(pattern, input())
for el in result:
    print(f'Day: {el[0]}, Month: {el[2]}, Year: {el[3]}')

