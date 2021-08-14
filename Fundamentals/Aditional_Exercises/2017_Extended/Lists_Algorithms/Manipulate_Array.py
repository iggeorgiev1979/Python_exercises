my_list = input().split()
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'Distinct':
        tmp_list = []
        for i in my_list:
            if i not in tmp_list:
                tmp_list.append(i)
        my_list = tmp_list
    elif command[0] == 'Reverse':
        my_list.reverse()
    else:
        my_list[int(command[1])] = command[2]
print(', '.join(my_list))
