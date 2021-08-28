def validate(input_str: str):
    town = []
    artist = []
    tickets = None
    ticket_price = None
    sample = input_str.split()
    try:
        tickets = int(sample[-1])
        sample.pop(-1)
    except:
        return False
    try:
        ticket_price = int(sample[-1])
        sample.pop(-1)
    except:
        return False
    boolean = False
    for i in sample:
        if i[0] == '@':
            boolean = True
        if boolean:
            town.append(i)
        else:
            artist.append(i)
    if len(town) == 0:
        return False
    else:
        town = ' '.join(town)
        town = town[1:]
        artist = ' '.join(artist)
    return [artist, town, tickets * ticket_price]


def register(artist: str, town: str, money: int, log: dict):
    if town not in log.keys():
        log[town] = {}
    if artist not in log[town].keys():
        log[town][artist] = 0
    log[town][artist] += money


log_dict = {}
command = input()
while not command == 'End':
    command = validate(command)
    if not command:
        pass
    else:
        register(command[0], command[1], command[2], log_dict)
    command = input()
for i in log_dict.keys():
    print(i)
    [print(f'#  {x} -> {y}') for x, y in sorted(log_dict[i].items(), key=lambda el: -el[1])]
