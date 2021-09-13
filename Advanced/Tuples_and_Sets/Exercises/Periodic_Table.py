n = int(input())
elements = set()
for _ in range(n):
    elements.update(el for el in input().split())

print(*elements, sep='\n')
