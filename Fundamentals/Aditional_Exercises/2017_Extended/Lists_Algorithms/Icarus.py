def left_right(direction, steps, index, power, my_list):
    if direction == 'left':
        for _ in range(steps):
            if index == 0:
                index = len(my_list) - 1
                power += 1
            else:
                index -= 1
            if not my_list[index] - power < 0:
                my_list[index] -= power
            else:
                my_list[index] = 0
    else:
        for _ in range(steps):
            if index == len(my_list) - 1:
                index = 0
                power += 1
            else:
                index += 1
            if not my_list[index] - power < 0:
                my_list[index] -= power
            else:
                my_list[index] = 0
    return [index, power]


list_of_numbers = [int(x) for x in input().split()]
starting_power = [int(input()), 1]
command = input().split()
while not command[0] == 'Supernova':
    starting_power = left_right(command[0], int(command[1]), starting_power[0], starting_power[1], list_of_numbers)
    command = input().split()
print(*list_of_numbers, sep=' ')
