brackets = input()
opening_brackets = []
closing_brackets = {']': '[', '}': '{', ')': '('}
if len(brackets) == 1:
    print('NO')
    exit()
for el in brackets:
    if el == '(' or el == '[' or el == '{':
        opening_brackets.append(el)
    else:
        if len(opening_brackets) > 0:
            tmp = opening_brackets.pop()
        else:
            tmp = ''
        if closing_brackets[el] == tmp:
            pass
        else:
            print('NO')
            exit()
print('YES')
