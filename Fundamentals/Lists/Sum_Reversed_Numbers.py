list_of_numbers = input().split()
result = 0
for i in list_of_numbers:
    number = ''.join(reversed([x for x in i]))
    result += int(number)
print(result)
