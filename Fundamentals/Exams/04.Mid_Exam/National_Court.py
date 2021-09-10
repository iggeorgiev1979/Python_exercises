from math import ceil

total_employee = int(input()) + int(input()) + int(input())
total_people = int(input())
hours = 0
counter = 0
# hours = total_people / total_employee
# if hours > 3:
#     hours += hours // 3
# print(f'Time needed: {ceil(hours)}h.')
while total_people > 0:
    total_people -= total_employee
    counter += 1
    hours += 1
    if counter == 3 and not total_people == 0:
        hours += 1
        counter = 0
print(f'Time needed: {ceil(hours)}h.')

