def vowel_filter(function):
    vowels = {"a", "e", "i", "o", "u", "y"}

    def wrapper():
        return [el for el in function() if el.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
