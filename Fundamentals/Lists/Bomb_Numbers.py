list_of_numbers = [int(x) for x in input().split()]
command = input().split()
power = int(command[1])

while int(command[0]) in list_of_numbers:
    bomb = list_of_numbers.index(int(command[0]))
    if bomb - power >= 0:
        tmp_list = list_of_numbers[:bomb - power] + list_of_numbers[bomb + power + 1:]
    else:
        tmp_list = list_of_numbers[bomb + power + 1:]
    list_of_numbers = tmp_list
print(sum(list_of_numbers))