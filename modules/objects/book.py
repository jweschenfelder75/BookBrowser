from modules.objects.book_statistics import BookStatistics


class Book:
    def __init__(self, book_id: int, file: str, title: str, author: str, /):
        self.id = book_id
        self.file = file
        self.title = title
        self.author = author
        self.statistics = None

    @property
    def get_book(self) -> "Book":  # Type hint because it is Python
        return self

    @property
    def get_file(self):
        return self.file

    @property
    def has_statistics(self) -> bool:
        return self.statistics is not None

    @property
    def get_statistics(self) -> "BookStatistics":  # Type hint because it is Python
        return self.statistics

    def attach_statistics(self, statistics: BookStatistics, /):
        self.statistics = statistics
