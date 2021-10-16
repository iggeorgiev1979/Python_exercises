def check_up(row, col):
    for index in range(row, -1, -1):
        if board[index][col] == "Q":
            return False
    return True


def check_diagonal(row, col):
    for index in range(row, -1, -1):
        if board[index][col] == "Q":
            return False
        if col > 0:
            col -= 1
        else:
            return True
    return True


def check_right_diagonal(row, col):
    for index in range(row, -1, -1):
        if board[index][col] == "Q":
            return False
        if col < 7:
            col += 1
        else:
            return True
    return True


def check_left(row, col):
    for index in range(col, -1, -1):
        if board[row][index] == "Q":
            return False
    return True


def clear_row(row):
    if queens[-1][0] == row:
        board[queens[-1][0]][queens[-1][1]] = "-"
        if not row == 0:
            queens.pop()


def print_board():
    print(*[" ".join(el) for el in board], sep='\n')
    counter.append(1)


def place_queen(row=0, col=0):
    if row == 8:
        print_board()
        return

    for col in range(8):
        if check_up(row, col) and check_left(row, col) and check_diagonal(row, col) and check_right_diagonal(row, col):
            if [row, col] not in queens:
                board[row][col] = "Q"
                queens.append([row, col])
                place_queen(row + 1)
        clear_row(row)


board = [["-"] * 8 for _ in range(8)]
queens = []
counter = []
place_queen()
print(len(counter))
