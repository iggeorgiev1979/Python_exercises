dictionary = {'test': {1, 3}, 'test2': {2}, 'test3': {2, 3}}

if 'test2' in dictionary:
    print(list(dictionary).index('test2'))
