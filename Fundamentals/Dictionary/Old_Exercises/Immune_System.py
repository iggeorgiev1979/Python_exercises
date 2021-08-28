def virus_strength(virus: str):
    return sum([ord(x) for x in virus]) // 3


def time_defeat(strength: int, virus: str):
    if virus not in log_viruses:
        return strength * len(virus)
    return strength * len(virus) // 3


def register(log: list, virus: str):
    if virus not in log:
        log.append(virus)


log_viruses = []
immune_strength = int(input())
virus_name = input()
health = immune_strength
while not virus_name == 'end':
    x = virus_strength(virus_name)
    y = time_defeat(x, virus_name)
    register(log_viruses, virus_name)
    health -= y
    if health >= 0:
        print(f'Virus {virus_name}: {x} => {y} seconds')
        print(f'{virus_name} defeated in {y // 60}m {y % 60}s.')
        print(f'Remaining health: {health}')
        health += int(health * 0.2)
        if health > immune_strength:
            health = immune_strength
    else:
        print(f'Virus {virus_name}: {x} => {y} seconds')
        print('Immune System Defeated.')
        exit()
    virus_name = input()
print(f'Final Health: {int(health)}')
