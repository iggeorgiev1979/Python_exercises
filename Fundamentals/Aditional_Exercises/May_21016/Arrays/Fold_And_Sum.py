numbers = list(map(lambda x: int(x), input().split()))
center = len(numbers) // 2
start_end = center // 2
center_list = list(numbers[start_end:len(numbers) - start_end])
start_list = list(numbers[:start_end])
end_list = list(numbers[len(numbers) - start_end:])
start_list.reverse()
end_list.reverse()
start_end_list = start_list + end_list
result = []
for i in range(len(center_list)):
    sum_element = center_list[i] + start_end_list[i]
    result.append(sum_element)
print(*result, sep=' ')
