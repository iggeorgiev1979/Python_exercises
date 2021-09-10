energy = int(input())
wins = 0
command = input()
defeat = False
while not command == 'End of battle':
    points = int(command)
    if energy - points >= 0:
        energy -= points
        wins += 1
        if wins % 3 == 0:
            energy += wins
    elif energy - points < 0:
        print(f'Not enough energy! Game ends with {wins} won battles and {energy} energy')
        defeat = True
        break
    command = input()
if not defeat:
    print(f'Won battles: {wins}. Energy left: {energy}')
