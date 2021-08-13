def shoot(my_list, index, power):
    my_list[index] -= power
    if my_list[index] <= 0:
        my_list.pop(index)


def add(my_list, index, value):
    my_list.insert(index, value) if 0 <= index < len(my_list) else print('Invalid placement!')


def strike(my_list, index, radius):
    del my_list[index - radius:index + radius + 1]


list_of_numbers = list(map(lambda x: int(x), input().split()))
command = input().split()

while not command[0] == 'End':
    if command[0] == 'Shoot':
        if 0 <= int(command[1]) < len(list_of_numbers):
            shoot(list_of_numbers, int(command[1]), int(command[2]))
    elif command[0] == 'Add':
        add(list_of_numbers, int(command[1]), int(command[2]))
    elif command[0] == 'Strike':
        if int(command[1]) - int(command[2]) >= 0 and int(command[1]) + int(command[2]) < len(list_of_numbers):
            strike(list_of_numbers, int(command[1]), int(command[2]))
        else:
            print('Strike missed!')
    command = input().split()
print(*list_of_numbers, sep='|')
