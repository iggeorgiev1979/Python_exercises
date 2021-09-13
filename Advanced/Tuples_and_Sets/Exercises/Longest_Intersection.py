def find_intersection(ranges: str):
    first_range, second_range = ranges.split('-')
    start, end = first_range.split(',')
    first_set = set()
    for el in range(int(start), int(end) + 1):
        first_set.add(el)
    start, end = second_range.split(',')
    second_set = set()
    for el in range(int(start), int(end) + 1):
        second_set.add(el)
    return first_set & second_set


n = int(input())
result = []
for _ in range(n):
    tmp = find_intersection(input())
    if len(tmp) > len(result):
        result = list(tmp)
print(f'Longest intersection is {result} with length {len(result)}')
