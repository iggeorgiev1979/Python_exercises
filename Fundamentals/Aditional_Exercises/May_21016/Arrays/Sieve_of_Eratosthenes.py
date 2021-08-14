number = int(input())
numbers_list = [int(x) for x in range(2, number + 1)]
for i in range(len(numbers_list)):
    for j in range(len(numbers_list) - 1, i - 1, -1):
        if not numbers_list[j] == numbers_list[i] and numbers_list[j] % numbers_list[i] == 0:
            numbers_list.pop(j)
print(*numbers_list, sep=' ')
