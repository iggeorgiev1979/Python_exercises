def find_player_position(field: list, n: int):
    for row in range(n):
        for col in range(n):
            if field[row][col] == 'P':
                return [row, col]


def move_up(field: list, result: str, position: list):
    row, col = position
    if row == 0:
        if result:
            result = result[:-1]
        return result, position
    field[row][col] = "-"
    row -= 1
    if field[row][col].isalpha():
        result += field[row][col]
        field[row][col] = "P"
    return result, [row, col]


def move_down(field: list, result: str, position: list, field_size):
    row, col = position
    if row == field_size - 1:
        if result:
            result = result[:-1]
        return result, position
    field[row][col] = "-"
    row += 1
    if field[row][col].isalpha():
        result += field[row][col]
        field[row][col] = "P"
    return result, [row, col]


def move_left(field: list, result: str, position: list):
    row, col = position
    if col == 0:
        if result:
            result = result[:-1]
        return result, position
    field[row][col] = "-"
    col -= 1
    if field[row][col].isalpha():
        result += field[row][col]
        field[row][col] = "P"
    return result, [row, col]


def move_right(field: list, result: str, position: list, field_size):
    row, col = position
    if col == field_size - 1:
        if result:
            result = result[:-1]
        return result, position
    field[row][col] = "-"
    col += 1
    if field[row][col].isalpha():
        result += field[row][col]
        field[row][col] = "P"
    return result, [row, col]


result_string = input()
size = int(input())
matrix = [list(input()) for _ in range(size)]
moves = int(input())
player_position = find_player_position(matrix, size)

for _ in range(moves):
    direction = input()
    if direction == "up":
        result_string, player_position = move_up(matrix, result_string, player_position)
    elif direction == "down":
        result_string, player_position = move_down(matrix, result_string, player_position, size)

    elif direction == "left":
        result_string, player_position = move_left(matrix, result_string, player_position)

    elif direction == "right":
        result_string, player_position = move_right(matrix, result_string, player_position, size)
print(result_string)
print(*["".join(el) for el in matrix], sep='\n')