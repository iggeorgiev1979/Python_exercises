def swap(matrix, a, b, c, d):
    try:
        matrix[a][b], matrix[c][d] = matrix[c][d], matrix[a][b]
        matrix = [' '.join(x) for x in matrix]
        return matrix
    except:
        return f'Invalid input!'

size = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(size[0])]
command = input().split()
while not command[0] == 'END':
    if command[0] == 'swap' and len(command) == 5 and command[1].isnumeric() and command[2].isnumeric() and command[3].isnumeric() and command[4].isnumeric():
        result = swap(matrix, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        if not result == 'Invalid input!':
            print(*result, sep='\n')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input().split()
