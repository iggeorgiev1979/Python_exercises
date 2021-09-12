n = int(input())
pumps = []
for _ in range(n):
    pumps.append([int(el) for el in input().split()])
for index in range(len(pumps)):
    fuel_tank = 0
    i = index
    while True:
        fuel_tank += pumps[i % n][0]
        fuel_tank -= pumps[i % n][1]
        if fuel_tank < 0:
            break
        i += 1
        if i % n == index:
            print(index)
            exit()
