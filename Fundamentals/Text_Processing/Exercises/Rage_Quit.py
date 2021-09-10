text = input().upper()
tmp_str = ''
result = ''
for el in range(len(text)):
    if not text[el].isnumeric():
        tmp_str += text[el]
    else:
        n = text[el]
        if not el == len(text) -1:
            if text[el + 1].isnumeric():
                n += text[el + 1]
        if not tmp_str == '':
            tmp_str *= int(n)
            result += tmp_str
            tmp_str = ''
print(f'Unique symbols used: {len(set(result))}\n{result}')
