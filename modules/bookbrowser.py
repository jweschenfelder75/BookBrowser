import os
from modules.utils import inputvalidator as inpcheck
from modules.parsers import bookparser
from modules.views import Menu
from modules.objects.bookshelf import Bookshelf

"""
Author:             Jana Weschenfelder
Version:            0.2
Description:        Browses a given dictionary for books and which analyzes them.
                    Project 2 of the Python Advanced course. OOP.
Display language:   German
Docent:             Ms Meyer
"""

# TODO: Rework all DocStrings in all files!


class BookBrowser:
    def __init__(self):
        self.__parser = bookparser.BookParser()
        self.__inpchk = inpcheck.InputValidator()
        self.__menu = Menu()
        self.bookshelf = Bookshelf(0)

    def ask_for_regex(self) -> str | None:
        """
        Ask if a pattern shall be analyzed, and if yes: Asks for a pattern (regex) and validates the input.

        Returns:
            str | None: either the entered pattern or None
        """
        result = None
        inp_regex = self.__inpchk.validate_yesno_input("Möchten Sie ein Pattern analysieren (Ja/Nein)? ")
        if inp_regex and inp_regex in ("j", "ja"):
            inp_srch_regex = self.__inpchk.validate_pattern_input("Geben Sie bitte ein Pattern an: ")
            result = inp_srch_regex
        return result

    def browse_books(self, directory: str, /):
        """
        Executes the BookBrowser program that browses a given dictionary for books and which analyzes them.

        Args:
            directory (str): directory path which contains books
        """
        self.bookshelf = self.__parser.get_books(directory)
        self.__menu.print_menu(self.bookshelf)
        inp_all_books = self.__inpchk.validate_yesno_with_exit_input("Möchten Sie alle Bücher analysieren (Ja/Nein/Exit)? ")
        if inp_all_books and inp_all_books in ("e", "exit"):
            return
        elif inp_all_books and inp_all_books in ("j", "ja"):
            inp_srch_regex = self.ask_for_regex()
            self.__menu.print_statistics_header()
            if inp_srch_regex and inp_srch_regex.isprintable():
                for book in self.bookshelf.get_books:
                    book_statistics = self.__parser.get_book_info_with_regex(book, inp_srch_regex)
                    self.__menu.print_statistics_entry(book_statistics)
            else:
                for book in self.bookshelf.get_books:
                    book_statistics = self.__parser.get_book_info(book)
                    self.__menu.print_statistics_entry(book_statistics)
        else:
            inp_sel_book = self.__inpchk.validate_yesno_with_exit_input(
                "Möchten Sie ein bestimmtes Buch analysieren (Ja/Nein/Exit)? ")
            if inp_sel_book and inp_sel_book in ("e", "exit"):
                return
            elif inp_sel_book and inp_sel_book in ("j", "ja"):
                book_count = len(self.bookshelf.get_books)
                inp_spec_book = self.__inpchk.validate_int_with_exit_input(
                    f"Wählen Sie bitte ein Buch aus (1-{book_count}/Exit): ", 1, book_count)
                if inp_spec_book and inp_spec_book in ("e", "exit"):
                    return
                elif inp_spec_book.isnumeric() and inp_spec_book not in ("e", "exit"):
                    book = self.bookshelf.get_books[int(inp_spec_book) - 1]
                    inp_srch_regex = self.ask_for_regex()
                    if inp_srch_regex and inp_srch_regex.isprintable():
                        book_statistics = self.__parser.get_book_info_with_regex(book, inp_srch_regex)
                    else:
                        book_statistics = self.__parser.get_book_info(book)
                    self.__menu.print_statistics_header()
                    self.__menu.print_statistics_entry(book_statistics)

    def execute(self, directory: str, /):
        """
        Executes the BookBrowser program that browses a given dictionary for books and which analyzes them.
        Adds the possibility to restart the program.

        Args:
            directory (str): directory path which contains books
        """
        shall_loop = True
        while shall_loop:
            if directory and os.path.exists(directory) and os.path.isdir(directory):
                self.browse_books(directory)
                inp_exit = self.__inpchk.validate_yesno_with_exit_input("Programm beenden (Ja/Nein)? ")
                if inp_exit and inp_exit in ("j", "ja"):
                    shall_loop = False
            else:
                print(f"Fehler: Ordnerpfad '{directory}' konnte nicht gefunden werden!")
                shall_loop = False
