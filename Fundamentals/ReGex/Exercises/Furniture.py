import re

patters = r"^>>([a-z]+)<<(\d+\.?\d+)!(\d+\b)"
text = input()
money = 0
furniture = []
while not text == 'Purchase':
    result = re.findall(patters, text, re.IGNORECASE)
    if not len(result) == 0:
        furniture.append(result[0][0])
        money += float(result[0][1]) * int(result[0][2])
    text = input()
print('Bought furniture:')
[print(x) for x in furniture]
print(f'Total money spend: {money:.2f}')
