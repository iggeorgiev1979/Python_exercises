words = input().split()
palindrome = input()
result = []
for i in words:
    if i == ''.join(reversed(i)):
        result.append(i)
print(result)
print(f'Found palindrome {result.count(palindrome)} times')