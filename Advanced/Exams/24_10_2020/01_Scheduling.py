jobs = [int(el) for el in input().split(", ")]
index = int(input())
print(sum(list(filter(lambda x: x <= jobs[index], jobs))))
