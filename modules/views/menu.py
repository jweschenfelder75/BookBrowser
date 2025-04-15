from typing import Any


class Menu:
    def print_separator(self):
        """
            Prints a horizontal line that is 100 characters long.
        """
        print("-" * 100)


    def print_menu_header(self):
        """
            Prints a menu header.
        """
        self.print_separator()
        print(f"{'Buch-Id':<8}\tTitel und Autor")
        self.print_separator()


    def print_menu_entry(self, book_id: int, title: str, author: str, /):
        """
        Prints a menu entry with the given book id, book title and book author.

        Args:
            book_id (int): book id
            title (str): book title
            author (str): book author
        """
        print(f"{book_id:<8}\t{title} (von {author})")


    def print_menu_footer(self):
        """
        Prints a menu footer.
        """
        print(f"{'(E)xit':<8}\tProgramm beenden")
        self.print_separator()


    def print_menu(self, book_list: list[dict[str, Any]], /):
        """
            Prints a menu for a given book list (with the given book id, book title and book author).
        Args:
            book_list (list[dict]): book list (with the given book id, book title and book author) to be shown in the menu
        """
        self.print_menu_header()
        if book_list:
            for book in book_list:
                book_id = book.get("Id")
                title = book.get("Title")
                author = book.get("Author")
                self.print_menu_entry(book_id, title, author)
        else:
            print(f"{'':<8}\tKein Buch gefunden!")
        self.print_menu_footer()


    def print_statistics_header(self):
        """
        Prints a statistics header.
        """
        self.print_separator()
        print("Buch Statistiken:")
        self.print_separator()


    def print_statistics_entry(self, book_statistics: dict[str, Any], /):
        """
        Prints a statistics entry for a given book statistics.

        Args:
            book_statistics (dict): book statistics
        """
        if book_statistics:
            translated_book_statistics = self.get_statistics_entry_translations(book_statistics)
            for key, value in translated_book_statistics.items():
                print(f"{key:<20}{value}")
            self.print_separator()


    def get_statistics_entry_translations(self, book_statistics: dict[str, Any], /) -> dict[str, Any]:
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
