def register(name: str, number: str, log: dict):
    log[name] = number


phonebook = {}
command = input().split()
while not command[0] == 'END':
    if command[0] == 'A':
        register(command[1], command[2], phonebook)
    else:
        if command[1] in phonebook.keys():
            print(f'{command[1]} -> {phonebook[command[1]]}')
        else:
            print(f'Contact {command[1]} does not exist.')
    command = input().split()
