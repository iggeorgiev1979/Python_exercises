def print_comb(text, index=0):
    if index >= len(text):
        print("".join(text))

        return

    print_comb(text, index + 1)

    for i in range(index + 1, len(text)):
        text[index], text[i] = text[i], text[index]

        print_comb(text, index + 1)

        text[index], text[i] = text[i], text[index]


text_input = list(input())

print_comb(text_input)
