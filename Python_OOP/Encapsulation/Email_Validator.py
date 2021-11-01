class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def __get_name(self, email):
        tmp_list = email.split("@")
        return tmp_list[0]

    def __get_email(self, email):
        tmp_list = email.split("@")
        tmp_list_1 = tmp_list[1].split(".")
        return tmp_list_1[0]

    def __get_domain(self, email):
        tmp_list = email.split("@")
        tmp_list_1 = tmp_list[1].split(".")
        return tmp_list_1[-1]

    def validate(self, email):
        name = self.__get_name(email)
        domain = self.__get_domain(email)
        e_mail = self.__get_email(email)
        if self.__is_name_valid(name) and self.__is_domain_valid(domain) and self.__is_mail_valid(e_mail):
            return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
