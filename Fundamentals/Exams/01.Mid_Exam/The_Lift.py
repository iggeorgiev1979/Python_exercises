people = int(input())
lift = list(map(lambda x: int(x), input().split()))
people = abs(people)

for i in range(len(lift)):

    if lift[i] + people >= 4:
        people_in = 4 - lift[i]
        lift[i] += people_in
        people -= people_in
    else:
        lift[i] += people
        people = 0

if lift == [4] * len(lift) and people == 0:
    print(*lift, sep=' ')
elif lift == [4] * len(lift) and people > 0:
    print(f'There isn\'t enough space! {people} people in a queue!')
    print(*lift, sep=' ')
else:
    print('The lift has empty spots!')
    print(*lift, sep=' ')
