import re

print(*re.findall(r"\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b", input()), sep=', ')
