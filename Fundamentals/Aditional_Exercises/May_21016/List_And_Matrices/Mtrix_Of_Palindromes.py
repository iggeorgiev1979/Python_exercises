row = int(input())
place = int(input())
matrix = []
element = None
for first_last in range(ord('a'), ord('a') + row):
    row_list = []
    for middle in range(first_last, first_last + place):
        row_list.append(chr(first_last) + chr(middle) + chr(first_last))
    matrix.append(' '.join(row_list))
print(*matrix, sep='\n')
