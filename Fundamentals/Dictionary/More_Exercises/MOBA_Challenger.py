def register(players: dict, total_skill: dict, info: list):
    if info[0] not in players.keys():
        players[info[0]] = {}
    if info[1] not in players[info[0]].keys():
        players[info[0]][info[1]] = 0
    if int(info[2]) > players[info[0]][info[1]]:
        old_points = players[info[0]][info[1]]
        players[info[0]][info[1]] = int(info[2])
        if info[0] not in total_skill.keys():
            total_skill[info[0]] = 0
        else:
            total_skill[info[0]] -= old_points
        total_skill[info[0]] += int(info[2])


def fight(players: dict, total_skill: dict, info: list):
    if info[0] in total_skill.keys() and info[1] in total_skill.keys():
        exists = False
        for position in players[info[0]].keys():
            if position in players[info[1]].keys():
                exists = True
                break
        if exists:
            if total_skill[info[0]] > total_skill[info[1]]:
                players.pop(info[1])
                total_skill.pop(info[1])
            elif total_skill[info[0]] < total_skill[info[1]]:
                players.pop(info[0])
                total_skill.pop(info[0])


players = {}
total_skill = {}
command = input()
while not command == 'Season end':
    if '->' in command:
        command = command.split(' -> ')
        register(players, total_skill, command)
    else:
        command = command.split(' vs ')
        fight(players, total_skill, command)
    command = input()
total_skill = dict(sorted(total_skill.items(), key=lambda x: (-x[1], x[0])))
for name in total_skill.keys():
    print(f'{name}: {total_skill[name]} skill')
    players[name] = dict(sorted(players[name].items(), key=lambda x: (-x[1], x[0])))
    print(*[f'- {i} <::> {j}' for i, j in players[name].items()], sep='\n')
