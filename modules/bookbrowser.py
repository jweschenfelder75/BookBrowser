import os
from modules.utils import inputvalidator as inpcheck
from modules.parsers import bookparser
from modules.views import view


"""
Author:             Jana Weschenfelder
Version:            0.1
Description:        Browses a given dictionary for books and which analyzes them.
                    Project 1 of the Python Advanced course.
Display language:   German
Docent:             Ms Meyer
"""


def ask_for_regex() -> str | None:
    """
    Ask if a pattern shall be analyzed, and if yes: Asks for a pattern (regex) and validates the input.

    Returns:
        str | None: either the entered pattern or None
    """
    result = None
    inp_regex = inpcheck.validate_yesno_input("Möchten Sie ein Pattern analysieren (Ja/Nein)? ")
    if inp_regex and inp_regex in ("j", "ja"):
        inp_srch_regex = inpcheck.validate_pattern_input("Geben Sie bitte ein Pattern an: ")
        result = inp_srch_regex
    return result


def browse_books(directory: str, /):
    """
    Executes the BookBrowser program that browses a given dictionary for books and which analyzes them.

    Args:
        directory (str): directory path which contains books
    """
    book_list = bookparser.get_books(directory)
    view.print_menu(book_list)
    inp_all_books = inpcheck.validate_yesno_with_exit_input("Möchten Sie alle Bücher analysieren (Ja/Nein/Exit)? ")
    if inp_all_books and inp_all_books in ("e", "exit"):
        return
    elif inp_all_books and inp_all_books in ("j", "ja"):
        inp_srch_regex = ask_for_regex()
        view.print_statistics_header()
        if inp_srch_regex and inp_srch_regex.isprintable():
            for book in book_list:
                book_statistics = bookparser.get_book_info_with_regex(book, inp_srch_regex)
                view.print_statistics_entry(book_statistics)
        else:
            for book in book_list:
                book_statistics = bookparser.get_book_info(book)
                view.print_statistics_entry(book_statistics)
    else:
        inp_sel_book = inpcheck.validate_yesno_with_exit_input(
            "Möchten Sie ein bestimmtes Buch analysieren (Ja/Nein/Exit)? ")
        if inp_sel_book and inp_sel_book in ("e", "exit"):
            return
        elif inp_sel_book and inp_sel_book in ("j", "ja"):
            book_count = len(book_list)
            inp_spec_book = inpcheck.validate_int_with_exit_input(
                f"Wählen Sie bitte ein Buch aus (1-{book_count}/Exit): ", 1, book_count)
            if inp_spec_book and inp_spec_book in ("e", "exit"):
                return
            elif inp_spec_book.isnumeric() and inp_spec_book not in ("e", "exit"):
                book = book_list[int(inp_spec_book) - 1]
                inp_srch_regex = ask_for_regex()
                if inp_srch_regex and inp_srch_regex.isprintable():
                    book_statistics = bookparser.get_book_info_with_regex(book, inp_srch_regex)
                else:
                    book_statistics = bookparser.get_book_info(book)
                view.print_statistics_header()
                view.print_statistics_entry(book_statistics)


def execute(directory: str, /):
    """
    Executes the BookBrowser program that browses a given dictionary for books and which analyzes them.
    Adds the possibility to restart the program.

    Args:
        directory (str): directory path which contains books
    """
    shall_loop = True
    while shall_loop:
        if directory and os.path.exists(directory) and os.path.isdir(directory):
            browse_books(directory)
            inp_exit = inpcheck.validate_yesno_with_exit_input("Programm beenden (Ja/Nein)? ")
            if inp_exit and inp_exit in ("j", "ja"):
                shall_loop = False
        else:
            print(f"Fehler: Ordnerpfad '{directory}' konnte nicht gefunden werden!")
            shall_loop = False
