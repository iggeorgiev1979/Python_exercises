numbers_list = input().split(' ')
txt = [x for x in input()]
result = ''
for i in numbers_list:
    a = sum(int(x) for x in i)
    counter = 0
    index = 0
    if a < len(txt):
        result += txt.pop(a)
    else:
        while counter < a:
            counter += 1
            index += 1
            if index >= len(txt):
                index = 0
        result += txt.pop(index)
print(result)
