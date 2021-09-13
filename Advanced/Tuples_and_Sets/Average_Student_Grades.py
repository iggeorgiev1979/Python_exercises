n = int(input())
grades = {}
for _ in range(n):
    student = input().split()
    if student[0] not in grades.keys():
        grades[student[0]] = []
    grades[student[0]].append(f'{float(student[1]):.2f}')

for key, value in grades.items():
    print(f'{key} -> {" ".join(value)} (avg: {sum([float(el) for el in value]) / len(value):.2f})')
