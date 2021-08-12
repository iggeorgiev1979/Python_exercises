initial_list = [int(x) for x in input().split(' ')]
n = int(input())
len_list = len(initial_list)
result_list = []
index_counter = 0
n_counter = 0
while len(result_list) < len_list:
    n_counter += 1
    if n_counter % n == 0:
        result_list.append(initial_list.pop(index_counter))
    else:
        index_counter += 1
    if index_counter >= len(initial_list):
        index_counter = 0
print(str(result_list).replace(' ', ''))
