def sum_ascii_value(name: str):
    result = 0
    for ch in name:
        result += ord(ch)
    return result


odd_set = set()
even_set = set()

n = int(input())

for i in range(n):
    tmp = sum_ascii_value(input()) // (i + 1)
    if tmp % 2 == 0:
        even_set.add(tmp)
    else:
        odd_set.add(tmp)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    print(*odd_set | even_set, sep=', ')
elif sum_odd > sum_even:
    print(*odd_set - even_set, sep=', ')
else:
    print(*odd_set ^ even_set, sep=', ')
