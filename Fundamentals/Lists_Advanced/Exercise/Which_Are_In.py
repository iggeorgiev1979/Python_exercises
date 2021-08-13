sequence_1 = input().split(', ')
sequence_2 = input().split(', ')
result = []
for i in sequence_1:
    for j in sequence_2:
        if i in j:
            result.append(i)
            break
print(result)