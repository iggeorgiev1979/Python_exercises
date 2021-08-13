employees = input()
factor = int(input())
employees_list = list(map(lambda x: int(x) * factor, employees.split()))
average_happiness = sum(employees_list) / len(employees_list)
happy_employees = list(filter(lambda x: x >= average_happiness, employees_list))
print(f'Score: {len(happy_employees)}/{len(employees_list)}. Employees are happy!') if len(happy_employees) >= len(
    employees_list) / 2 else print(f'Score: {len(happy_employees)}/{len(employees_list)}. Employees are not happy!')
