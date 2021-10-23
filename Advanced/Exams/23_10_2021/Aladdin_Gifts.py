import sys
from collections import deque
from io import StringIO

input_1 = """105 20 30 25
120 60 11 400 10 1"""

input_2 = """30 5 21 6 0 91
15 9 5 15 8"""

input_3 = """200
5 15 32 20 10 5"""

# sys.stdin = StringIO(input_2)


def mix(material: int, magic: int):
    product = material + magic
    if product < 100:
        if product % 2 == 0:
            material *= 2
            magic *= 3
            product = material + magic
        else:
            product *= 2
    elif product > 499:
        product /= 2

    if 100 <= product <= 199:
        presents["Gemstone"] += 1
    elif 200 <= product <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= product <= 399:
        presents["Gold"] += 1
    elif 400 <= product <= 499:
        presents["Diamond Jewellery"] += 1


materials = [int(el) for el in input().split()]
magics = deque(int(el) for el in input().split())
presents = {
    "Diamond Jewellery": 0,
    "Gemstone": 0,
    "Gold": 0,
    "Porcelain Sculpture": 0,
}


while len(materials) > 0 and len(magics) > 0:
    material = materials.pop()
    magic = magics.popleft()
    mix(material, magic)

txt_msg = "Aladdin does not have enough wedding presents."

if presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0:
    txt_msg = "The wedding presents are made!"
elif presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0:
    txt_msg = "The wedding presents are made!"
print(txt_msg)
if materials:
    print("Materials left: ", end='')
    print(*materials, sep=", ")
if magics:
    print("Magic left: ", end='')
    print(*magics, sep=", ")

for key, value in presents.items():
    if value > 0:
        print(f"{key}: {value}")