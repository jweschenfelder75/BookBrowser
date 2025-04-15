from typing import Any


def print_separator():
    """
        Prints a horizontal line that is 100 characters long.
    """
    print("-" * 100)


def print_menu_header():
    """
        Prints a menu header.
    """
    print_separator()
    print(f"{'Buch-Id':<8}\tTitel und Autor")
    print_separator()


def print_menu_entry(book_id: int, title: str, author: str, /):
    """
    Prints a menu entry with the given book id, book title and book author.

    Args:
        book_id (int): book id
        title (str): book title
        author (str): book author
    """
    print(f"{book_id:<8}\t{title} (von {author})")


def print_menu_footer():
    """
    Prints a menu footer.
    """
    print(f"{'(E)xit':<8}\tProgramm beenden")
    print_separator()


def print_menu(book_list: list[dict[str, Any]], /):
    """
        Prints a menu for a given book list (with the given book id, book title and book author).
    Args:
        book_list (list[dict]): book list (with the given book id, book title and book author) to be shown in the menu
    """
    print_menu_header()
    if book_list:
        for book in book_list:
            book_id = book.get("Id")
            title = book.get("Title")
            author = book.get("Author")
            print_menu_entry(book_id, title, author)
    else:
        print(f"{'':<8}\tKein Buch gefunden!")
    print_menu_footer()


def print_statistics_header():
    """
    Prints a statistics header.
    """
    print_separator()
    print("Buch Statistiken:")
    print_separator()


def print_statistics_entry(book_statistics: dict[str, Any], /):
    """
    Prints a statistics entry for a given book statistics.

    Args:
        book_statistics (dict): book statistics
    """
    if book_statistics:
        translated_book_statistics = get_statistics_entry_translations(book_statistics)
        for key, value in translated_book_statistics.items():
            print(f"{key:<20}{value}")
        print_separator()


def get_statistics_entry_translations(book_statistics: dict[str, Any], /) -> dict[str, Any]:
    """
    Retrieves the German translation for a given book statistics.

    Args:
        book_statistics (dict): book statistics

    Returns:
        dict: translated keys of the book statistics dictionary
    """
    new_keys = {"Id": "Buch-Id", "File": "Datei", "Title": "Titel", "Author": "Autor", "LineCount": "Anzahl Zeilen",
                "SpaceCount": "Anzahl Leerzeichen", "WordCount": "Anzahl Wörter", "MatchCount": "Anzahl Pattern"}
    translated_book_statistics = {new_keys.get(k, k): v for k, v in book_statistics.items()}
    return translated_book_statistics
