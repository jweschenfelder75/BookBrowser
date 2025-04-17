from modules.objects.book import Book

"""
Represents a bookshelf that can contain a list of books.
"""


class Bookshelf:
    def __init__(self, shelf_id: int, /):
        """
        Constructor of the class.

        Args:
            shelf_id (int): id of the bookshelf
        """
        self.id = shelf_id
        self.books: list[Book] = []

    @property
    def get_books(self) -> list[Book]:
        """
        Returns a list of books (Book) or an empty list.

        Returns:
            list: books (Book) or an empty list
        """
        return self.books

    def append_book(self, book: Book, /):
        """
            Appends a given book to the bookshelf (list of books).
        Args:
            book (Book): book (possibly with statistics)
        """
        self.books.append(book)
