clothes = [int(el) for el in input().split()]
capacity = int(input())
rack = 0
counter = 0
for index in range(len(clothes) - 1, -1, -1):
    if rack + clothes[index] <= capacity:
        rack += clothes[index]
    else:
        rack = clothes[index]
        counter += 1
print(counter + 1)
