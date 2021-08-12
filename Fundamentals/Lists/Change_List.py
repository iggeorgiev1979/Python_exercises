list_of_numbers = input().split(' ')
command = input().split(' ')
while True:
    if command[0] == 'Odd' or command[0] == 'Even':
        break
    elif command[0] == 'Delete':
        list_of_numbers = [i for i in list_of_numbers if i not in command]
    else:
        list_of_numbers.insert(int(command[2]), command[1])

    command = input().split(' ')
if command[0] == 'Even':
    list_of_numbers = [i for i in list_of_numbers if int(i) % 2 == 0]
else:
    list_of_numbers = [i for i in list_of_numbers if not int(i) % 2 == 0]
print(*list_of_numbers)
