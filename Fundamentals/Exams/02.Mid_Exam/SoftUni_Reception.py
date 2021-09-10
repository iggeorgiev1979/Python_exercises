employee = int(input()) + int(input()) + int(input())
student = int(input())
hours = 0
counter = 0
while student > 0:
    student -= employee
    hours += 1
    counter += 1
    if counter % 3 == 0 and student > 0:
        hours += 1
        counter = 0
print(f'Time needed: {hours}h.')
