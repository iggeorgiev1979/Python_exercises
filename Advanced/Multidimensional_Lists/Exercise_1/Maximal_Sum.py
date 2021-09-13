import sys


def sum_matrix(matrix):
    result = 0
    for el in matrix:
        result += sum(el)
    return result


boolean = False
print_result = -sys.maxsize
result_matrix = []
size = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(size[0])]
if size[0] >= 3 and size[1] >= 3:
    boolean = True
    for i in range(0, size[0] - 2):
        for j in range(0, size[1] - 2):
            tmp_matrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]], [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]
            tmp_result = sum_matrix(tmp_matrix)
            if tmp_result > print_result:
                print_result = tmp_result
                result_matrix = tmp_matrix
else:
    print_result = sum_matrix(matrix)
    result_matrix = matrix
result_matrix = [[str(x) for x in el] for el in result_matrix]
result_matrix = [' '.join(el) for el in result_matrix]
print(f'Sum = {print_result}')
print(*result_matrix, sep='\n')
