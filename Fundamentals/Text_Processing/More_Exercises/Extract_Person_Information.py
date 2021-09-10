for _ in range(int(input())):
    text = input()
    name = ''
    age = ''
    for i in range(len(text)):
        if text[i] == '@':
            for j in range(i + 1, len(text)):
                name += text[j]
                if name[-1] == '|':
                    break
        elif text[i] == '#':
            for j in range(i + 1, len(text)):
                age += text[j]
                if age[-1] == '*':
                    break
    if name[-1] == '|':
        name = name[:-1]
    else:
        name = ''
    if age[-1] == '*':
        age = age[:-1]
    else:
        break
    if not name == '' and not age == '':
        print(f'{name} is {age} years old.')


