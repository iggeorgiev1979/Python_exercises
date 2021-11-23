def tags(tag):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))