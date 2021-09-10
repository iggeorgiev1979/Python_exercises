def magic(strings: str):
    strings = strings.split()
    if len(strings[0]) <= len(strings[1]):
        key_str = strings[0]
        value_str = strings[1]
    else:
        key_str = strings[1]
        value_str = strings[0]
    compare_dict = {}
    for el in range(len(key_str)):
        key = key_str[el]
        value = value_str[el]
        if key not in compare_dict.keys():
            if value not in compare_dict.values():
                compare_dict[key] = value
            else:
                return False
        else:
            if compare_dict[key] == value:
                pass
            else:
                return False
    value_str = value_str[len(key_str):]
    for el in value_str:
        if el not in compare_dict.values():
            return False
    return True


text = input()
result = magic(text)
print(str(result).lower())
