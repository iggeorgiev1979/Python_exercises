numbers = list(map(lambda x: int(x), input().split(', ')))
list_of_indices = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        list_of_indices.append(i)
print(list_of_indices)
