from collections import deque


def firework_assign(fire: deque):
    tmp = 0
    while tmp <= 0:
        if len(fire) == 0:
            return 0
        tmp = fire.popleft()
    return tmp


def explosive_assign(explosive: list):
    tmp = 0
    while tmp <= 0:
        if len(explosive) == 0:
            return 0
        tmp = explosive.pop()
    return tmp


def make_firework(fire_effect: int, power: int):
    sum_effect_and_power = fire_effect + power

    if sum_effect_and_power % 3 == 0 and not sum_effect_and_power % 5 == 0:
        return [1, 0, 0]
    elif sum_effect_and_power % 5 == 0 and not sum_effect_and_power % 3 == 0:
        return [0, 1, 0]
    elif sum_effect_and_power % 3 == 0 and sum_effect_and_power % 5 == 0:
        return [0, 0, 1]
    else:
        if fire_effect - 1 > 0:
            firework_effects.append(fire_effect - 1)
        explosive_power.append(power)
    return [0, 0, 0]


firework_effects = deque(int(el) for el in input().split(", "))
explosive_power = [int(el) for el in input().split(", ")]
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while len(firework_effects) > 0 and len(explosive_power) > 0:
    firework = firework_assign(firework_effects)
    explosive = explosive_assign(explosive_power)
    if firework == 0 or explosive == 0:
        if not firework == 0:
            firework_effects.appendleft(firework)
        if not explosive == 0:
            explosive_power.append(explosive)
        break

    palm, willow, crossette = make_firework(firework, explosive)
    palm_fireworks += palm
    willow_fireworks += willow
    crossette_fireworks += crossette
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        break

if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if len(firework_effects) > 0:
    print("Firework Effects left: ", end='')
    print(*firework_effects, sep=", ")

if len(explosive_power) > 0:
    print("Explosive Power left: ", end='')
    print(*explosive_power, sep=", ")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")

