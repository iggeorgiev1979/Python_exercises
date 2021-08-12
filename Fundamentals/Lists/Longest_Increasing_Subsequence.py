list_of_numbers = [int(x) for x in input().split()]
results = [[]] * len(list_of_numbers)
results[0] = [list_of_numbers[0]]
for i in range(1, len(list_of_numbers)):
    for j in range(0, i):
        if list_of_numbers[i] > results[j][-1]:
            tmp_list = [x for x in results[j]]
            tmp_list.append(list_of_numbers[i])
            if len(tmp_list) > len(results[i]):
                results[i] = [x for x in tmp_list]
    if len(results[i]) == 0:
        results[i] = [list_of_numbers[i]]
counter = 0
index = None
for i in range(len(results)):
    if len(results[i]) > counter:
        counter = len(results[i])
        index = i
print(*results[index])
# 7 8 7 16 9 10
# 7 3 5 8 -1 0 6 7
# 11 12 13 3 14 4 15 5 6 7 8 7 16 9 8
# 11 8 12 15 9 10 6 16 10
