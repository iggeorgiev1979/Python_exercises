from collections import deque

water_quantity = int(input())
people = deque()
name = input()
while not name == 'Start':
    people.append(name)
    name = input()

command = input()
while not command == 'End':
    if command.split()[0] == 'refill':
        water_quantity += int(command.split()[1])
    else:
        if water_quantity >= int(command):
            water_quantity -= int(command)
            print(f'{people.popleft()} got water')
        else:
            print(f'{people.popleft()} must wait')

    command = input()
print(f'{water_quantity} liters left')

