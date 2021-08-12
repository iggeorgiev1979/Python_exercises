txt = input().split(' ')
n = int(input())
my_list = []
for i in txt:
    my_list.append(int(i))
for i in range(n):
    my_list.remove(min(my_list))
print(*my_list, sep=', ')
