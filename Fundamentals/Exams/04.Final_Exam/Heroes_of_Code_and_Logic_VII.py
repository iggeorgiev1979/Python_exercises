def register(log: dict, hero: list):
    log[hero[0]] = [int(hero[1]), int(hero[2])]


def cast_spell(log: dict, action: list):
    name = action[1]
    mana = int(action[2])
    spell = action[3]
    if log[name][1] - mana >= 0:
        log[name][1] -= mana
        print(f'{name} has successfully cast {spell} and now has {log[name][1]} MP!')
    else:
        print(f'{name} does not have enough MP to cast {spell}!')


def take_damage(log: dict, action: list):
    name = action[1]
    damage = int(action[2])
    attacker = action[3]
    log[name][0] -= damage
    if log[name][0] > 0:
        print(f'{name} was hit for {damage} HP by {attacker} and now has {log[name][0]} HP left!')
    else:
        print(f'{name} has been killed by {attacker}!')
        log.pop(name)


def recharge(log: dict, action: list):
    name = action[1]
    mana = int(action[2])
    if log[name][1] + mana > 200:
        mana = 200 - log[name][1]
    log[name][1] += mana
    print(f'{name} recharged for {mana} MP!')


def heal(log: dict, action: list):
    name = action[1]
    blood = int(action[2])
    if log[name][0] + blood > 100:
        blood = 100 - log[name][0]
    log[name][0] += blood
    print(f'{name} healed for {blood} HP!')


heroes = {}
for _ in range(int(input())):
    register(heroes, input().split())
command = input()
while not command == 'End':
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        cast_spell(heroes, command)
    elif command[0] == 'TakeDamage':
        take_damage(heroes, command)
    elif command[0] == 'Recharge':
        recharge(heroes, command)
    elif command[0] == 'Heal':
        heal(heroes, command)
    command = input()
[print(f"""{i}
  HP: {j[0]}
  MP: {j[1]}""") for i, j in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0]))]
