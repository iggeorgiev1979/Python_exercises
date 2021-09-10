biscuits_per_day = int(input())
workers = int(input())
other = int(input())
biscuits = 0
for i in range(1, 31):
    if i % 3 == 0:
        x = biscuits_per_day * 0.75
    else:
        x = biscuits_per_day
    biscuits += (workers * x) // 1

print(f'You have produced {int(biscuits)} biscuits for the past month.')
print(f'You produce {(biscuits - other) / other * 100:.2f} percent more biscuits.') if biscuits > other else print(f'You produce {(other - biscuits) / other * 100:.2f} percent less biscuits.')