def move_up(money: int, position: list):
    row, col = position
    if row == 0 or matrix[row - 1][col] == "X":
        return int(money * 0.5), False
    else:
        money += int(matrix[row - 1][col])
        matrix[row - 1][col] = 0
        moves.append([row - 1, col])
        position[0] -= 1
        return money, True


def move_down(money: int, position: list, n: int):
    row, col = position
    if row == n - 1 or matrix[row + 1][col] == "X":
        return int(money * 0.5), False
    else:
        money += int(matrix[row + 1][col])
        matrix[row + 1][col] = 0
        moves.append([row + 1, col])
        position[0] += 1
        return money, True


def move_left(money: int, position: list):
    row, col = position
    if col == 0 or matrix[row][col - 1] == "X":
        return int(money * 0.5), False
    else:
        money += int(matrix[row][col - 1])
        matrix[row][col - 1] = 0
        moves.append([row, col - 1])
        position[1] -= 1
        return money, True


def move_right(money: int, position: list, n: int):
    row, col = position
    if col == n - 1 or matrix[row][col + 1] == "X":
        return int(money * 0.5), False
    else:
        money += int(matrix[row][col + 1])
        matrix[row][col + 1] = 0
        moves.append([row, col + 1])
        position[1] += 1
        return money, True


def find_player_position(board: list, board_size: int):
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == "P":
                return [row, col]


size = int(input())
matrix = [input().split() for _ in range(size)]

player_position = find_player_position(matrix, size)
moves = []
coins = 0
play = True
while coins < 100:
    command = input()
    if command == "up":
        coins, play = move_up(coins, player_position)
    elif command == "down":
        coins, play = move_down(coins, player_position, size)
    elif command == "left":
        coins, play = move_left(coins, player_position)
    elif command == "right":
        coins, play = move_right(coins, player_position, size)
    if not play:
        break

print(f"You won! You've collected {coins} coins.") if play else print(f"Game over! You've collected {coins} coins.")
print("Your path:")
print(*moves, sep='\n')
