def t(matrix, row, col):
    return (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 3


def d(matrix, row, col):
    return (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 2


player_1 = 501
player_2 = 501
turns_1 = 0
turns_2 = 0
counter = 0
name_1, name_2 = input().split(', ')

target = [input().split() for _ in range(7)]
while True:
    command = input()[1:-1].split(',')
    row = int(command[0])
    col = int(command[1])
    if not 0 <= row < 7 or not 0 <= col < 7:
        if counter % 2 == 0:
            turns_1 += 1
        else:
            turns_2 += 1
        pass
    elif target[row][col] == 'D':
        if counter % 2 == 0:
            player_1 -= d(target, row, col)
            turns_1 += 1
        else:
            player_2 -= d(target, row, col)
            turns_2 += 1
    elif target[row][col] == 'T':
        if counter % 2 == 0:
            player_1 -= t(target, row, col)
            turns_1 += 1
        else:
            player_2 -= t(target, row, col)
            turns_2 += 1
    elif target[row][col] == 'B':
        if counter % 2 == 0:
            player_1 = 0
            turns_1 += 1
        else:
            player_2 = 0
            turns_2 += 1
    else:
        if counter % 2 == 0:
            player_1 -= int(target[row][col])
            turns_1 += 1
        else:
            player_2 -= int(target[row][col])
            turns_2 += 1
    counter += 1
    if player_1 <= 0 or player_2 <= 0:
        break
print(f'{name_1} won the game with {turns_1} throws!') if player_1 <= 0 else print(f'{name_2} won the game with {turns_2} throws!')

