def generate_row(r: int, c: int):
    chr_code = ord('a') + r
    return [f'{chr(chr_code)}{chr(chr_code + el)}{chr(chr_code)}' for el in range(c)]


row, column = input().split()

for i in range(int(row)):
    print(*generate_row(i, int(column)), sep=' ')
