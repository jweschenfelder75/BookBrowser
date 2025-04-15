from modules.objects import Book


class Bookshelf:
    def __init__(self, /):
        self.id = id
        self.books: list[Book] = []

    def get_bookshelf(self) -> "Bookshelf":  # Type hint because it is Python
        return self

    def get_books(self) -> list[Book]:
        return self.books
