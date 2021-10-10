from collections import deque


def assign_male(people: list):
    while len(people) > 0:
        person = people.pop()
        if person % 25 == 0 and not person == 0:
            people.pop()
        else:
            if person > 0:
                return person
    return 0


def assign_female(people: deque):
    while len(people) > 0:
        person = people.popleft()
        if person % 25 == 0 and not person == 0:
            people.popleft()
        else:
            if person > 0:
                return person
    return 0


def match_couples(man: int, woman: int):
    if man == woman:
        return 1
    else:
        male_list.append(male - 2)
        return 0


male_list = [int(element) for element in input().split()]
female_list = deque(int(element) for element in input().split())
matches = 0

while len(male_list) > 0 and len(female_list) > 0:
    male = assign_male(male_list)
    female = assign_female(female_list)
    if male == 0 or female == 0:
        if not male == 0:
            male_list.append(male)
        if not female == 0:
            female_list.appendleft(female)
        break
    matches += match_couples(male, female)

print(f"Matches: {matches}")
if len(male_list) > 0:
    print("Males left: ", end='')
    print(*reversed(male_list), sep=', ')
else:
    print("Males left: none")

if len(female_list) > 0:
    print("Females left: ", end='')
    print(*female_list, sep=', ')
else:
    print("Females left: none")
