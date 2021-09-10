def validate(user: str):
    if not 3 <= len(user) <= 16:
        return False
    for i in user:
        if not i.isalnum() and not i == '-' and not i == '_':
            return False
    return True


usernames = input().split(', ')
for el in range(len(usernames) - 1, -1, -1):
    if not validate(usernames[el]):
        usernames.pop(el)
print(*usernames, sep='\n')
