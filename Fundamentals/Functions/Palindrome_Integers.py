numbers = input().split(', ')


def palindrome(a):
    x = a[::-1]
    if x == a:
        return True
    else:
        return False


for i in numbers:
    print(palindrome(i))