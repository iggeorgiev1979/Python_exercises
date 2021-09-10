def insert_space(text: str, index: int):
    text = text[:index] + ' ' + text[index:]
    print(text)
    return text


def reverse(text: str, sub_str: str):
    if sub_str in text:
        index = text.index(sub_str)
        text = text[:index] + text[index + len(sub_str):] + sub_str[::-1]
        print(text)
        return text
    print('error')
    return text


def change(text: str, sub_str: str, replacement: str):
    text = text.replace(sub_str, replacement)
    print(text)
    return text


message = input()
command = input()
while not command == 'Reveal':
    command = command.split(':|:')
    if command[0] == 'InsertSpace':
        message = insert_space(message, int(command[1]))
    elif command[0] == 'Reverse':
        message = reverse(message, command[1])
    elif command[0] == 'ChangeAll':
        message = change(message, command[1], command[2])
    command = input()
print(f'You have a new text message: {message}')

