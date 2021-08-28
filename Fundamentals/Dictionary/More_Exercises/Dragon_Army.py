def register(colour: str, name: str, damage: int, health: int, armor: int, dragons: dict):
    if colour not in dragons.keys():
        dragons[colour] = {}
    dragons[colour][name] = [damage, health, armor]


def check(stats: list):
    default = [0, 0, 45, 250, 10]
    for i in range(5):
        if stats[i] == 'null':
            stats[i] = default[i]
    return stats


n = int(input())
dragons_dict = {}
total_dict = {}
for _ in range(n):
    command = check(input().split())
    register(command[0], command[1], int(command[2]), int(command[3]), int(command[4]), dragons_dict)

for i in dragons_dict.keys():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for j in dragons_dict[i].keys():
        total_damage += dragons_dict[i][j][0]
        total_health += dragons_dict[i][j][1]
        total_armor += dragons_dict[i][j][2]
    print(f'{i}::({total_damage / len(dragons_dict[i]):.2f}/{total_health / len(dragons_dict[i]):.2f}/{total_armor / len(dragons_dict[i]):.2f})')
    [print(f'-{el1} -> damage: {el2[0]}, health: {el2[1]}, armor: {el2[2]}') for el1, el2 in sorted(dragons_dict[i].items(), key=lambda x: x[0])]
