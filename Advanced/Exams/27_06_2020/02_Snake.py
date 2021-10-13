import sys
from io import StringIO

input_1 = """6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left"""

input_2 = """7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down"""

sys.stdin = StringIO(input_2)


def find_snake(matrix: list, matrix_size: int):
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "S":
                return [row, col]


def find_burrows(matrix: list, matrix_size: int):
    burrow_positions = []

    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "B":
                burrow_positions.append([row, col])
    if burrow_positions:
        return burrow_positions[0], burrow_positions[1]
    else:
        return False, False


def enter_the_burrow(matrix: list, door_1: list, door_2: list, position: list):
    row, col = position
    matrix[row][col] = "."
    if not door_1 == [row, col]:
        row, col = door_1
    else:
        row, col = door_2
    matrix[row][col] = "S"
    return [row, col]


def move_up(matrix: list, coordinates: list, door_1, door_2):
    row, col = coordinates
    if not row == 0:
        matrix[row][col] = "."
        row -= 1
        if matrix[row][col] == "*":
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 1, True
        elif matrix[row][col] == "B":
            row, col = enter_the_burrow(matrix, door_1, door_2, [row, col])
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
        else:
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
    matrix[row][col] = "."
    return 0, False


def move_down(matrix: list, matrix_size: int, coordinates: list, door_1, door_2):
    row, col = coordinates
    if not row == matrix_size - 1:
        matrix[row][col] = "."
        row += 1
        if matrix[row][col] == "*":
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 1, True
        elif matrix[row][col] == "B":
            row, col = enter_the_burrow(matrix, door_1, door_2, [row, col])
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
        else:
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
    matrix[row][col] = "."
    return 0, False


def move_left(matrix: list, coordinates: list, door_1, door_2):
    row, col = coordinates
    if not col == 0:
        matrix[row][col] = "."
        col -= 1
        if matrix[row][col] == "*":
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 1, True
        elif matrix[row][col] == "B":
            row, col = enter_the_burrow(matrix, door_1, door_2, [row, col])
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
        else:
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
    matrix[row][col] = "."
    return 0, False


def move_right(matrix: list, matrix_size: int, coordinates: list, door_1, door_2):
    row, col = coordinates
    if not col == matrix_size - 1:
        matrix[row][col] = "."
        col += 1
        if matrix[row][col] == "*":
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 1, True
        elif matrix[row][col] == "B":
            row, col = enter_the_burrow(matrix, door_1, door_2, [row, col])
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
        else:
            matrix[row][col] = "S"
            coordinates[0] = row
            coordinates[1] = col
            return 0, True
    matrix[row][col] = "."
    return 0, False


size = int(input())
field = [list(input()) for _ in range(size)]
snake_position = find_snake(field, size)
burrow_1, burrow_2 = find_burrows(field, size)
play = True
food = 0

while play:
    command = input()
    if command == "up":
        f, play = move_up(field, snake_position, burrow_1, burrow_2)
        food += f
    elif command == "down":
        f, play = move_down(field, size, snake_position, burrow_1, burrow_2)
        food += f
    elif command == "left":
        f, play = move_left(field, snake_position, burrow_1, burrow_2)
        food += f
    elif command == "right":
        f, play = move_right(field, size, snake_position, burrow_1, burrow_2)
        food += f
    if food == 10:
        break

if food == 10:
    print(f"You won! You fed the snake.\nFood eaten: {food}")
    print(*["".join(el) for el in field], sep='\n')
else:
    print(f"Game over!\nFood eaten: {food}")
    print(*["".join(el) for el in field], sep='\n')
