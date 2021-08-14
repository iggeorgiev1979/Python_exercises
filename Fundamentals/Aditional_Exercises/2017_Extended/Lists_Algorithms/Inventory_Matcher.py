matrix_of_products = [input().split(), [int(x) for x in input().split()], [float(x) for x in input().split()]]
command = input()
while not command == 'done':
    index = matrix_of_products[0].index(command)
    print(f"{matrix_of_products[0][index]} costs: {matrix_of_products[2][index]}; Available quantity: {matrix_of_products[1][index]}")
    command = input()
