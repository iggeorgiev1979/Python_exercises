class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


def check_name(email: str):
    tmp = email.split("@")
    if len(tmp[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def check_for_at(email: str):
    tmp = email.split("@")
    if not len(tmp) > 1:
        raise MustContainAtSymbolError("Email must contain @")


def check_domain(email: str):
    tmp = email.split(".")[-1]
    if tmp == "com" or tmp == "bg" or tmp == "org" or tmp == "net":
        pass
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


email_str = input()

while not email_str == "End":

    check_for_at(email_str)
    check_name(email_str)
    check_domain(email_str)
    print("Email is valid")
    email_str = input()
