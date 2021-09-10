import re

pattern = r"(^|(?<=\s))([a-z0-9]+)(\.?\-?\_?[a-z0-9]+)+@([a-z]+)\-?[a-z]+(\.[a-z]+\-?[a-z]+)+($|(?=\s)|(?=\.)|(?=\,))"

text = input()
result = [x.group() for x in re.finditer(pattern, text, re.IGNORECASE)]
print(*result, sep='\n')
