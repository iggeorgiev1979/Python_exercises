items = input().split()
items_dict = {}
for el in range(0, len(items), 2):
    items_dict[items[el]] = int(items[el + 1])
print(items_dict)
