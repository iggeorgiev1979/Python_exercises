items = {'fragments': 0, 'shards': 0, 'motes': 0}
winner = ''
while True:
    tmp_list = input().lower().split()
    boolean = False
    for el in range(1, len(tmp_list), 2):
        if tmp_list[el] not in items.keys():
            items[tmp_list[el]] = 0
        items[tmp_list[el]] += int(tmp_list[el - 1])
        if items[tmp_list[el]] >= 250:
            if tmp_list[el] == 'shards' or tmp_list[el] == 'fragments' or tmp_list[el] == 'motes':
                boolean = True
                winner = tmp_list[el]
                break
    if boolean:
        break
if winner == 'shards':
    items[winner] -= 250
    winner = 'Shadowmourne'
elif winner == 'fragments':
    items[winner] -= 250
    winner = 'Valanyr'
elif winner == 'motes':
    items[winner] -= 250
    winner = 'Dragonwrath'
key_items = {i: j for (i, j) in items.items() if i == 'shards' or i == 'fragments' or i == 'motes'}
junk = {i: j for (i, j) in items.items() if i not in key_items.keys()}
key_items = dict(sorted(key_items.items(), key=lambda x: (-x[1], x[0])))
junk = dict(sorted(junk.items(), key=lambda x: x[0]))
print(f'{winner} obtained!')
print(*[f'{i}: {j}' for (i, j) in key_items.items()], sep='\n')
print(*[f'{i}: {j}' for (i, j) in junk.items()], sep='\n')
