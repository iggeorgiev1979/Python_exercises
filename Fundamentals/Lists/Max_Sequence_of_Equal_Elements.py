list_of_numbers = input().split(' ')
list_1 = [list_of_numbers[0]]
result_list = []
for i in range(1, len(list_of_numbers)):
    if list_of_numbers[i] == list_of_numbers[i - 1]:
        list_1.append(list_of_numbers[i])
    else:
        if len(list_1) > len(result_list):
            result_list = list_1
        list_1 = [list_of_numbers[i]]
    if len(list_1) > len(result_list):
        result_list = list_1
print(*result_list)