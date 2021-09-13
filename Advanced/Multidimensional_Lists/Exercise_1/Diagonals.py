def sum_primary_diagonal(matrix: list):
    result = []
    sum_result = 0
    for index in range(len(matrix)):
        result.append(matrix[index][index])
        sum_result += int(matrix[index][index])
    return result, sum_result


def sum_secondary_diagonal(matrix: list):
    result = []
    sum_result = 0
    for index in range(len(matrix)):
        result.append(matrix[index][len(matrix) - 1 - index])
        sum_result += int(matrix[index][len(matrix) - 1 - index])
    return result, sum_result


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([el for el in input().split(', ')])

primary, sum_primary = sum_primary_diagonal(matrix)
secondary, sum_secondary = sum_secondary_diagonal(matrix)

print(f'Primary diagonal: {", ".join(primary)}. Sum: {sum_primary}')
print(f'Secondary diagonal: {", ".join(secondary)}. Sum: {sum_secondary}')
