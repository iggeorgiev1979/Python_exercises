import re


def find_pairs(text: str):
    pattern = r'(\b[A-Za-z][\w]{2,25})(?:\s|/|\\|\(|\)|$)'
    result = re.findall(pattern, text)
    return result


def find_the_pair_sum(pairs_list: list):
    result = 0
    result_list = []
    for i in range(len(pairs_list) - 1):
        tmp_result = len(pairs_list[i]) + len(pairs_list[i + 1])
        if tmp_result > result:
            result = tmp_result
            result_list = [pairs_list[i], pairs_list[i + 1]]
    print(*result_list, sep='\n')


input_txt = input()
pairs = find_pairs(input_txt)
find_the_pair_sum(pairs)
