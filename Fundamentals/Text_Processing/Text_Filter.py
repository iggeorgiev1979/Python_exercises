words = input().split(', ')
text = input()
while len(words) > 0:
    text = text.replace(words[-1], '*' * len((words[-1])))
    if text.count(words[-1]) == 0:
        words.pop()
print(text)
