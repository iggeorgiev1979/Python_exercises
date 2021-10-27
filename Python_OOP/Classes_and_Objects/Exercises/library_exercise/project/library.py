class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        for user in self.user_records:
            if user.user_id == user_id:
                if not user.username == new_username:
                    old_user_name = user.username
                    user.username = new_username
                    if old_user_name in self.rented_books.keys():
                        tmp_dict = self.rented_books[old_user_name].copy()
                        del self.rented_books[old_user_name]
                        self.rented_books[user.username] = tmp_dict.copy()
                    return f"Username successfully changed to: {new_username} for userid: {user_id}"
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"
