def order(product, quantity, price, quantity_available):
    if quantity <= quantity_available:
        print(f'{product} x {quantity} costs {quantity * price:.2f}')
        return quantity_available - quantity
    else:
        print(f'We do not have enough {product}')
        return 0


products = input().split()
available = [int(x) for x in input().split()]
cost = [float(x) for x in input().split()]
command = input().split()
while not len(products) == len(available):
    available.append(0)
while not command[0] == 'done':
    place = products.index(command[0])
    available[place] = order(command[0], int(command[1]), cost[place], available[place])
    command = input().split()
