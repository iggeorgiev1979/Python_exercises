import sys
from io import StringIO

input_1 = """3
3
---
-*-
--e"""

input_2 = """3
5
-**-e
-----
*****"""

sys.stdin = StringIO(input_1)


def check_up(labyrinth: list, row, col):
    if not row < 0:
        if labyrinth[row][col] == "-" or labyrinth[row][col] == "e":
            return True
    return False


def check_right(labyrinth: list, row, col):
    if not col == len(labyrinth[0]):
        if labyrinth[row][col] == "-" or labyrinth[row][col] == "e":
            return True
    return False


def check_down(labyrinth: list, row, col):
    if not row == len(labyrinth):
        if labyrinth[row][col] == "-" or labyrinth[row][col] == "e":
            return True
    return False


def check_left(labyrinth: list, row, col):
    if not col < 0:
        if labyrinth[row][col] == "-" or labyrinth[row][col] == "e":
            return True
    return False


def last_direction_assign(path: list):
    if path:
        return path[-1]
    return


def delete_last_direction(path):
    path.pop()


def find_paths(labyrinth: list, row=0, col=0, path=[]):
    if labyrinth[row][col] == "e":
        print("".join(path))
        delete_last_direction(path)
        return

    last_direction = last_direction_assign(path)

    if not last_direction == "D" and check_up(labyrinth, row - 1, col):
        path.append("U")
        find_paths(labyrinth, row - 1, col, path)

    if not last_direction == "L" and check_right(labyrinth, row, col + 1, ):
        path.append("R")
        find_paths(labyrinth, row, col + 1, path)

    if not last_direction == "U" and check_down(labyrinth, row + 1, col):
        path.append("D")
        find_paths(labyrinth, row + 1, col, path)

    if not last_direction == "R" and check_left(labyrinth, row, col - 1):
        path.append("L")
        find_paths(labyrinth, row, col - 1, path)
    if path:
        delete_last_direction(path)
    last_direction = last_direction_assign(path)


rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]

find_paths(matrix)
