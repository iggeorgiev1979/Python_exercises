def type_check(type_of_the_element):
    def decorator(func):
        def wrapper(element):
            if type(element) == type_of_the_element:
                return func(element)
            return "Bad Type"

        return wrapper
    return decorator

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))