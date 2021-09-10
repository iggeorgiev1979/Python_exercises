items_list = input().split(', ')
command = input().split(' - ')
while not command[0] == 'Craft!':
    item = command[1]
    if command[0] == 'Collect':
        if item not in items_list:
            items_list.append(item)
    elif command[0] == 'Drop':
        if item in items_list:
            items_list.remove(item)
    elif command[0] == 'Combine Items':
        tmp_list = item.split(':')
        if tmp_list[0] in items_list:
            items_list.insert(items_list.index(tmp_list[0]) + 1, tmp_list[1])
    elif command[0] == 'Renew':
        if item in items_list:
            items_list.remove(item)
            items_list.append(item)
    command = input().split(' - ')
print(', '.join(items_list))
