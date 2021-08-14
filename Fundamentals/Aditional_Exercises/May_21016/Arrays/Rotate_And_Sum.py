numbers = list(map(lambda x: int(x), input().split()))
rotated_numbers = []
result = []
n = int(input())
for _ in range(n):
    xi = numbers.pop(-1)
    numbers.insert(0, xi)
    rotated_numbers.append(tuple(numbers))
for i in range(len(numbers)):
    sum_elements = 0
    for j in range(len(rotated_numbers)):
        sum_elements += rotated_numbers[j][i]
    result.append(sum_elements)

print(*result, sep=' ')

