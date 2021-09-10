text = input()
power = 0
for i in range(len(text)):
    if not power == 0:
        if text[i] == '>':
            print(text[i], end='')
    else:
        print(text[i], end='')
    if text[i] == '>':
        power += int(text[i + 1])
    if not text[i] == '>':
        if not power == 0:
            power -= 1
print()
