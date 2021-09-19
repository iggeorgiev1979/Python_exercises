def move_up(row, col, tea):
    field[row][col] = "*"
    row -= 1
    if row < 0:
        return False, False, False
    if field[row][col] == "R":
        field[row][col] = "*"
        return False, False, False
    if field[row][col] == ".":
        field[row][col] = "*"
        return row, col, tea
    if not field[row][col] == "*":
        tea += int(field[row][col])
    field[row][col] = "*"
    return row, col, tea


def move_down(row, col, tea):
    field[row][col] = "*"
    row += 1
    if row > len(field) - 1:
        return False, False, False
    if field[row][col] == "R":
        field[row][col] = "*"
        return False, False, False
    if field[row][col] == ".":
        field[row][col] = "*"
        return row, col, tea
    if not field[row][col] == "*":
        tea += int(field[row][col])
    field[row][col] = "*"
    return row, col, tea


def move_right(row, col, tea):
    field[row][col] = "*"
    col += 1
    if col > len(field) - 1:
        return False, False, False
    if field[row][col] == "R":
        field[row][col] = "*"
        return False, False, False
    if field[row][col] == ".":
        field[row][col] = "*"
        return row, col, tea
    if not field[row][col] == "*":
        tea += int(field[row][col])
    field[row][col] = "*"
    return row, col, tea


def move_left(row, col, tea):
    field[row][col] = "*"
    col -= 1
    if col < 0:
        return False, False, False
    if field[row][col] == "R":
        field[row][col] = "*"
        return False, False, False
    if field[row][col] == ".":
        field[row][col] = "*"
        return row, col, tea
    if not field[row][col] == "*":
        tea += int(field[row][col])
    field[row][col] = "*"
    return row, col, tea


def find_alice(field_size):
    for row in range(field_size):
        for col in range(field_size):
            if field[row][col] == "A":
                return row, col


size = int(input())
field = []
bags_of_tea = 0
for _ in range(size):
    field.append(input().split())

position_row, position_col = find_alice(size)

while True:
    direction = input()
    if direction == "right":
        position_row, position_col, bags_of_tea = move_right(position_row, position_col, bags_of_tea)
    elif direction == "left":
        position_row, position_col, bags_of_tea = move_left(position_row, position_col, bags_of_tea)
    elif direction == "up":
        position_row, position_col, bags_of_tea = move_up(position_row, position_col, bags_of_tea)
    elif direction == "down":
        position_row, position_col, bags_of_tea = move_down(position_row, position_col, bags_of_tea)

    if bags_of_tea is False or bags_of_tea >= 10:
        break

print("Alice didn't make it to the tea party.") if not bags_of_tea else print("She did it! She went to the party.")
for el in field:
    print(*el)
"""
5
A . . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
"""