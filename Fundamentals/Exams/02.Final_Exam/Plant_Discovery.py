def register(log: dict, info: list):
    name = info[0]
    if info[1].isnumeric():
        rarity = int(info[1])
    else:
        print('error')
        return
    if name not in log.keys():
        log[name] = [0]
    log[name][0] = rarity


def rate(log: dict, plant_info: list):
    name = plant_info[0]
    if name not in log.keys():
        print('error')
        return
    if plant_info[1].isnumeric():
        rating = float(plant_info[1])
    else:
        print('error')
        return
    log[name].append(rating)


def update(log: dict, plant_info: list):
    name = plant_info[0]
    if name not in log.keys():
        print('error')
        return
    if plant_info[1].isnumeric():
        rarity = int(plant_info[1])
    else:
        print('error')
        return
    log[name][0] = rarity


def reset(log: dict, name: str):
    # log[name] = [log[name][0]]
    if name not in log.keys():
        print('error')
        return
    if len(log[name]) > 1:
        del log[name][1:]


plants = {}
for _ in range(int(input())):
    plant = input().split('<->')
    register(plants, plant)
command = input()
while not command == 'Exhibition':
    command = command.split(': ')
    if command[0] == 'Rate':
        command = command[1].split(' - ')
        if len(command) == 2:
            rate(plants, command)
        else:
            print('error')
    elif command[0] == 'Update':
        command = command[1].split(' - ')
        if len(command) == 2:
            update(plants, command)
        else:
            print('error')
    elif command[0] == 'Reset':
        if len(command) == 2:
            reset(plants, command[1])
        else:
            print('error')
    else:
        print('error')
    command = input()

for i, j in plants.items():
    if len(j) == 1:
        j.append(0)
    else:
        rating = sum(j[1:]) / (len(j) - 1)
        del j[1:]
        j.append(rating)

print('Plants for the exhibition:')
for i, j in sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])):
    print(f'- {i}; Rarity: {j[0]}; Rating: {j[1]:.2f}')
