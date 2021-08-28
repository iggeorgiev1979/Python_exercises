def register(side, name):
    exists = False
    if name[0] not in side.keys():
        side[name[0]] = []
    for i in side.keys():
        if name[1] in side[i]:
            exists = True
    if not exists:
        side[name[0]].append(name[1])


def change(side, name):
    exists = False
    if name[0] not in side.keys():
        side[name[0]] = []
    for i in side.keys():
        if name[1] in side[i] and not i == name[0]:
            side[i].remove(name[1])
            side[name[0]].append(name[1])
            exists = True
            print(f'{name[1]} joins the {name[0]} side!')
    if not exists:
        side[name[0]].append(name[1])
        print(f'{name[1]} joins the {name[0]} side!')


force = {}
while True:
    command = input()
    if ' | ' in command:
        command = command.split(' | ')
        register(force, command)
    elif ' -> ' in command:
        command = command.split(' -> ')
        command.reverse()
        change(force, command)
    else:
        break
force = dict(sorted(force.items(), key=lambda x: (-len(x[1]), x[0])))
for i in force.keys():
    if not len(force[i]) == 0:
        print(f'Side: {i}, Members: {len(force[i])}')
        print(*[f'! {x}' for x in sorted(force[i])], sep='\n')
