text = input().split()
text = sorted(text, key=lambda x: -len(x))
result = 0
for i in range(len(text[0])):
    if not i > len(text[1]) -1:
        result += ord(text[0][i]) * ord(text[1][i])
    else:
        result += ord(text[0][i])
print(result)
