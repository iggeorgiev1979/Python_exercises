def find_position_and_targets():
    targets = 0
    shooter = []
    for row in range(5):
        for col in range(5):
            if field[row][col] == "A":
                shooter = [row, col]
            elif field[row][col] == "x":
                targets += 1
    return shooter, targets


def move_left(row, col, steps):
    new_col = col - steps
    if not new_col < 0 and field[row][new_col] == ".":
        field[row][col] = "."
        field[row][new_col] = "A"
        return [row, new_col]
    return [row, col]


def move_right(row, col, steps):
    new_col = col + steps
    if not new_col > 4 and field[row][new_col] == ".":
        field[row][col] = "."
        field[row][new_col] = "A"
        return [row, new_col]
    return [row, col]


def move_up(row, col, steps):
    new_row = row - steps
    if not new_row < 0 and field[new_row][col] == ".":
        field[row][col] = "."
        field[new_row][col] = "A"
        return [new_row, col]
    return [row, col]


def move_down(row, col, steps):
    new_row = row + steps
    if not new_row > 4 and field[new_row][col] == ".":
        field[row][col] = "."
        field[new_row][col] = "A"
        return [new_row, col]
    return [row, col]


def shoot_up(row, col):
    for rr in range(row, -1, -1):
        if field[rr][col] == "x":
            targets_down.append([rr, col])
            field[rr][col] = "."
            return True
    return False


def shoot_down(row, col):
    for rr in range(row, 5):
        if field[rr][col] == "x":
            targets_down.append([rr, col])
            field[rr][col] = "."
            return True
    return False


def shoot_left(row, col):
    for cc in range(col, -1, -1):
        if field[row][cc] == "x":
            targets_down.append([row, cc])
            field[row][cc] = "."
            return True
    return False


def shoot_right(row, col):
    for cc in range(col, 5):
        if field[row][cc] == "x":
            targets_down.append([row, cc])
            field[row][cc] = "."
            return True
    return False


field = []
targets_down = []
for _ in range(5):
    field.append(input().split())

player, tar = find_position_and_targets()

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "shoot":
        if command[1] == "right":
            tmp = shoot_right(player[0], player[1])
            if tmp:
                tar -= 1
        elif command[1] == "left":
            tmp = shoot_left(player[0], player[1])
            if tmp:
                tar -= 1
        elif command[1] == "up":
            tmp = shoot_up(player[0], player[1])
            if tmp:
                tar -= 1
        elif command[1] == "down":
            tmp = shoot_down(player[0], player[1])
            if tmp:
                tar -= 1
    elif command[0] == "move":
        if command[1] == "right":
            player = move_right(player[0], player[1], int(command[2]))
        elif command[1] == "left":
            player = move_left(player[0], player[1], int(command[2]))
        elif command[1] == "up":
            player = move_up(player[0], player[1], int(command[2]))
        elif command[1] == "down":
            player = move_down(player[0], player[1], int(command[2]))

    if tar == 0:
        break

print("Training not completed!", end=" ") if not tar == 0 else print("Training completed!", end=" ")
print(f'All {len(targets_down)} targets hit.') if tar == 0 else print(f'{tar} targets left.')

print(*targets_down, sep='\n')
