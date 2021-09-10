price = 0
while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    money = float(command)

    if money < 0:
        print('Invalid price!')
    else:
        price += money
total_price = price * 1.2
if command == 'special':
    total_price -= total_price * 0.1

print('Invalid order!') if price == 0 else print(
    f'Congratulations you\'ve just bought a new computer!\nPrice without taxes: {price:.2f}$\nTaxes: {price * 0.2:.2f}$\n-----------\nTotal price: {total_price:.2f}$')
