import sys
from io import StringIO

input_1 = """4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)
"""

input_2 = """5
3
(1, 1)
(2, 4)
(4, 1)"""

sys.stdin = StringIO(input_2)


def insert_bomb(matrix: list, mine: str):
    row, col = mine.split(", ")
    row = int(row)
    col = int(col)
    matrix[row][col] = "*"
    if not row == 0:
        if not matrix[row - 1][col] == "*":
            matrix[row - 1][col] += 1
    if not row == len(matrix) - 1:
        if not matrix[row + 1][col] == "*":
            matrix[row + 1][col] += 1
    if not col == 0:
        if not matrix[row][col - 1] == "*":
            matrix[row][col - 1] += 1
    if not col == len(matrix) - 1:
        if not matrix[row][col + 1] == "*":
            matrix[row][col + 1] += 1
    if not row == 0 and not col == 0:
        if not matrix[row - 1][col - 1] == "*":
            matrix[row - 1][col - 1] += 1

    if not row == len(matrix) - 1 and not col == len(matrix) - 1:
        if not matrix[row + 1][col + 1] == "*":
            matrix[row + 1][col + 1] += 1
    if not row == 0 and not col == len(matrix) - 1:
        if not matrix[row - 1][col + 1] == "*":
            matrix[row - 1][col + 1] += 1
    if not row == len(matrix) - 1 and not col == 0:
        if not matrix[row + 1][col - 1] == "*":
            matrix[row + 1][col - 1] += 1


size = int(input())
field = [[0] * size for _ in range(size)]
count_of_bombs = int(input())
for _ in range(count_of_bombs):
    bomb = input()
    insert_bomb(field, bomb[1:-1])

for element in field:
    print(*element, sep=' ')
