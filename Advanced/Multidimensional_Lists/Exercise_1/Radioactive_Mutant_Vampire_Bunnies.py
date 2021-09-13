def move(matrix, direction, size):
    if direction == 'U':
        if not player[0] == 0:
            matrix[player[0]][player[1]] = '.'
            if matrix[player[0] - 1][player[1]] == '.':
                matrix[player[0] - 1][player[1]] = 'P'
                el1 = player[0] - 1
                el2 = player[1]
                return [el1, el2]
            elif matrix[player[0] - 1][player[1]] == 'B':
                el1 = player[0] - 1
                el2 = player[1]
                return ['d', el1, el2]
        else:
            matrix[player[0]][player[1]] = '.'
            el1 = player[0]
            el2 = player[1]
            return ['w', el1, el2]
    elif direction == 'D':
        if not player[0] > size[0] - 2:
            matrix[player[0]][player[1]] = '.'
            if matrix[player[0] + 1][player[1]] == '.':
                matrix[player[0] + 1][player[1]] = 'P'
                el1 = player[0] + 1
                el2 = player[1]
                return [el1, el2]
            elif matrix[player[0] + 1][player[1]] == 'B':
                el1 = player[0] + 1
                el2 = player[1]
                return ['d', el1, el2]
        else:
            matrix[player[0]][player[1]] = '.'
            el1 = player[0]
            el2 = player[1]
            return ['w', el1, el2]
    elif direction == 'L':
        if not player[1] == 0:
            matrix[player[0]][player[1]] = '.'
            if matrix[player[0]][player[1] - 1] == '.':
                matrix[player[0]][player[1] - 1] = 'P'
                el1 = player[0]
                el2 = player[1] - 1
                return [el1, el2]
            elif matrix[player[0]][player[1] - 1] == 'B':
                el1 = player[0]
                el2 = player[1] - 1
                return ['d', el1, el2]
        else:
            matrix[player[0]][player[1]] = '.'
            el1 = player[0]
            el2 = player[1]
            return ['w', el1, el2]
    elif direction == 'R':
        if not player[1] > size[1] - 2:
            matrix[player[0]][player[1]] = '.'
            if matrix[player[0]][player[1] + 1] == '.':
                matrix[player[0]][player[1] + 1] = 'P'
                el1 = player[0]
                el2 = player[1] + 1
                return [el1, el2]
            elif matrix[player[0]][player[1] + 1] == 'B':
                el1 = player[0]
                el2 = player[1] + 1
                return ['d', el1, el2]
        else:
            matrix[player[0]][player[1]] = '.'
            el1 = player[0]
            el2 = player[1]
            return ['w', el1, el2]


def spread(matrix, player, size):
    previous_elements = []
    for i in range(size[0]):
        for j in range(size[1]):
            if matrix[i][j] == 'B' and [i, j] not in previous_elements:
                if not i == 0:
                    if matrix[i - 1][j] == '.' or matrix[i - 1][j] == 'P':         # up
                        if matrix[i - 1][j] == 'P':
                            player.insert(0, 'd')
                        matrix[i - 1][j] = 'B'
                        previous_elements.append([i - 1, j])
                if not i > size[0] - 2:
                    if matrix[i + 1][j] == '.' or matrix[i + 1][j] == 'P':        # down
                        if matrix[i + 1][j] == 'P':
                            player.insert(0, 'd')
                        matrix[i + 1][j] = 'B'
                        previous_elements.append([i + 1, j])
                if not j == 0:
                    if matrix[i][j - 1] == '.' or matrix[i][j - 1] == 'P':        # left
                        if matrix[i][j - 1] == 'P':
                            player.insert(0, 'd')
                        matrix[i][j - 1] = 'B'
                        previous_elements.append([i, j - 1])
                if not j > size[1] - 2:
                    if matrix[i][j + 1] == '.' or matrix[i][j + 1] == 'P':       # right
                        if matrix[i][j + 1] == 'P':
                            player.insert(0, 'd')
                        matrix[i][j + 1] = 'B'
                        previous_elements.append([i, j + 1])


size = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(size[0])]
player = [[i, j] for i in range(size[0]) for j in range(size[1]) if matrix[i][j] == 'P'][0]
command = list(input())
for direction in command:
    player = move(matrix, direction, size)
    spread(matrix, player, size)
    if player[0] == 'd':
        matrix = [''.join(x) for x in matrix]
        print(*matrix, sep='\n')
        print(f"dead: {player[1]} {player[2]}")
        break
    if player[0] == 'w':
        matrix = [''.join(x) for x in matrix]
        print(*matrix, sep='\n')
        print(f"won: {player[1]} {player[2]}")
        break
