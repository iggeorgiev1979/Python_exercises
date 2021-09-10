import re

pattern = r"www\.[a-zA-Z0-9]+(\-?\.?[a-zA-Z0-9]+)+(\.[a-z]+)+"
print_result = []
while True:
    text = input()
    if text == '':
        break
    else:
        result = [x.group() for x in re.finditer(pattern, text)]
        if not len(result) == 0:
            print_result.append(result[0])
print(*print_result, sep='\n')
