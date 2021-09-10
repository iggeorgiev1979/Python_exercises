text = input()
for i in range(len(text)):
    if text[i] == ':':
        print(text[i] + text[i + 1])
