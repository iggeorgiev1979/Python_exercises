shopping_list = input().split('!')
command = input().split()
while not command[0] == 'Go':
    item = command[1]
    if command[0] == 'Urgent':
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif command[0] == 'Unnecessary':
        if item in shopping_list:
            shopping_list.remove(item)
    elif command[0] == 'Correct':
        if item in shopping_list:
            shopping_list[shopping_list.index(item)] = command[2]
    elif command[0] == 'Rearrange':
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
    command = input().split()

print(*shopping_list, sep=', ')
