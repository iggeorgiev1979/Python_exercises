def register_towns(log: dict, town_info: str):
    town = town_info.split('||')
    if town[0] not in log:
        log[town[0]] = [0, 0]
    log[town[0]][0] += int(town[1])
    log[town[0]][1] += int(town[2])


def ride(log: dict, goals: list):
    log[goals[1]][0] -= int(goals[2])
    log[goals[1]][1] -= int(goals[3])
    print(f"{goals[1]} plundered! {goals[3]} gold stolen, {goals[2]} citizens killed.")
    if log[goals[1]][0] <= 0 or log[goals[1]][1] <= 0:
        print(f"{goals[1]} has been wiped off the map!")
        log.pop(goals[1])


def prosper(log : dict, goals: list):
    if int(goals[2]) < 0:
        print('Gold added cannot be a negative number!')
    else:
        log[goals[1]][1] += int(goals[2])
        print(f"{goals[2]} gold added to the city treasury. {goals[1]} now has {log[goals[1]][1]} gold.")


towns = {}
command = input()
while not command == 'Sail':
    register_towns(towns, command)
    command = input()
event = input()
while not event == 'End':
    event = event.split('=>')
    if event[0] == 'Plunder':
        ride(towns, event)
    elif event[0] == 'Prosper':
        prosper(towns, event)
    event = input()
if not len(towns) == 0:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    [print(f"{i} -> Population: {j[0]} citizens, Gold: {j[1]} kg") for i, j in sorted(towns.items(), key=lambda x: (-x[1][1], x[0]))]
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
