list_one = [int(x) for x in input().split()]
list_two = [int(x) for x in input().split()]
result = []
for i in range(len(list_one)):
    for j in range(len(list_two) - 1, -1, -1):
        if len(list_one) > 0 and len(list_two) > 0:
            result.append(list_one.pop(i))
            result.append(list_two.pop(j))
        else:
            break
    if len(list_one) == 0 or len(list_two) == 0:
        break
if len(list_one) > 0:
    list_one.sort()
else:
    list_one = sorted(list_two)
result = list(filter(lambda x: list_one[0] < x < list_one[1], result))
print(*sorted(result), sep=' ')
