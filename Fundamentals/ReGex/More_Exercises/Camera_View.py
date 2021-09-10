import re

margins = input().split()

skip = f'{{{margins[0]}}}'
take = f'{{1,{margins[1]}}}'

pattern = rf'(?:\|\<)[^\|\<]{skip}([^\|\<]{take})'
text = input()

print(*re.findall(pattern, text), sep=', ')
