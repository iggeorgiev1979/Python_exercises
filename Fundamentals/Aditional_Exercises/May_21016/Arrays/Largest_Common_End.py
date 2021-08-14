txt_1 = input().split()
txt_2 = input().split()
shorter_len = len(txt_1)
if shorter_len > len(txt_2):
    shorter_len = len(txt_2)
result = 0
counter = 0
for i in range(shorter_len):
    if txt_1[i] == txt_2[i]:
        counter += 1
        if counter > result:
            result = counter
    else:
        counter = 0
txt_1.reverse()
txt_2.reverse()
for i in range(shorter_len):
    if txt_1[i] == txt_2[i]:
        counter += 1
        if counter > result:
            result = counter
    else:
        counter = 0
print(result)
