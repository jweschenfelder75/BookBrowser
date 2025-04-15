class Book:
    def __init__(self, id: int, file: str, title: str, author: str, /):
        self.id = id
        self.file = file
        self.title = title
        self.author = author

    def get_book(self) -> "Book":  # Type hint because it is Python
        return self

    def get_file(self):
        return self.file