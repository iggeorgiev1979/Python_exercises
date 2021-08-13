population_list = list(map(lambda x: int(x), input().split(', ')))
min_wealth = int(input())
for i in range(len(population_list)):
    for _ in range(len(population_list) - 1):
        max_wealth = max(population_list)
        for j in range(len(population_list)):
            if population_list[j] == max_wealth:
                index = j
                break
        if population_list[i] < min_wealth:
            points_needed = min_wealth - population_list[i]
            if population_list[index] - points_needed >= min_wealth:
                population_list[i] += points_needed
                population_list[index] -= points_needed
            else:
                points = population_list[index] - min_wealth
                population_list[i] += points
                population_list[index] -= points

tmp_list = list(filter(lambda x: x >= min_wealth, population_list))
if len(tmp_list) == len(population_list):
    print(population_list)
else:
    print('No equal distribution possible')