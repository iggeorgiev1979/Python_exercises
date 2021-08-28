products = {}
while True:
    command = input().split()
    if command[0] == 'buy':
        break
    if command[0] not in products.keys():
        products[command[0]] = [0, 0]
    tmp_list = products.get(command[0])
    if not tmp_list[0] == float(command[1]):
        tmp_list[0] = float(command[1])
    tmp_list[1] += int(command[2])
print(*[f'{i} -> {j[0] * j[1]:.2f}' for (i, j) in products.items()], sep='\n')
