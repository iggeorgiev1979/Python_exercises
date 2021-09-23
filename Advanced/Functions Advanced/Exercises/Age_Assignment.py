def age_assignment(*args, **kwargs):
    result = {}
    for el in args:
        result[el] = kwargs[el[0]]
    return result


print(age_assignment("Peter", "George", G=26, P=19))
