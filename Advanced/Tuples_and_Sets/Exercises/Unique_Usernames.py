n = int(input())
usernames = set()
for _ in range(n):
    usernames.add(input())
print(*usernames, sep='\n')