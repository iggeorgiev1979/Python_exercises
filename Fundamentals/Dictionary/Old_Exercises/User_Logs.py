def register(ip: str, user: str, log: dict):
    if user not in log.keys():
        log[user] = {}
    if ip not in log[user].keys():
        log[user][ip] = 1
    else:
        log[user][ip] += 1


logbook = {}
command = input()
while not command == 'end':
    command = [[x for x in y.split('=')] for y in command.split()]
    register(command[0][1], command[2][1], logbook)
    command = input()
logbook = dict(sorted(logbook.items(), key=lambda x: x[0]))
for i in logbook.keys():
    print(f'{i}:')
    result = [f'{x} => {j}' for x, j in logbook[i].items()]
    print(', '.join(result) + '.')
