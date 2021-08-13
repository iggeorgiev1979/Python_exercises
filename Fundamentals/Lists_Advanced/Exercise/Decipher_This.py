sequence_list = input().split()
result = []
for word in sequence_list:
    word_list = list(word)
    number_list = []
    for number in word_list:
        try:
            number_list.append(int(number))
        except:
            pass
    number_list = [str(x) for x in number_list]
    number = ''.join(number_list)
    word_list = word_list[len(number):]
    word_list.insert(0, chr(int(number)))
    word_list[1], word_list[len(word_list) - 1] = word_list[len(word_list) - 1], word_list[1]
    result.append(''.join(word_list))
print(*result, sep=' ')
