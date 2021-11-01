class Profile:
    def __init__(self, username: str, password: str, ):
        self.username = self.__validate_username(username)
        self.password = self.__validate_password(password)

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

    def __validate_username(self, username):
        if 5 <= len(username) <= 15:
            return username
        raise ValueError("The username must be between 5 and 15 characters.")

    def __validate_password(self, password):
        if len(password) >= 8 and self.__there_is_a_digit(password) and self.__there_is_upper_case_letter(password):
            return password
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __there_is_a_digit(self, password):
        for el in password:
            if el.isnumeric():
                return True
        return False

    def __there_is_upper_case_letter(self, password):
        for el in password:
            if el.isupper():
                return True
        return False


# profile_with_invalid_password = Profile('My_username', 'My-password')

# profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)