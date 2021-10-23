# import sys
# from io import StringIO
#
# input_1 = """10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 В
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)"""
#
# input_2 = """B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)"""

# sys.stdin = StringIO(input_2)


def check_throw(coordinates: str):
    row, col = coordinates.split(", ")
    row = int(row)
    col = int(col)
    if 0 <= row < 6 and 0 <= col < 6:
        if board[row][col] == "B":
            board[row][col] = "X"
            return calculate_points(col)
    return 0


def calculate_points(col):
    result = 0
    for row in range(6):
        el = board[row][col]
        if el.isnumeric():
            result += int(el)
    return result


def gift(points):
    if 100 <= points < 200:
        return "Football"
    if 200 <= points < 300:
        return "Teddy Bear"
    if points >= 300:
        return "Lego Construction Set"


board = [input().split() for _ in range(6)]
total_points = 0

for _ in range(3):
    throw = input()
    total_points += check_throw(throw[1:-1])

prize = gift(total_points)

if prize:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
