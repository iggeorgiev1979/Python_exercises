from collections import deque


def add(toy: str):
    if toy not in toys.keys():
        toys[toy] = 0
    toys[toy] += 1


toys_magic_level = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

toys = {}
materials = [int(el) for el in input().split()]
magic = deque(int(el) for el in input().split())
current_material = None
current_magic = None

while len(materials) > 0 and len(magic) > 0:
    if not current_material:
        current_material = materials.pop()
    if not current_magic:
        current_magic = magic.popleft()

    current_toy = current_material * current_magic
    if current_toy in toys_magic_level.keys():
        add(toys_magic_level[current_toy])
        current_material = None
        current_magic = None
    elif current_toy == 0:
        if not current_magic == 0:
            magic.appendleft(current_magic)
        if not current_material == 0:
            materials.append(current_material)
        current_material = None
        current_magic = None
    elif current_toy < 0:
        materials.append(current_material + current_magic)
        current_material = None
        current_magic = None
    else:
        current_material += 15
        current_magic = None

if current_material:
    materials.append(current_material)
if current_magic:
    magic.appendleft(current_magic)


if ('Doll' in toys.keys() and 'Wooden train' in toys.keys()) or ('Teddy bear' in toys.keys() and 'Bicycle' in toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials) > 0:
    print("Materials left: ", end="")
    print(*reversed(materials), sep=', ')

if len(magic) > 0:
    print("Magic left: ", end='')
    print(*magic, sep=', ')

print(*[f'{i}: {j}' for i, j in sorted(toys.items(), key=lambda x: x[0])], sep='\n')
