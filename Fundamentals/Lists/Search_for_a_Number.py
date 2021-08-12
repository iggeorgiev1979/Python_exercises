list_of_numbers = input().split(' ')
list_of_commands = input().split(' ')
list_of_numbers = list_of_numbers[:int(list_of_commands[0])]
list_of_numbers = list_of_numbers[int(list_of_commands[1]):]
if list_of_commands[2] in list_of_numbers:
    print('YES!')
else:
    print('NO!')
