x = ord(input())
y = ord(input())
result = 0
for el in input():
    if x < ord(el) < y:
        result += ord(el)
print(result)
