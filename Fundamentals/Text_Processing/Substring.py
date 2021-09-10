text_to_remove = input()
text = input()
while text_to_remove in text:
    text = text.replace(text_to_remove, '')
print(text)
