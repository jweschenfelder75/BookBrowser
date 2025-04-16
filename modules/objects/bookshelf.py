from modules.objects import Book


class Bookshelf:
    def __init__(self, shelf_id: int, /):
        self.id = shelf_id
        self.books: list[Book] = []

    @property
    def get_bookshelf(self) -> "Bookshelf":  # Type hint because it is Python
        return self

    @property
    def has_books(self) -> bool:
        return len(self.books) > 0

    @property
    def get_books(self) -> list[Book]:
        return self.books

    def attach_books(self, book: Book, /):
        self.books = book
