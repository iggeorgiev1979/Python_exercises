# Works only with sorted list
# Possible permutations = !len(symbols)/!len(set(symbols)) - 1

def permute(symbols: list, start_index=0, end_index=None):
    if not end_index:
        end_index = len(symbols) - 1
    print(*symbols, sep=", ")
    for left in range(end_index - 1, start_index - 1, -1):
        for right in range(left + 1, end_index + 1):
            if not symbols[left] == symbols[right]:
                symbols[left], symbols[right] = symbols[right], symbols[left]
                permute(symbols, left + 1, end_index)
        element = symbols[left]
        for index in range(left, end_index):
            symbols[index] = symbols[index + 1]
        symbols[end_index] = element


permute(["A", "B", "B"])
