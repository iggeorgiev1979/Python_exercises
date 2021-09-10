import re

pattern = r"(\d+)"
while True:
    x = input()
    if x:
        result = re.findall(pattern, x)
        if not len(result) == 0:
            print(' '.join(result), end=' ')
    else:
        break

