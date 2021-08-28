def register(cars, new_car):
    if new_car[0] not in cars.keys():
        cars[new_car[0]] = new_car[1]
        print(f'{new_car[0]} registered {new_car[1]} successfully')
    else:
        print(f'ERROR: already registered with plate number {new_car[1]}')


def unregister(cars, new_car):
    if new_car in cars.keys():
        cars.pop(new_car)
        print(f'{new_car} unregistered successfully')
    else:
        print(f'ERROR: user {new_car} not found')


n = int(input())
parking = {}
for i in range(n):
    command = input().split()
    if command[0] == 'register':
        command = [command[1], command[2]]
        register(parking, command)
    else:
        command = command[1]
        unregister(parking, command)
print(*[f'{i} => {j}' for (i, j) in parking.items()], sep='\n')

