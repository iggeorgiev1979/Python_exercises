pirate = list(map(lambda x: int(x), input().split('>')))
war_ship = list(map(lambda x: int(x), input().split('>')))
max_health = int(input())
command = input().split()
winner = False
while not command[0] == 'Retire':
    if command[0] == 'Fire':
        if 0 <= int(command[1]) < len(pirate):
            war_ship[int(command[1])] -= int(command[2])
            if war_ship[int(command[1])] <= 0:
                print('You won! The enemy ship has sunken.')
                winner = True
                break
    elif command[0] == 'Defend':
        start = int(command[1])
        end = int(command[2])
        damage = int(command[3])
        if start >= 0 and end < len(pirate):
            for i in range(start, end + 1):
                pirate[i] -= damage
                if pirate[i] < 0:
                    pirate[i] = 0
            if 0 in pirate:
                print('You lost! The pirate ship has sunken.')
                winner = True
                break
    elif command[0] == 'Repair':
        if 0 <= int(command[1]) < len(pirate):
            if pirate[int(command[1])] + int(command[2]) > max_health:
                pirate[int(command[1])] = max_health
            else:
                pirate[int(command[1])] += int(command[2])
    elif command[0] == 'Status':
        repair_list = list(filter(lambda x: x < max_health * 0.2, pirate))
        print(f'{len(repair_list)} sections need repair.')
    command = input().split()
if not winner:
    print(f'Pirate ship status: {sum(pirate)}\nWarship status: {sum(war_ship)}')
