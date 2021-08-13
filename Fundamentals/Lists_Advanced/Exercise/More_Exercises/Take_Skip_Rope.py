initial_list = list(input())
digit_list = [int(x) for x in initial_list if 48 <= ord(x) <= 57]
text_list = [x for x in initial_list if not 48 <= ord(x) <= 57]
take_list = digit_list[::2]
skip_list = digit_list[1::2]
result = []
for i in range(len(take_list)):
    if take_list[i] > 0:
        result.extend(text_list[:take_list[i]])
        del text_list[:take_list[i]]
    if skip_list[i] > 0:
        del text_list[:skip_list[i]]
print(*result,sep='')
