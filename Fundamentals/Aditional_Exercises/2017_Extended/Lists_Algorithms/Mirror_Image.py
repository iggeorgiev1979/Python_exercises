def reverse_list(my_list, index):
    a = [my_list[x] for x in range(index - 1, -1, -1)]
    b = [my_list[x] for x in range(len(my_list) - 1, index, -1)]
    return f'{" ".join(a)} {my_list[index]} {" ".join(b)}'


list_to_reverse = input().split()
command = input()
while not command == 'Print':
    list_to_reverse = reverse_list(list_to_reverse, int(command)).split()
    command = input()
print(*list_to_reverse, sep=' ')
