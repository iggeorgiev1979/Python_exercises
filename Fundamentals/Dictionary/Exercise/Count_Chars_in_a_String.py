text = input()
result = {}
result = {el: text.count(el) for el in text if not el == ' ' and el not in result.keys()}
print(*[f'{index_1} -> {index_2}' for (index_1, index_2) in result.items()], sep='\n')
