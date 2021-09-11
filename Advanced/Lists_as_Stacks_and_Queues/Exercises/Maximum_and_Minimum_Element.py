n = int(input())
numbers = []
for _ in range(n):
    command = input().split()
    if command[0] == '1':
        numbers.append(int(command[1]))
    elif command[0] == '2':
        if len(numbers) > 0:
            numbers.pop()
    elif command[0] == '3' and len(numbers) > 0:
        print(max(numbers))
    elif command[0] == '4' and len(numbers) > 0:
        print(min(numbers))

print(", ".join(reversed([str(el) for el in numbers])))
