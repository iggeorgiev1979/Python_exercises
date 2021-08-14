list_of_numbers = input().split()
result = ''
result_counter = 0
for i in range(len(list_of_numbers)):
    counter = 0
    for j in range(i + 1, len(list_of_numbers)):
        if list_of_numbers[j] == list_of_numbers[i]:
            counter += 1
    if counter > result_counter:
        result_counter = counter
        result = list_of_numbers[i]
print(result)
