import re
result = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", input())
print(*result, sep=' ')
