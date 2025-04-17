import os
from modules.utils.inputvalidator import InputValidator
from modules.parsers import bookparser
from modules.views.menu import Menu
from modules.objects.bookshelf import Bookshelf

"""
Author:             Jana Weschenfelder
Version:            0.2
Description:        Browses a given dictionary for books and which analyzes them.
                    Project 2 of the Python Advanced course. OOP.
Display language:   German
Docent:             Ms Meyer
"""


class BookBrowser:
    def __init__(self, directory: str, /):
        """
        Constructor of the class.

        Args:
            directory (str): directory containing the books for the BookBrowser
        """
        self.__directory = directory
        self.__parser = bookparser.BookParser(self.__directory)
        self.__inpchk = InputValidator()
        self.__bookshelf = Bookshelf(0)  # So far, we have only one
        self.__menu = Menu()

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

    def browse_books(self):
        """
        Executes the BookBrowser program that browses a given dictionary for books and which analyzes them.
        """
        self.__bookshelf = self.__parser.get_books()
        self.__menu.print_menu(self.__bookshelf)
        inp_all_books = self.__inpchk.validate_yesno_with_exit_input(
                            "Möchten Sie alle Bücher analysieren (Ja/Nein/Exit)? ")
        if inp_all_books and inp_all_books in ("e", "exit"):
            return
        elif inp_all_books and inp_all_books in ("j", "ja"):
            inp_srch_regex = self.ask_for_regex()
            self.__menu.print_statistics_header()
            if inp_srch_regex and inp_srch_regex.isprintable():
                for book in self.__bookshelf.get_books:
                    book_with_stats = self.__parser.get_book_info_with_regex(book, inp_srch_regex)
                    self.__menu.print_statistics_entry(book_with_stats)
            else:
                for book in self.__bookshelf.get_books:
                    book_with_stats = self.__parser.get_book_info(book)
                    self.__menu.print_statistics_entry(book_with_stats)
        else:
            inp_sel_book = self.__inpchk.validate_yesno_with_exit_input(
                "Möchten Sie ein bestimmtes Buch analysieren (Ja/Nein/Exit)? ")
            if inp_sel_book and inp_sel_book in ("e", "exit"):
                return
            elif inp_sel_book and inp_sel_book in ("j", "ja"):
                book_count = len(self.__bookshelf.get_books)
                inp_spec_book = self.__inpchk.validate_int_with_exit_input(
                    f"Wählen Sie bitte ein Buch aus (1-{book_count}/Exit): ", 1, book_count)
                if inp_spec_book and inp_spec_book in ("e", "exit"):
                    return
                elif inp_spec_book.isnumeric() and inp_spec_book not in ("e", "exit"):
                    book = self.__bookshelf.get_books[int(inp_spec_book) - 1]
                    inp_srch_regex = self.ask_for_regex()
                    if inp_srch_regex and inp_srch_regex.isprintable():
                        book_statistics = self.__parser.get_book_info_with_regex(book, inp_srch_regex)
                    else:
                        book_statistics = self.__parser.get_book_info(book)
                    self.__menu.print_statistics_header()
                    self.__menu.print_statistics_entry(book_statistics)

    def execute(self):
        """
        Executes the BookBrowser program that browses a given dictionary for books and which analyzes them.
        Adds the possibility to restart the program.

        Returns:
            object:
        """
        shall_loop = True
        while shall_loop:
            if self.__directory and os.path.exists(self.__directory) and os.path.isdir(self.__directory):
                self.browse_books()
                inp_exit = self.__inpchk.validate_yesno_with_exit_input("Programm beenden (Ja/Nein)? ")
                if inp_exit and inp_exit in ("j", "ja"):
                    shall_loop = False
            else:
                print(f"Fehler: Ordnerpfad '{self.__directory}' konnte nicht gefunden werden!")
                shall_loop = False
