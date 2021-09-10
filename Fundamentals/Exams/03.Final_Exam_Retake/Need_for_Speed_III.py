def register(log: dict, car: list):
    car_model = car[0]
    car_mileage = int(car[1])
    car_fuel = int(car[2])
    log[car_model] = [car_mileage, car_fuel]


def drive(log: dict, car):
    model = car[1]
    distance = int(car[2])
    fuel = int(car[3])
    if fuel > log[model][1]:
        print("Not enough fuel to make that ride")
    else:
        log[model][0] += distance
        log[model][1] -= fuel
        print(f'{model} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if log[model][0] >= 100000:
            log.pop(model)
            print(f"Time to sell the {model}!")


def refuel(log: dict, car: list):
    model = car[1]
    fuel = int(car[2])
    if log[model][1] + fuel > 75:
        fuel = 75 - log[model][1]
    log[model][1] += fuel
    print(f'{model} refueled with {fuel} liters')


def revert(log: dict, car: list):
    model = car[1]
    distance = int(car[2])
    log[model][0] -= distance
    if log[model][0] >= 10000:
        print(f'{model} mileage decreased by {distance} kilometers')
    else:
        log[model][0] = 10000


garage = {}
for _ in range(int(input())):
    new_car = input().split('|')
    register(garage, new_car)
command = input()
while not command == 'Stop':
    command = command.split(' : ')
    if command[0] == 'Drive':
        drive(garage, command)
    elif command[0] == 'Refuel':
        refuel(garage, command)
    elif command[0] == 'Revert':
        revert(garage, command)
    command = input()
[print(f"{i} -> Mileage: {j[0]} kms, Fuel in the tank: {j[1]} lt.") for i, j in sorted(garage.items(), key=lambda x: (-x[1][0], x[0]))]
