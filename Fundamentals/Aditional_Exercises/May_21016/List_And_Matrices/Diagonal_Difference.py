number = int(input())
matrix = []
for _ in range(number):
    row = list(map(lambda x: int(x), input().split()))
    matrix.append(row)
diagonal_1 = []
diagonal_2 = []
for i in range(number):
    diagonal_1.append(matrix[i][i])
    diagonal_2.append(matrix[i][number - 1 - i])
print(abs(sum(diagonal_1) - sum(diagonal_2)))

