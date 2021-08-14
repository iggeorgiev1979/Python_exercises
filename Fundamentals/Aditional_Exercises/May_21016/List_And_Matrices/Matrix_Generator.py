def type_a(row, column):
    matrix = []
    for i in range(1, row + 1):
        row_list = []
        for j in range(i, row * column + 1, row):
            row_list.append(str(j))
            if len(row_list) == column:
                break
        matrix.append(' '.join(row_list))
    return matrix


def type_b(row, column):
    matrix = []
    tmp_matrix = []
    column_list = []
    counter = 0
    while not counter == row * column:
        counter += 1
        column_list.append(counter)
        if len(column_list) == row:
            if not len(tmp_matrix) % 2 == 0:
                column_list.reverse()
            tmp_matrix.append(column_list)
            column_list = []
    for i in range(row):
        tmp_list = []
        for j in range(column):
            tmp_list.append(tmp_matrix[j][i])
        tmp_list = [str(x) for x in tmp_list]
        matrix.append(' '.join(tmp_list))

    return matrix


def type_c(row, column):
    number = 1
    matrix = [list('0' * column) for i in range(row)]
    for i in range(len(matrix) - 1, -1, -1):
        place = 0
        for j in range(i, len(matrix)):
            matrix[j][place] = str(number)
            number += 1
            place += 1
    count = matrix[-1].count('0')
    for i in range(1, count + 1):
        p = i
        for r in range(len(matrix)):
            matrix[r][p] = str(number)
            number += 1
            p += 1
    count = len(matrix) - 1
    while number <= row * column:
        place = len(matrix[0]) - matrix[0].count('0')
        for i in range(count):
            matrix[i][place] = str(number)
            number += 1
            place += 1
        count -= 1
    tmp_matrix = [' '.join(matrix[i]) for i in range(len(matrix))]

    return tmp_matrix


def type_d(row, column):
    matrix = [list('0' * column) for i in range(row)]
    row_index = 0
    col_index = 0
    number = 1
    direction = 'down'
    while number <= row * column:
        if direction == 'down':
            if matrix[row_index][col_index] == '0':
                matrix[row_index][col_index] = str(number)
                number += 1
                if row_index < row - 1 and matrix[row_index + 1][col_index] == '0':
                    row_index += 1
                else:
                    direction = 'right'
            else:
                row_index += 1
        elif direction == 'right':
            if matrix[row_index][col_index] == '0':
                matrix[row_index][col_index] = str(number)
                number += 1
                if col_index < column - 1 and matrix[row_index][col_index + 1] == '0':
                    col_index += 1
                else:
                    direction = 'up'
            else:
                col_index += 1
        elif direction == 'up':
            if matrix[row_index][col_index] == '0':
                matrix[row_index][col_index] = str(number)
                number += 1
                if row_index > 0 and matrix[row_index - 1][col_index] == '0':
                    row_index -= 1
                else:
                    direction = 'left'
            else:
                row_index -= 1
        elif direction == 'left':
            if matrix[row_index][col_index] == '0':
                matrix[row_index][col_index] = str(number)
                number += 1
                if col_index > 0 and matrix[row_index][col_index - 1] == '0':
                    col_index -= 1
                else:
                    direction = 'down'
            else:
                col_index -= 1
    matrix = [' '.join(matrix[i]) for i in range(len(matrix))]
    return matrix


command = input().split()
if command[0] == 'A':
    result = type_a(int(command[1]), int(command[2]))
    print(*result, sep='\n')
elif command[0] == 'B':
    result = type_b(int(command[1]), int(command[2]))
    print(*result, sep='\n')
elif command[0] == 'C':
    result = type_c(int(command[1]), int(command[2]))
    print(*result, sep='\n')
elif command[0] == 'D':
    result = type_d(int(command[1]), int(command[2]))
    print(*result, sep='\n')
