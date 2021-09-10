targets = list(map(lambda x: int(x), input().split()))
command = input()
while not command == 'End':
    index = int(command)
    if -len(targets) <= index < len(targets) and not targets[index] == -1:
        old_value = targets[index]
        targets[index] = -1
        for i in range(len(targets)):
            if not targets[i] == -1 and targets[i] > old_value:
                targets[i] -= old_value
            elif not targets[i] == -1 and targets[i] <= old_value:
                targets[i] += old_value
    command = input()
targets = [str(x) for x in targets]
print(f'Shot targets: {targets.count("-1")} -> {" ".join(targets)}')
