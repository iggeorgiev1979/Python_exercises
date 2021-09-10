import re


text = input()
while True:
    symbol, count = input().split()
    pattern = rf'(\{symbol}{{{count},}})'
    element = re.findall(pattern, text)
    if len(element) > 0:
        element = list(sorted(element, key=lambda x: -len(x)))
        index = text.index(element[0])
        length = len(element[0])
        print(f'Hideout found at index {index} and it is with size {length}!')
        break
