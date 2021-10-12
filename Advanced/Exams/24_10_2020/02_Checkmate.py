import sys
from io import StringIO

input_1 = '''. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .'''

input_2 = '''. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .'''

input_3 = """. . . . . . . .
. . . . . Q . .
. . . Q . Q . Q
. . . . Q . . .
. . Q Q . . . Q
. . . . . Q . .
. . . Q . Q . Q
K Q . . . . . ."""

sys.stdin = StringIO(input_1)


def find_king(board: list):
    for row in range(8):
        for col in range(8):
            if board[row][col] == "K":
                return [row, col]


def check_vertical(board: list, position: list, queens: list):
    row, col = position
    tmp = ''
    for index in range(8):
        if index <= row:
            if board[index][col] == "Q":
                tmp = [index, col]
            elif board[index][col] == "K" and tmp:
                queens.append(tmp)
        else:
            if board[index][col] == "Q":
                queens.append([index, col])
                break


def check_horizontal(board: list, position: list, queens: list):
    row, col = position
    tmp = ''
    for index in range(8):
        if index <= col:
            if board[row][index] == "Q":
                tmp = [row, index]
            elif board[row][index] == "K" and tmp:
                queens.append(tmp)
        else:
            if board[row][index] == "Q":
                queens.append([row, index])
                break


def check_left_diagonal(board: list, position: list, queens: list):
    row, col = position
    tmp_number = row - col
    if tmp_number >= 0:
        row = tmp_number
        col = 0
    else:
        row = 0
        col = abs(tmp_number)
    tmp = ''
    for _ in range(8):
        if row <= position[0]:
            if board[row][col] == "Q":
                tmp = [row, col]
            elif board[row][col] == "K" and tmp:
                queens.append(tmp)
        else:
            if row > 7 or col > 7:
                break
            if board[row][col] == "Q":
                queens.append([row, col])
                break
        row += 1
        col += 1


def check_right_diagonal(board: list, position: list, queens: list):
    tmp_number = position[0] + position[1]
    if tmp_number <= 7:
        row = tmp_number
        col = 0
    else:
        row = 7
        col = tmp_number - 7
    tmp = ''
    for _ in range(8):
        if row >= position[0]:
            if board[row][col] == "Q":
                tmp = [row, col]
            elif board[row][col] == "K" and tmp:
                queens.append(tmp)
        else:
            if row < 0 or col > 7:
                break
            if board[row][col] == "Q":
                queens.append([row, col])
                break
        row -= 1
        col += 1


matrix = [input().split() for _ in range(8)]
result_queens = []
king_position = find_king(matrix)
check_vertical(matrix, king_position, result_queens)
check_horizontal(matrix, king_position, result_queens)
check_left_diagonal(matrix, king_position, result_queens)
check_right_diagonal(matrix, king_position, result_queens)

print(*result_queens, sep='\n') if result_queens else print("The king is safe!")

