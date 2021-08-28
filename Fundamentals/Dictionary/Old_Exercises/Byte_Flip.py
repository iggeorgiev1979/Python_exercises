my_str = [x for x in input().split() if len(x) == 2]
my_str = [x[::-1] for x in reversed(my_str)]
my_str = [chr(int(x, 16)) for x in my_str]
print(''.join(my_str))
