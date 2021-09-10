text = input()
result = ['', '', '']
for i in text:
    if i.isnumeric():
        result[0] += i
    elif i.isalpha():
        result[1] += i
    else:
        result[2] += i
print(*result, sep='\n')
