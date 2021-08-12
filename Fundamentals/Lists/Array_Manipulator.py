def add_number(my_list, index, element):
    my_list.insert(index, element)


def add_many(my_list, index, new_numbers):
    new_numbers.reverse()
    for i in new_numbers:
        my_list.insert(index, i)


def contains(my_list, element):
    print(my_list.index(element)) if element in my_list else print('-1')


def remove(my_list, index):
    try:
        my_list.pop(index)
    except:
        pass


def shift(my_list, position):
    if position > len(my_list):
        position = position % len(my_list)
    tmp_list = my_list[position:] + my_list[:position]
    return tmp_list


def sum_pairs(my_list):
    tmp_list = []
    for i in range(0, len(my_list), 2):
        try:
            tmp_list.append(my_list[i] + my_list[i + 1])
        except:
            tmp_list.append(my_list[i])
    return tmp_list


list_of_numbers = [int(x) for x in input().split()]
command = input().split()

while not command[0] == 'print':
    if command[0] == 'add':
        add_number(list_of_numbers, int(command[1]), int(command[2]))
    elif command[0] == 'addMany':
        numbers_to_insert = [int(x) for x in command[2:]]
        add_many(list_of_numbers, int(command[1]), numbers_to_insert)
    elif command[0] == 'contains':
        contains(list_of_numbers, int(command[1]))
    elif command[0] == 'remove':
        remove(list_of_numbers, int(command[1]))
    elif command[0] == 'shift':
        list_of_numbers = shift(list_of_numbers, int(command[1]))
    elif command[0] == 'sumPairs':
        list_of_numbers = sum_pairs(list_of_numbers)

    command = input().split()

print(list_of_numbers)
