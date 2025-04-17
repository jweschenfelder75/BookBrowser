from modules.objects.book import Book


class Bookshelf:
    def __init__(self, shelf_id: int, /):
        self.id = shelf_id
        self.books: list[Book] = []

    @property
    def get_books(self) -> list[Book]:
        return self.books

    def append_book(self, book: Book, /):
        self.books.append(book)
