n = int(input())
words = {}
for _ in range(n):
    new_word = [input(), input()]
    if new_word[0] not in words.keys():
        words[new_word[0]] = []
    words[new_word[0]].append(new_word[1])
for el in words.keys():
    print(f'{el} - {", ".join(words.get(el))}')
