matrix_size = list(map(lambda x: int(x), input().split()))
matrix = []
for _ in range(matrix_size[0]):
    matrix.append(input().split())
result = 0
for i in range(0, matrix_size[0] - 1):
    for j in range(0, matrix_size[1] - 1):
        if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i + 1][j] and matrix[i][j] == matrix[i + 1][j + 1]:
            result += 1
print(result)
