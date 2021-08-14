numbers = input().split()
n = int(input())
for _ in range(n):
    tmp_list = input().split()
    for i in tmp_list:
        if i in numbers:
            for _ in range(numbers.count(i)):
                numbers.remove(i)
        else:
            numbers.append(i)
print(*sorted(numbers), sep=' ')
