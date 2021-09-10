def orders(a, b):
    if a == 'coffee':
        return b * 1.5
    elif a == 'water':
        return b
    elif a == 'coke':
        return b * 1.4
    elif a == 'snacks':
        return b * 2


a = input()
b = int(input())
print(f'{orders(a, b):.2f}')