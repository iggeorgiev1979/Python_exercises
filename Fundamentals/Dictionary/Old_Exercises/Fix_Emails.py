log = {}
while True:
    name = input()
    if name == 'stop':
        break
    mail = input()
    x = mail[-2:].lower()
    if not x == 'us' and not x == 'uk':
        log[name] = mail
[print(f'{i} -> {j}') for i, j in log.items()]
