numbers = input().split()
for i in range(len(numbers)):
    for j in range(len(numbers) - 1, i, -1):
        if numbers[i] == numbers[j]:
            numbers.pop(j)
print(*numbers, sep=' ')
