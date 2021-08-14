number = input().split()
row = int(number[0])
column = int(number[1])
matrix = []
for _ in range(row):
    matrix.append(list(map(lambda x: int(x), input().split())))
result = 0
result_cell = ()
for i in range(row - 2):
    for j in range(column - 2):
        cell = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]
        sum_cell = sum(cell[0]) + sum(cell[1]) + sum(cell[2])
        if sum_cell > result:
            result = sum_cell
            result_cell = cell

print(f'Sum = {result}')
print(*result_cell[0], sep=' ')
print(*result_cell[1], sep=' ')
print(*result_cell[2], sep=' ')
