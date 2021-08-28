def register_grade(grades: dict, student: list):
    if student[0] not in grades.keys():
        grades[student[0]] = 0
    if int(student[2]) > grades[student[0]]:
        grades[student[0]] = int(student[2])


def register_student(courses: dict, student: list):
    if student[1] not in courses.keys():
        courses[student[1]] = []
    courses[student[1]].append(1)


def ban(grades: dict, student: str):
    grades.pop(student)


students_grades = {}
students_courses = {}
command = input()
while not command == 'exam finished':
    command = command.split('-')
    if command[1] == 'banned':
        ban(students_grades, command[0])
    else:
        register_grade(students_grades, command)
        register_student(students_courses, command)
    command = input()

students_grades = dict(sorted(students_grades.items(), key=lambda x: (-x[1], x[0])))
students_courses = dict(sorted(students_courses.items(), key=lambda x: (-len(x[1]), x[0])))
print('Results:')
print(*[f'{i} | {j}' for i, j in students_grades.items()], sep='\n')
print('Submissions:')
print(*[f'{i} - {len(j)}' for i, j in students_courses.items()], sep='\n')
