import re


def weather(text: str):
    pattern = r'([A-Z]{2})(\d+\.\d+)([a-zA-Z]+)(?:\|)'
    result = re.findall(pattern, text)
    return result


def register(log: dict, town: list):
    name, temp, cond = town
    log[name] = [temp, cond]


towns_dict = {}
info = input()
while not info == 'end':
    town_list = weather(info)
    if not len(town_list) == 0:
        register(towns_dict, town_list[0])
    info = input()

[print(f'{i} => {float(j[0]):.2f} => {j[1]}') for i, j in sorted(towns_dict.items(), key=lambda x: x[1][0])]
