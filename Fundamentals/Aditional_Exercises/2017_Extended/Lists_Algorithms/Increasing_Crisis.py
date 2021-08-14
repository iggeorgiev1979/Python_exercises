n = int(input())
result = []
for _ in range(n):
    tmp_list = [int(x) for x in input().split()]
    if len(result) == 0:
        result = tmp_list
    else:
        for i in range(len(result) - 1, -1, -1):
            if result[i] <= tmp_list[0]:
                index = i
                for j in tmp_list:
                    if j >= result[index]:
                        result.insert(index + 1, j)
                        index += 1
                    else:
                        del result[index + 1:]
                        break
                break
print(*result, sep=' ')
