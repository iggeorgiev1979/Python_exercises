items = input().split()
items_to_search = input().split()
items_dict = {}
for el in range(0, len(items), 2):
    items_dict[items[el]] = int(items[el + 1])
for el in items_to_search:
    print(f'We have {items_dict[el]} of {el} left') if el in items_dict.keys() else print(f'Sorry, we don\'t have {el}')