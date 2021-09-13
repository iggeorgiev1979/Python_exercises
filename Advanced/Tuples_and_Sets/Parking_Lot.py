n = int(input())
parking = set()
for _ in range(n):
    command, car_number = input().split(', ')
    if command == 'IN':
        parking.add(car_number)
    elif command == 'OUT':
        parking.remove(car_number)

print('Parking Lot is Empty') if len(parking) == 0 else print(*parking, sep='\n')
