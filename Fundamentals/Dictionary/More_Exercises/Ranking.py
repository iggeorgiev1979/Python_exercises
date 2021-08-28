def register(cont: dict, students: dict, participant: list):
    if participant[0] in cont.keys() and participant[1] in cont.values():
        if participant[2] not in students.keys():
            students[participant[2]] = {}
        if participant[0] not in students[participant[2]]:
            students[participant[2]][participant[0]] = 0
        if int(participant[3]) > students[participant[2]][participant[0]]:
            students[participant[2]][participant[0]] = int(participant[3])


def best_candidate(participants: dict):
    name = ''
    points = 0
    for i in participants.keys():
        tmp_points = 0
        for result in participants[i].values():
            tmp_points += result
        if tmp_points > points:
            points = tmp_points
            name = i
    print(f'Best candidate is {name} with total {points} points.')


contests = {}
command = input().split(':')
while not command[0] == 'end of contests':
    contests[command[0]] = command[1]
    command = input().split(':')
users = {}
command = input().split('=>')
while not command[0] == 'end of submissions':
    register(contests, users, command)
    command = input().split('=>')

best_candidate(users)
users = dict(sorted(users.items(), key=lambda x: x[0]))
print('Ranking:')
for name in users.keys():
    print(name)
    users[name] = dict(sorted(users[name].items(), key=lambda x: -x[1]))
    print(*[f'#  {course} -> {grade}' for course, grade in users[name].items()], sep='\n')
