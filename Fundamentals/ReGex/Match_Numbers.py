import re

pattern = r"(^|(?<=\s))(-?\d+)(\.\d+)?($|(?=\s))"
text = input()
result = [x.group() for x in re.finditer(pattern, text)]
print(*result, sep=' ')
