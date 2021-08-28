def register(company, name):
    if name[0] not in company.keys():
        company[name[0]] = []
    if name[1] not in company[name[0]]:
        company[name[0]].append(name[1])


result = {}
command = input().split(' -> ')
while not command[0] == 'End':
    register(result, command)
    command = input().split(' -> ')
result = dict(sorted(result.items(), key=lambda x: x[0]))
for i in result.keys():
    print(i)
    print(*[f'-- {x}' for x in result[i]], sep='\n')
