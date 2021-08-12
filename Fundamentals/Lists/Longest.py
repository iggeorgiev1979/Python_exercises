def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)
    P = [None] * len(seq)

    L = 1
    M[0] = 0

    for i in range(1, len(seq)):
        lower = 0
        upper = L

        if seq[M[upper - 1]] < seq[i]:
            j = upper

        else:
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid - 1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower

        P[i] = M[j - 1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    r = []
    pos = M[L - 1]
    for _ in range(L):
        r.append(seq[pos])
        pos = P[pos]

    return r[::-1]


seq = [int(x) for x in input().split()]
print(subsequence(seq))
