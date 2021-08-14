bees = [int(x) for x in input().split()]
hornets = [int(x) for x in input().split()]
for i in range(len(bees)):
    if sum(hornets) > bees[i]:
        bees[i] = 0
    else:
        bees[i] -= sum(hornets)
        hornets.pop(0)
bees = list(filter(lambda x: x > 0, bees))
print(*bees, sep=' ') if len(bees) > 0 else print(*hornets, sep=' ')
