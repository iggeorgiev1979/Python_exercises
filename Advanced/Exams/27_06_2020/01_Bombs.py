import sys
from collections import deque
from io import StringIO

# input_1 = """5, 25, 25, 115
# 5, 15, 25, 35"""
#
# input_2 = """30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
# 20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10"""
#
# sys.stdin = StringIO(input_2)


def mix(effects: deque, casing: list):
    ef = effects.popleft()
    cas = casing.pop()
    tmp_value = ef + cas
    if tmp_value == 40:
        return 1, 0, 0
    elif tmp_value == 60:
        return 0, 1, 0
    elif tmp_value == 120:
        return 0, 0, 1
    effects.appendleft(ef)
    casing.append(cas - 5)
    return 0, 0, 0


bomb_effects = deque(int(el) for el in input().split(', '))
bomb_casing = [int(el) for el in input().split(', ')]

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0
while len(bomb_effects) > 0 and len(bomb_casing) > 0:
    d, c, s = mix(bomb_effects, bomb_casing)
    datura_bombs += d
    cherry_bombs += c
    smoke_decoy_bombs += s
    if datura_bombs > 2 and cherry_bombs > 2 and smoke_decoy_bombs > 2:
        break

if datura_bombs > 2 and cherry_bombs > 2 and smoke_decoy_bombs > 2:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) == 0:
    print("Bomb Effects: empty")
else:
    print("Bomb Effects: ", end='')
    print(*bomb_effects, sep=', ')

if len(bomb_casing) == 0:
    print("Bomb Casings: empty")
else:
    print("Bomb Casings: ", end='')
    print(*bomb_casing, sep=', ')

print(f"Cherry Bombs: {cherry_bombs}\nDatura Bombs: {datura_bombs}\nSmoke Decoy Bombs: {smoke_decoy_bombs}")

