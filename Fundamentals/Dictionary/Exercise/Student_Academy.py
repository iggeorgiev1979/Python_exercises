def grade(students, name):
    if name[0] not in students.keys():
        students[name[0]] = []
    students[name[0]].append(name[1])


n = int(input())
register = {}
for _ in range(n):
    tmp_list = [input(), float(input())]
    grade(register, tmp_list)
register = {i: sum(j) / len(j) for (i, j) in register.items()}
register = dict(sorted(register.items(), key=lambda x: -x[1]))
print(*[f'{i} -> {j:.2f}' for (i, j) in register.items() if register[i] >= 4.5], sep='\n')
