words = input().lower().split()
words_dict = {}
for el in words:
    if el not in words_dict.keys() and not words.count(el) % 2 == 0:
        words_dict[el] = words.count(el)
print(*words_dict)
