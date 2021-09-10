import re


def find_mine(text: str):
    pattern = r'\<..\>'
    mine = set(re.findall(pattern, text))
    if mine:
        return mine


def calculate_power(text: str):
    result = abs(ord(text[1]) - ord(text[2]))
    return result


def clear_mine(text: str, mine: str, number_power: int):
    pattern = rf'.{{,{number_power}}}{mine}.{{,{number_power}}}'
    element = set(re.findall(pattern, text))
    for el in element:
        text = re.sub(rf'{el}', '_' * len(el), text)
    return text


mine_field = input()
bombs = find_mine(mine_field)
if bombs:
    for bomb in bombs:
        power = calculate_power(bomb)
        mine_field = clear_mine(mine_field, bomb, power)

print(mine_field)
