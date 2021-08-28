log = {}
duration = {}
n = int(input())
for _ in range(n):
    command = input().split()
    if command[1] not in log.keys():
        log[command[1]] = []
        duration[command[1]] = 0
    if command[0] not in log[command[1]]:
        log[command[1]].append(command[0])
    duration[command[1]] += int(command[2])
[print(f'{i}: {duration[i]} [{", ".join(sorted(j))}]') for i, j in sorted(log.items(), key=lambda x: x[0])]
