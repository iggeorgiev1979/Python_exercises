import re


def key(message: str):
    reg = r"[starSTAR]"
    return len(re.findall(reg, message))


def transform(message: str, value: int):
    return ''.join([chr(ord(x) - value) for x in message])


def register(message: str, log: dict):
    pattern = r"([^@\-\!\,\:\>]+)?@(?P<planet_name>[a-zA-Z]+)([^@\-\!\,\:\>]+)?:(?P<planet_population>\d+)([^@\-\!\,\:\>]+)?\!(?P<attack>[AD])\!([^@\-\!\,\:\>]+)?\-\>(?P<soldiers>\d+)"
    match = re.match(pattern, message)
    if match:
        el = match.groupdict()
        if el['attack'] == 'A':
            log['attacked_planets'].append(el['planet_name'])
        elif el['attack'] == 'D':
            log['destroyed_planets'].append(el['planet_name'])


text = []
for _ in range(int(input())):
    text.append(input())
status = {'attacked_planets': [], 'destroyed_planets': []}
for i in text:
    decr_message = transform(i, key(i))
    register(decr_message, status)

print(f'Attacked planets: {len(status["attacked_planets"])}')
[print(f'-> {x}') for x in sorted(status["attacked_planets"])]
print(f'Destroyed planets: {len(status["destroyed_planets"])}')
[print(f'-> {x}') for x in sorted(status["destroyed_planets"])]
