import re


def find_health(text: str):
    reg = r"[^0-9\+\-\*\/\.]"
    return sum([ord(x) for x in re.findall(reg, text)])


def find_damage(text: str):
    reg = r"(?:\+|-)?[0-9]+(?:\.[0-9]+)?"
    reg_3 = r"[\*\/]"
    numbers = [float(x) for x in re.findall(reg, text)]
    damage = sum(numbers)
    manipulators = re.findall(reg_3, text)
    for i in manipulators:
        if i == '*':
            damage *= 2
        else:
            damage /= 2

    return damage


demons_list = input().split(',')
demons_list = [x.strip() for x in demons_list]
for demon in sorted(demons_list):
    print(f'{demon} - {find_health(demon)} health, {find_damage(demon):.2f} damage')
