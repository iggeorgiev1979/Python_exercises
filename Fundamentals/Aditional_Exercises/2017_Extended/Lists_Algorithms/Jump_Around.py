numbers = [int(x) for x in input().split()]
index = 0
result = numbers[index]
while True:
    if index + numbers[index] < len(numbers):
        index += numbers[index]
        result += numbers[index]
    else:
        if index - numbers[index] >= 0:
            index -= numbers[index]
            result += numbers[index]
        else:
            break
print(result)
