countries = dict(zip(input().split(', '), input().split(', ')))
print(*[f'{i} -> {j}' for (i, j) in countries.items()], sep='\n')
