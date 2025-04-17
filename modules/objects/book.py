from modules.objects.book_statistics import BookStatistics

"""
Represents a book that might contain book statistics.
"""


class Book:
    def __init__(self, book_id: int, file: str, title: str, author: str, /):
        """
        Constructor of the class.

        Args:
            book_id (int): id of the book
            file (str): filepath of the book
            title (str): title of the book
            author (str): author of the book
        """
        self.id = book_id
        self.file = file
        self.title = title
        self.author = author
        self.statistics = None

    @property
    def has_statistics(self) -> bool:
        """
        Checks if the book has some BookStatistics attached (if it is not None)

        Returns:
            bool: True if the book has some BookStatistics attached, otherwise False
        """
        return self.statistics is not None

    @property
    def get_statistics(self) -> "BookStatistics":  # Type hint because it is Python
        """
        Returns the statistics of the book

        Returns:
            BookStatistics: statistics of the book or None
        """
        return self.statistics

    def set_statistics(self, statistics: BookStatistics, /):
        """
        Attaches the given statistics to the book.

        Args:
            statistics (BookStatistics): book statistics
        """
        self.statistics = statistics
