students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())
attendances = [int(input()) for _ in range(students_count)]
if lectures_count > 0:
    print(f'Max Bonus: {round(max(attendances)/ lectures_count * (5 + initial_bonus))}.\nThe student has attended {max(attendances)} lectures.')
else:
    print(f'Max Bonus: 0.\nThe student has attended 0 lectures.')
