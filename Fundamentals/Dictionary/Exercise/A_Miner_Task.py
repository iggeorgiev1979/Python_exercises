resources = {}
while True:
    metal = input()
    if metal == 'stop':
        break
    quantity = int(input())
    if metal not in resources:
        resources[metal] = 0
    resources[metal] += quantity
print(*[f'{i} -> {j}' for (i, j) in resources.items()], sep='\n')
