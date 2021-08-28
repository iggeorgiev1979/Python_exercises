students = {}
while True:
    command = input().split(':')
    if len(command) == 1:
        break
    if command[2] not in students.keys():
        students[command[2]] = {}
    students[command[2]].update({command[0]: command[1]})
command = command[0].split('_')
if not len(command) == 1:
    command = [' '.join(command)]
for (name, index) in students[command[0]].items():
    print(f'{name} - {index}')
