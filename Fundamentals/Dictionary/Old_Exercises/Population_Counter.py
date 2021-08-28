def register(town: str, country: str, population: int, log: dict, total: dict):
    if country not in log.keys():
        log[country] = {}
        total[country] = 0
    if town not in log[country].keys():
        log[country][town] = population
        total[country] += population


countries_dict = {}
total_population = {}
command = input().split('|')
while not command[0] == 'report':
    register(command[0], command[1], int(command[2]), countries_dict, total_population)
    command = input().split('|')
for i in dict(sorted(total_population.items(), key=lambda x: -x[1])).keys():
    print(f'{i} (total population: {total_population[i]})')
    [print(f'=>{x}: {y}') for x, y in sorted(countries_dict[i].items(), key=lambda el: -el[1])]
