def triangle(n: int, row: list):
    if n == 2:
        return
    triangle(n - 1, row)
    row.append([1])
    for index in range(1, n - 1):
        row[n - 1].append(row[n - 2][index] + row[n - 2][index - 1])
    row[n - 1].append(1)


n = int(input())
k = int(input())
row = [[1], [1, 1]]
triangle(n + 1, row)
print(row[n][k - 1])
