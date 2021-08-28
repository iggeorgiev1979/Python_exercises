def register(courses, name):
    if name[0] not in courses.keys():
        courses[name[0]] = []
    courses[name[0]].append(name[1])


result = {}
command = input().split(' : ')
while not command[0] == 'end':
    register(result, command)
    command = input().split(' : ')
result = dict(sorted(result.items(), key=lambda x: -len(x[1])))
for i in result.keys():
    print(f'{i}: {len(result[i])}')
    print(*[f'-- {x}' for x in sorted(result[i])], sep='\n')
