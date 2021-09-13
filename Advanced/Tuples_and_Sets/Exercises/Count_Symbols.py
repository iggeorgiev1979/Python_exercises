text = input()
elements = {}
for el in text:
    if el not in elements.keys():
        elements[el] = 0
    elements[el] += 1

for key in sorted(elements.keys(), key=lambda x: x[0]):
    print(f'{key}: {elements[key]} time/s')
