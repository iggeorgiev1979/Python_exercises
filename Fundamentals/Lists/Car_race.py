list_of_numbers = [int(x) for x in input().split(' ')]
car_1 = 0
car_2 = 0
for i in range(len(list_of_numbers) // 2):
    if list_of_numbers[i] == 0:
        car_1 *= 0.8
    else:
        car_1 += list_of_numbers[i]
for i in range(-1, -len(list_of_numbers) // 2, -1):
    if list_of_numbers[i] == 0:
        car_2 *= 0.8
    else:
        car_2 += list_of_numbers[i]
if car_1 < car_2:
    print(f'The winner is left with total time: {car_1:.1f}')
else:
    print(f'The winner is right with total time: {car_2:.1f}')
