numbers = [int(x) for x in input().split()]
boolean = False
for i in range(len(numbers)):
    left = numbers[:i]
    right = numbers[i + 1:]
    if sum(left) == sum(right):
        print(i)
        boolean = True
        break
if not boolean:
    print('no')
