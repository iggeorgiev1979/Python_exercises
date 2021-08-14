list_of_numbers = [int(x) for x in input().split()]
len_sequence = 0
result_list = []
for i in range(len(list_of_numbers)):
    tmp_list = [list_of_numbers[i]]
    for j in range(i + 1, len(list_of_numbers)):
        if list_of_numbers[j] > tmp_list[-1]:
            tmp_list.append(list_of_numbers[j])
        else:
            break
    if len(tmp_list) > len_sequence:
        len_sequence = len(tmp_list)
        result_list = tmp_list
print(*result_list, sep=' ')
