def manipulate(text: str):
    number = int(text[1:-1])
    if text[0].isupper():
        number /= ord(text[0]) - 64
    else:
        number *= ord(text[0]) - 96
    if text[-1].isupper():
        number -= ord(text[-1]) - 64
    else:
        number += ord(text[-1]) - 96
    return number


result = input().split()
for i in range(len(result)):
    result[i] = manipulate(result[i])
print(f'{sum(result):.2f}')
