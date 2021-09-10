def take_odd(text: str):
    result = ''
    for i in range(len(text)):
        if not i % 2 == 0:
            result += text[i]
    if result:
        print(result)
        return result
    return text


def cut(text: str, start: int, end: int):
    sub_str = text[start:start + end]
    start = text.find(sub_str)
    result = text[:start] + text[start + end:]
    print(result)
    return result


def substitute(text: str, sub_str: str, replacement: str):
    if sub_str in text:
        text = text.replace(sub_str, replacement)
        print(text)
    else:
        print("Nothing to replace!")
    return text


password = input()
command = input()
while not command == 'Done':
    command = command.split()
    if command[0] == 'TakeOdd':
        password = take_odd(password)
    elif command[0] == 'Cut':
        password = cut(password, int(command[1]), int(command[2]))
    elif command[0] == 'Substitute':
        password = substitute(password, command[1], command[2])
    command = input()
print(f"Your password is: {password}")
