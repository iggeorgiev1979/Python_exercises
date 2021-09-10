text = input()
punch_power = 0
result = ''
for i in range(len(text)):
    el = text[i]
    if el == '>':
        punch_power += int(text[i + 1])
    if punch_power == 0 or el == '>':
        result += el
    else:
        punch_power -= 1
print(result)
