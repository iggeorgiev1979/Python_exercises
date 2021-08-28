def register_student(register: dict, info: list, total_points):
    if info[1] not in register.keys():
        register[info[1]] = {}
    if info[0] not in register[info[1]].keys():
        register[info[1]][info[0]] = 0
    if int(info[2]) > register[info[1]][info[0]]:
        old_points = register[info[1]][info[0]]
        register[info[1]][info[0]] = int(info[2])
        if info[0] not in total_points.keys():
            total_points[info[0]] = 0
        else:

            total_points[info[0]] -= old_points
        total_points[info[0]] += int(info[2])


problems = {}
total_points = {}
command = input().split(' -> ')
while not command[0] == 'no more time':
    register_student(problems, command, total_points)
    command = input().split(' -> ')
for problem in problems.keys():
    print(f'{problem}: {len(problems[problem])} participants')
    position = 1
    problems[problem] = dict(sorted(problems[problem].items(), key=lambda x: (-x[1], x[0])))
    for name, grade in problems[problem].items():
        print(f'{position}. {name} <::> {grade}')
        position += 1
print('Individual standings:')
total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
position = 1
for name in total_points.keys():
    print(f'{position}. {name} -> {total_points[name]}')
    position += 1
