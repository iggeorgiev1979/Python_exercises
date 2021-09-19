def add(row_index: int, col_index: int, number: int):
    matrix[row_index][col_index] += number


def subtract(row_index: int, col_index: int, number: int):
    matrix[row_index][col_index] -= number


def check_indexes(row_index: int, col_index: int):
    if 0 <= row_index < n and 0 <= col_index < n:
        return True
    print("Invalid coordinates")
    return False


def print_matrix():
    for el in matrix:
        print(*el)


"""
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
"""

n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

command = input()

while not command == 'END':
    action, row, col, num = command.split()
    if check_indexes(int(row), int(col)):
        if action == 'Add':
            add(int(row), int(col), int(num))
        elif action == 'Subtract':
            subtract(int(row), int(col), int(num))

    command = input()
print_matrix()