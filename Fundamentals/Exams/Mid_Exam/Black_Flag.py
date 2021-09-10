days = int(input())
daily_plunder = int(input())
target_plunder = float(input())
plunder = 0
for i in range(1, days + 1):
    plunder += daily_plunder
    if i % 3 == 0:
        plunder += daily_plunder * 0.5
    if i % 5 == 0:
        plunder *= 0.7
print(f'Ahoy! {plunder:.2f} plunder gained.') if plunder >= target_plunder else print(f'Collected only {plunder * 100 / target_plunder:.2f}% of the plunder.')
