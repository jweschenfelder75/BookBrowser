from typing import Generator
from typing import Tuple
from typing import Any
import os
import re

"""
Program:        BookBrowser
Version:        0.1
Author:         Jana Weschenfelder
Description:    Browses books and analyzes them. This is a procedural and modular program. 
"""


def get_files_recursively(directory: str, /) -> Generator[str, None, None]:
    """
    Walks through a given directory path and fetches all subdirectories and files there.
    Return a list of filepaths of all TXT files on the fly via a generator (iterator).

    Args:
        directory (str): directory path which contains books

    Returns:
        Generator: yields the file paths of all TXT files on the fly via a generator (iterator)
    """
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(".txt"):
                    yield os.path.join(root, file)
    except Exception as e:
        print(f"Fehler, ein Ausnahmefehler ist aufgetreten: {e}")


def get_file_title_author_from_book(filepath: str, /) -> Tuple[str, str, str]:
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
    return filepath, title, author


def read_file_and_count_lines(filepath: str, /) -> Tuple[str, int]:
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


def get_basic_book_stats(book: dict[str, Any], content: str, line_count: int, /) -> dict[str, Any]:
    """
    Fetches, calculates and combines the book statistics for a given book, its content and line count.

    Args:
        book (dict): book (book id, book filepath, book title, book author)
        content (str): book content
        line_count (int): book line count

    Returns:
        dict: book statistics (book id, book filepath, book title, book author, book line count, book space count,
                               book word count)
    """
    return {
        "Id": book["Id"],
        "File": book["File"],
        "Title": book["Title"],
        "Author": book["Author"],
        "LineCount": line_count,
        "SpaceCount": content.count(" "),
        "WordCount": len(content.split())
    }


def get_book_info(book: dict[str, Any], /) -> dict[str, Any]:
    """
    Fetches, calculates and combines the book statistics for a given book.

    Args:
        book (dict): book (book id, book filepath, book title, book author)

    Returns:
        dict: book statistics (book id, book filepath, book title, book author, book line count, book space count,
                               book word count)
    """
    content, line_count = read_file_and_count_lines(book["File"])
    return get_basic_book_stats(book, content, line_count)


def get_book_info_with_regex(book: dict[str, Any], regex: str, /) -> dict[str, Any]:
    """
    Fetches, calculates and combines the book statistics for a given book and a given pattern.

    Args:
        book (dict): book (book id, book filepath, book title, book author)
        regex (str): pattern

    Returns:
        dict: book statistics (book id, book filepath, book title, book author, book line count, book space count,
                               book word count, book pattern count)
    """
    content, line_count = read_file_and_count_lines(book["File"])
    result = get_basic_book_stats(book, content, line_count)
    result["MatchCount"] = len(re.findall(regex, content))
    return result


def get_books(directory: str, /) -> list[dict[str, Any]]:
    """
    Generates a list of books (a book is a dictionary containing: book id, book filepath, book title, book author)

    Args:
        directory (str): directory path which contains books

    Returns:
        List: books (dictionaries) as a list
    """
    result = []
    book_id = 0
    for found_file in get_files_recursively(directory):
        book_id += 1
        file, title, author = get_file_title_author_from_book(found_file)
        result.append({
            "Id": book_id,
            "File": file,
            "Title": title,
            "Author": author
        })
    return result
