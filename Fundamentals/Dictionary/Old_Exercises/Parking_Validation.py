def validate(number: str):
    if not len(number) == 8:
        return False
    if not 65 <= ord(number[0]) <= 90 or not 65 <= ord(number[1]) <= 90 or not 65 <= ord(
            number[6]) <= 90 or not 65 <= ord(number[7]) <= 90:
        return False
    if not number[2:6].isnumeric():
        return False
    return True


def register(log: dict, car: list):
    if car[1] not in log.keys():
        if car[2] not in log.values():
            log[car[1]] = car[2]
            print(f'{car[1]} registered {car[2]} successfully')
        else:
            print(f'ERROR: license plate {car[2]} is busy')
    else:
        print(f'ERROR: already registered with plate number {log[car[1]]}')


def unregister(log: dict, car: list):
    if car[1] not in log.keys():
        print(f'ERROR: user {car[1]} not found')
    else:
        print(f'user {car[1]} unregistered successfully')
        log.pop(car[1])


parking = {}
n = int(input())
for _ in range(n):
    command = input().split()

    if command[0] == 'register':
        if not validate(command[2]):
            if command[1] in parking:
                print(f'ERROR: already registered with plate number {parking[command[1]]}')
            else:
                print(f'ERROR: invalid license plate {command[2]}')
        else:
            register(parking, command)
    elif command[0] == 'unregister':
        unregister(parking, command)
[print(f'{i} => {j}') for i, j in parking.items()]
