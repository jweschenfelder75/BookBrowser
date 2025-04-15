from modules.objects import book


class Bookshelf:
    def __init__(self, /):
        self.id = id
        self.books: list[book.Book] = []

    def get_bookshelf(self) -> "Bookshelf":  # Type hint because it is Python
        return self

    def get_books(self) -> list[book.Book]:
        return self.books
