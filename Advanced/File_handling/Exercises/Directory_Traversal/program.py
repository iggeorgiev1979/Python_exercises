import os


def register_files(file: str):
    ext = file.split('.')[-1]
    if ext not in files.keys():
        files[ext] = []
    files[ext].append(file)


files = {}
for r, d, f in os.walk(os.getcwd()):
    if len(f) > 0:
        for el in f:
            register_files(el)

result = open('report.txt', 'w')
for key, value in sorted(files.items()):
    result.writelines(f'.{key}\n')
    for element in sorted(value):
        result.writelines(f'- - - {element}\n')

result.close()

