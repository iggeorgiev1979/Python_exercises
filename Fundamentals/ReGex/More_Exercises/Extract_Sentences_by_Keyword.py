import re

x = input()
pattern = r'[\.\!\?]'
text = input()
result = re.split(pattern, text)
pattern2 = rf'(.*)([^A-Za-z]{x}[^A-Za-z])(.+)'
for i in result:
    y = re.findall(pattern2, i)
    if not len(y) == 0:
        el = ''.join(y[0])
        print(el.strip())
