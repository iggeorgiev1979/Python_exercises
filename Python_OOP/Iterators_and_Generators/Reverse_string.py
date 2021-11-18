def reverse_text(text: str):
    end = 0
    start = len(text) - 1
    while start >= end:
        yield text[start]
        start -= 1


for char in reverse_text("step"):
    print(char, end='')
