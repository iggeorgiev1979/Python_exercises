def top_bottom(matrix, row, start, ending):
    result = []
    for i in range(start, ending + 1):
        result.append(matrix[row][i])
    if len(set(result)) == 1:
        return True
    return False


def left_right(matrix, column, start, ending):
    result = []
    for i in range(start, ending + 1):
        result.append(matrix[i][column])
    if len(set(result)) == 1:
        return True
    return False


matrix_dimensions = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(matrix_dimensions[0])]
result = 0
result_list = []
for row_start in range(matrix_dimensions[0]):
    for row_end in range(row_start, matrix_dimensions[0]):
        for column_start in range(matrix_dimensions[1]):
            for column_end in range(column_start, matrix_dimensions[1]):
                roof_boolean = top_bottom(matrix, row_start, column_start, column_end)
                bottom_boolean = top_bottom(matrix, row_end, column_start, column_end)
                left_boolean = left_right(matrix, column_start, row_start, row_end)
                right_boolean = left_right(matrix, column_end, row_start, row_end)
                if roof_boolean and bottom_boolean and right_boolean and left_boolean:
                    result_list.append([(row_end - row_start) + 1, (column_end - column_start) + 1])

for element in result_list:
    if element[0] * element[1] > result:
        result = element[0] * element[1]
result_list = list(filter(lambda x: x[0] * x[1] == result, result_list))
result_list = [f'{x[0]}x{x[1]}' for x in result_list]
print(*sorted(result_list), sep=', ')
