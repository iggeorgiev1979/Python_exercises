note = input().split('-')
to_do_list = ['0'] * 10
while not note[0] == 'End':
    to_do_list.insert(int(note[0]) - 1, note[1])
    to_do_list.pop(int(note[0]))
    note = input().split('-')
print_list = [x for x in to_do_list if not x == '0']
print(print_list)
