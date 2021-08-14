pokemons = [int(x) for x in input().split()]
result = 0
while not len(pokemons) == 0:
    index = int(input())
    if index < 0:
        element = pokemons.pop(0)
        result += element
        pokemons.insert(0, pokemons[len(pokemons) - 1])
        for i in range(len(pokemons)):
            if pokemons[i] <= element:
                pokemons[i] += element
            else:
                pokemons[i] -= element
    elif index > len(pokemons) - 1:
        element = pokemons.pop(-1)
        result += element
        pokemons.append(pokemons[0])
        for i in range(len(pokemons)):
            if pokemons[i] <= element:
                pokemons[i] += element
            else:
                pokemons[i] -= element
    else:
        element = pokemons.pop(index)
        result += element
        for i in range(len(pokemons)):
            if pokemons[i] <= element:
                pokemons[i] += element
            else:
                pokemons[i] -= element
print(result)
