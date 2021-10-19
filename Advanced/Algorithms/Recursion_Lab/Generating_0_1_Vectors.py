def generate(chain: list, index=0):
    if index == len(chain):
        print(*chain, sep='')
        return
    else:
        for el in range(2):
            chain[index] = el
            generate(chain, index + 1)


vector = [None] * 3

generate(vector)
