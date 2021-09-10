import re

names_list = input().split(', ')
names = {}
text = input()
pattern_1 = r"([a-zA-Z])"
pattern_2 = r"(\d)"
while not text == 'end of race':
    racer = ''.join(re.findall(pattern_1, text))
    points = sum([int(x) for x in re.findall(pattern_2, text)])
    if racer in names_list:
        if racer not in names.keys():
            names[racer] = 0
        names[racer] += points
    text = input()
names = sorted(names.items(), key=lambda x: -x[1])
print(f'1st place: {names[0][0]}')
print(f'2nd place: {names[1][0]}')
print(f'3rd place: {names[2][0]}')
