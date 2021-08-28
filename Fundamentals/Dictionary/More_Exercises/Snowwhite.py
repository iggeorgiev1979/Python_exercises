def register(name: str, hat_colour: str, points: int, dwarfs: dict, hats: dict):
    el = f'({hat_colour}) {name}'
    if el not in dwarfs.keys():
        dwarfs[el] = [hat_colour, 0]
        if hat_colour not in hats.keys():
            hats[hat_colour] = 0
        hats[hat_colour] += 1
    if points > dwarfs[el][1]:
        dwarfs[el][1] = points


dwarfs_dict, hats_dict = {}, {}
command = input()
while not command == 'Once upon a time':
    command = command.split(' <:> ')
    register(command[0], command[1], int(command[2]), dwarfs_dict, hats_dict)
    command = input()
result = {i: j for i, j in sorted(dwarfs_dict.items(), key=lambda x: (-x[1][1], -hats_dict[x[1][0]]))}
[print(f'{i} <-> {j[1]}') for i, j in result.items()]
