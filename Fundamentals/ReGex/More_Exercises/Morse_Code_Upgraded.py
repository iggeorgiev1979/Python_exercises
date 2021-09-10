message = input().split('|')

code = 0
for part in message:
    sequence = ''
    for el in part:
        if sequence == '' or el == sequence[-1]:
            sequence += el
        else:
            if len(sequence) > 1:
                code += len(sequence)
            sequence = el
        if el == '0':
            code += 3
        else:
            code += 5
    if len(sequence) > 1:
        code += len(sequence)
    print(chr(code), end='')
    code = 0
print()
