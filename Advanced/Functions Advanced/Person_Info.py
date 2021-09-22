def get_info(**arg):
    return f'This is {arg["name"]} from {arg["town"]} and he is {arg["age"]} years old'


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))