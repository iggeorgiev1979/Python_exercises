from project.library import Library
from project.user import User

user = User(12, 'Peter')
library = Library()
library.add_user(user)

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})

user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library)

print(user)