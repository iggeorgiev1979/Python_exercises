numbers = [int(x) for x in input().split()]
n = int(input())
result = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if abs(numbers[i] - numbers[j]) == n:
            result += 1
print(result)
