def max_value(number_str):
    number = int(number_str)
    number_list = list(number_str)
    for i in range(len(number_list) - 1):
        number_list.append(number_list.pop(0))
        if int(''.join(number_list)) > number:
            number = int(''.join(number_list))
    return str(number)


def min_value(number_str):
    number = int(number_str)
    number_list = list(number_str)
    for i in range(len(number_list) - 1):
        number_list.append(number_list.pop(0))
        if int(''.join(number_list)) < number:
            number = int(''.join(number_list))
    return str(number)


list_of_numbers = input().split()
command = input()
if command == 'Max':
    result = [int(max_value(i)) for i in list_of_numbers]
    print(*result, sep=', ')
    print(sum(result))
else:
    result = [int(min_value(i)) for i in list_of_numbers]
    print(*result, sep=', ')
    print(sum(result))
