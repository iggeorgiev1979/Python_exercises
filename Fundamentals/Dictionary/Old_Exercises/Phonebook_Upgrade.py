def register(name: str, number: str, log: dict):
    log[name] = number


phonebook = {}
command = input().split()
while not command[0] == 'END':
    if command[0] == 'A':
        register(command[1], command[2], phonebook)
    elif command[0] == 'S':
        if command[1] in phonebook.keys():
            print(f'{command[1]} -> {phonebook[command[1]]}')
        else:
            print(f'Contact {command[1]} does not exist.')
    else:
        [print(f'{i} -> {j}') for i, j in sorted(phonebook.items(), key=lambda x: x[0])]
    command = input().split()
