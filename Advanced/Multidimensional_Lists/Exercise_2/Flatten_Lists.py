numbers = input().split('|')

for el in reversed(numbers):
    tmp_list = el.split()
    tmp_string = " ".join(tmp_list)
    if tmp_string:
        print(tmp_string, end=' ')
