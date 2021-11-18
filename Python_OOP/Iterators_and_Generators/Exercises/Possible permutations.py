def all_permutations(symbols: list, index=0, result=[], used=[], final_result=[]):
    if not result:
        result = [None] * len(symbols)
    if not used:
        used = [False] * len(symbols)
    if index == len(symbols):
        final_result.append(result.copy())
        return

    for i in range(len(symbols)):
        if not used[i]:
            result[index] = symbols[i]
            used[i] = True
            all_permutations(symbols, index + 1, result, used)
            used[i] = False
    return final_result

def possible_permutations(seq):
    permutations = all_permutations(seq)
    for perm in permutations:
        yield perm


[print(n) for n in possible_permutations([1, 2, 3])]
