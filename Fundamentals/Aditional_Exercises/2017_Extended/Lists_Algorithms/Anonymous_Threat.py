def merge(my_list, start, end):
    if start < 0:
        start = 0
    if end > len(my_list) - 1:
        end = len(my_list) - 1
    a = ''.join(my_list[start:end + 1])
    del my_list[start:end + 1]
    my_list.insert(start, a)
    return ' '.join(my_list)


def divide(my_list, index, parts):
    element = list(my_list.pop(index))
    tmp = []
    n = len(element) // parts
    for i in range(parts):
        if not i == parts - 1:
            a = ''
            for j in range(n):
                a += element.pop(0)
            tmp.append(a)
        else:
            tmp.append(''.join(element))
    for i in range(len(tmp) - 1, -1, -1):
        my_list.insert(index, tmp[i])
    return f"{' '.join(my_list)}"


my_string = input()
command = input().split()
while not command[0] == '3:1':
    if command[0] == 'merge':
        my_string = merge(my_string.split(), int(command[1]), int(command[2]))
    else:
        my_string = divide(my_string.split(), int(command[1]), int(command[2]))
    command = input().split()
print(my_string)
