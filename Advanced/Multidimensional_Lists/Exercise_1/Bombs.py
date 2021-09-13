def explode(matrix, bomb, n):
    power = matrix[bomb[0]][bomb[1]]
    matrix[bomb[0]][bomb[1]] = 0
    if not bomb[0] == 0:
        if matrix[bomb[0] - 1][bomb[1]] > 0:
            matrix[bomb[0] - 1][bomb[1]] -= power  # up
    if not bomb[0] == 0 and not bomb[1] > n - 2:
        if matrix[bomb[0] - 1][bomb[1] + 1] > 0:
            matrix[bomb[0] - 1][bomb[1] + 1] -= power  # up_right
    if not bomb[0] == 0 and not bomb[1] == 0:
        if matrix[bomb[0] - 1][bomb[1] - 1] > 0:
            matrix[bomb[0] - 1][bomb[1] - 1] -= power  # up_left
    if not bomb[1] == 0:
        if matrix[bomb[0]][bomb[1] - 1] > 0:
            matrix[bomb[0]][bomb[1] - 1] -= power  # left
    if not bomb[1] > n - 2:
        if matrix[bomb[0]][bomb[1] + 1] > 0:
            matrix[bomb[0]][bomb[1] + 1] -= power  # right
    if not bomb[0] > n - 2:
        if matrix[bomb[0] + 1][bomb[1]] > 0:
            matrix[bomb[0] + 1][bomb[1]] -= power  # down
    if not bomb[0] > n - 2 and not bomb[1] > n - 2:
        if matrix[bomb[0] + 1][bomb[1] + 1] > 0:
            matrix[bomb[0] + 1][bomb[1] + 1] -= power  # down_right
    if not bomb[0] > n - 2 and not bomb[1] == 0:
        if matrix[bomb[0] + 1][bomb[1] - 1] > 0:
            matrix[bomb[0] + 1][bomb[1] - 1] -= power  # down_left


def sum_matrix(matrix, n):
    active_cells = 0
    result = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                active_cells += 1
                result += matrix[i][j]
    return [active_cells, result]


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = [[int(x) for x in y.split(',')] for y in input().split()]
for el in bombs:
    if matrix[el[0]][el[1]] > 0:
        explode(matrix, [el[0], el[1]], n)
result_list = sum_matrix(matrix, n)
matrix = [[str(x) for x in y] for y in matrix]
matrix = [" ".join(x) for x in matrix]
print(f'Alive cells: {result_list[0]}\nSum: {result_list[1]}')
print(*matrix, sep='\n')
