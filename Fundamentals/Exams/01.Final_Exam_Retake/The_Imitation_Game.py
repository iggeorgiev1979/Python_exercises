def move(text: str, number: int):
    text = text[number:] + text[:number]
    return text


def insert(text: str, info: list):
    index = int(info[1])
    value = info[2]
    text = text[:index] + value + text[index:]
    return text


def change(text: str, info: list):
    sub_str = info[1]
    replacement = info[2]
    text = text.replace(sub_str, replacement)
    return text


message = input()
command = input()
while not command == 'Decode':
    command = command.split('|')
    if command[0] == 'Move':
        message = move(message, int(command[1]))
    elif command[0] == 'Insert':
        message = insert(message, command)
    elif command[0] == 'ChangeAll':
        message = change(message, command)
    command = input()
print(f'The decrypted message is: {message}')
