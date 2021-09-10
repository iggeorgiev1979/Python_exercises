health = 100
coins = 0
rooms = input().split('|')
counter = 0
for i in range(len(rooms)):
    command = rooms[i].split()
    if command[0] == 'potion':
        if health + int(command[1]) > 100:
            amount = 100 - health
            health = 100
        else:
            amount = int(command[1])
            health += amount
        print(f'You healed for {amount} hp.')
        print(f'Current health: {health} hp.')
    elif command[0] == 'chest':
        coins += int(command[1])
        print(f'You found {command[1]} bitcoins.')
    else:
        health -= int(command[1])
        if health <= 0:
            print(f'You died! Killed by {command[0]}.\nBest room: {i + 1}')
            break
        else:
            print(f'You slayed {command[0]}.')
    counter += 1
if counter == len(rooms):
    print(f"You've made it!\nBitcoins: {coins}\nHealth: {health}")
