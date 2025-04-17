from typing import Generator
from typing import Tuple
import os
import re
from modules.objects.bookshelf import Bookshelf
from modules.objects.book import Book
from modules.objects.book import BookStatistics


class BookParser:
    def __init__(self, directory: str, /):
        self.__directory = directory

    def get_files_recursively(self) -> Generator[str, None, None]:
        """
        Walks through a given directory path and fetches all subdirectories and files there.
        Return a list of filepaths of all TXT files on the fly via a generator (iterator).

        Args:
            directory (str): directory path which contains books

        Returns:
            Generator: yields the file paths of all TXT files on the fly via a generator (iterator)
        """
        try:
            for root, dirs, files in os.walk(self.__directory):
                for file in files:
                    if file.lower().endswith(".txt"):
                        yield os.path.join(root, file)
        except Exception as e:
            print(f"Fehler, ein Ausnahmefehler ist aufgetreten: {e}")


    def get_file_title_author_from_book(self, book_id: int, filepath: str, /) -> Book:
        """
        Fetches the title and author (sometimes translator) from a book.

        Args:
            filepath (str): file path of the book

        Returns:
            Tuple: book (book filepath, book title, book author)
        """
        title = None
        author = None
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip().startswith("Title:"):
                        title = line.split("Title:")[1].strip()
                    elif line.strip().startswith("Author:"):
                        author = line.split("Author:")[1].strip()
                    elif line.strip().startswith("Translator:"):
                        author = line.split("Translator:")[1].strip()
        except FileNotFoundError:
            print(f"Fehler: Die Datei '{filepath}' konnte nicht gelesen werden.")
        return Book(book_id, filepath, title, author)


    def read_file_and_count_lines(self, filepath: str, /) -> Tuple[str, int]:
        """
        Reads the number of lines and the content of a given book file.

        Args:
            filepath (str): file path of the book

        Returns:
            Tuple: book filepath and book line count.
        """
        line_count = 0
        content = None
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                line_count = sum(1 for line in file)
                file.seek(0)
                content = file.read()
        except FileNotFoundError:
            print(f"Fehler: Die Datei '{filepath}' konnte nicht geöffnet werden.")
        return content, line_count


    def get_basic_book_stats(self, content: str, line_count: int, /) -> BookStatistics:
        """
        Fetches, calculates and combines the book statistics for a given book, its content and line count.

        Args:
            content (str): book content
            line_count (int): book line count

        Returns:
            dict: book statistics (book id, book filepath, book title, book author, book line count, book space count,
                                   book word count)
        """
        return BookStatistics(0, line_count, content.count(" "), len(content.split()))


    def get_book_info(self, book: Book, /) -> Book:
        """
        Fetches, calculates and combines the book statistics for a given book.

        Args:
            book (dict): book (book id, book filepath, book title, book author)

        Returns:
            dict: book statistics (book id, book filepath, book title, book author, book line count, book space count,
                                   book word count)
        """
        content, line_count = self.read_file_and_count_lines(book.file)
        stats = self.get_basic_book_stats(content, line_count)
        book.attach_statistics(stats)
        return book


    def get_book_info_with_regex(self, book: Book, regex: str, /) -> Book:
        """
        Fetches, calculates and combines the book statistics for a given book and a given pattern.

        Args:
            book (dict): book (book id, book filepath, book title, book author)
            regex (str): pattern

        Returns:
            dict: book statistics (book id, book filepath, book title, book author, book line count, book space count,
                                   book word count, book pattern count)
        """
        content, line_count = self.read_file_and_count_lines(book.file)
        stats = self.get_basic_book_stats(content, line_count)
        stats.pattern_count = len(re.findall(regex, content))
        book.attach_statistics(stats)
        return book


    def get_books(self) -> "Bookshelf":
        """
        Generates a list of books (a book is a dictionary containing: book id, book filepath, book title, book author)

        Args:
            directory (str): directory path which contains books

        Returns:
            List: books (dictionaries) as a list
        """
        result = Bookshelf(0)
        book_id = 0
        for found_file in self.get_files_recursively():
            book_id += 1
            book = self.get_file_title_author_from_book(book_id, found_file)
            result.attach_book(book)
        return result
