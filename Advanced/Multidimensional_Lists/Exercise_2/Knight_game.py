def move(matrix, knight, n):
    counter = 0
    if not knight[0] == 0 and not knight[1] > n - 3:
        if matrix[knight[0] - 1][knight[1] + 2] == 'K':    # right_up
            counter += 1
    if not knight[0] > n - 2 and not knight[1] > n - 3:    # right_down
        if matrix[knight[0] + 1][knight[1] + 2] == 'K':
            counter += 1
    if not knight[0] == 0 and not knight[1] < 2:
        if matrix[knight[0] - 1][knight[1] - 2] == 'K':    # left_up
            counter += 1
    if not knight[0] > n - 2 and not knight[1] < 2:
        if matrix[knight[0] + 1][knight[1] - 2] == 'K':    # left_down
            counter += 1
    if not knight[0] < 2 and not knight[1] > n - 2:
        if matrix[knight[0] - 2][knight[1] + 1] == 'K':    # up_right
            counter += 1
    if not knight[0] < 2 and not knight[1] == 0:
        if matrix[knight[0] - 2][knight[1] - 1] == 'K':    # up_left
            counter += 1
    if not knight[0] > n - 3 and not knight[1] > n - 2:
        if matrix[knight[0] + 2][knight[1] + 1] == 'K':    # down_right
            counter += 1
    if not knight[0] > n - 3 and not knight[1] == 0:
        if matrix[knight[0] + 2][knight[1] - 1] == 'K':    # down_left
            counter += 1
    return counter


n = int(input())
matrix = [list(x for x in input()) for _ in range(n)]
result = 0
for strength in range(8, 0, -1):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'K':
                if move(matrix, [i, j], n) == strength:
                    result += 1
                    matrix[i][j] = '0'
print(result)