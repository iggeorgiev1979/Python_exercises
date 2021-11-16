class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:

    def format(self, book: Book) -> str:
        return book.content + "EFGH"


class Printer:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def get_book(self, book):
        return self.formatter.format(book)


my_book = Book("ABCD")

my_formatter = Formatter()

my_printer = Printer(my_formatter)

print(my_printer.get_book(my_book))
