n = int(input())
ships_list = []
destroyed_ships = 0
for _ in range(n):
    ships_list.append(list(map(lambda x: int(x), input().split())))
attacks_list = input().split()
for i in attacks_list:
    attack = i.split('-')
    row = int(attack[0])
    place = int(attack[1])
    if ships_list[row][place] > 0:
        ships_list[row][place] -= 1
        if ships_list[row][place] == 0:
            destroyed_ships += 1
print(destroyed_ships)