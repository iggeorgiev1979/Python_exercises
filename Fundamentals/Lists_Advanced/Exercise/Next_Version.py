version = list(map(lambda x: int(x), input().split('.')))
for i in range(len(version) - 1, -1, -1):
    if not version[i] == 9:
        version[i] += 1
        break
    else:
        version[i] = 0
print(*version, sep='.')
