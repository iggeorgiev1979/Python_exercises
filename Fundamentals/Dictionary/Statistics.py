products = {}
key_counter = 0
value_counter = 0
while True:
    command = input().split(': ')
    if command[0] == 'statistics':
        break
    if command[0] in products.keys():
        products[command[0]] += int(command[1])
    else:
        products[command[0]] = int(command[1])
print('Products in stock:')
for (key, value) in products.items():
    print(f'- {key}: {value}')
    key_counter += 1
    value_counter += value
print(f'Total Products: {key_counter}\nTotal Quantity: {value_counter}')
