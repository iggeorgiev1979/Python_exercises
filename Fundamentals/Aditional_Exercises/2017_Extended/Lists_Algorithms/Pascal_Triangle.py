matrix = [['1'], ['1', '1']]
n = int(input())
row = 3
while row <= n:
    element = '1'
    for i in range(1, row - 1):
        element += f' {int(matrix[row - 2][i]) + int(matrix[row - 2][i - 1])}'
    element += ' 1'
    row += 1
    matrix.append(element.split())
matrix = [' '.join(x) for x in matrix]
print(*matrix, sep='\n')
