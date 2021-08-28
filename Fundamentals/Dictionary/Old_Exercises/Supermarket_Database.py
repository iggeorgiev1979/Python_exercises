def register(product: list, log: dict):
    if product[0] not in log.keys():
        log[product[0]] = [0, 0]
    log[product[0]][0] = float(product[1])
    log[product[0]][1] += int(product[2])


store = {}
item = input().split()
while not item[0] == 'stocked':
    register(item, store)
    item = input().split()
[print(f'{i}: ${j[0]:.2f} * {j[1]} = ${j[0] * j[1]:.2f}') for i, j in store.items()]
print('-' * 30)
el = [j[0] * j[1] for j in store.values()]
print(f'Grand Total: ${sum(el):.2f}')
