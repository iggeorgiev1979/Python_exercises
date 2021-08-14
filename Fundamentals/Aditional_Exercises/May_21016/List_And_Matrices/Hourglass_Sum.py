matrix = []
for _ in range(6):
    matrix.append(list(map(lambda x: int(x), input().split())))
result = 0
for i in range(4):
    for j in range(4):
        hourglass_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j + 1] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if hourglass_sum > result:
            result = hourglass_sum

print(result)
