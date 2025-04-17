from modules.objects.bookshelf import Bookshelf
from modules.objects.book import Book


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

    def print_menu(self, book_list: Bookshelf, /):
        """
            Prints a menu for a given book list (with the given book id, book title and book author).
        Args:
            book_list (list[dict]): book list (with the given book id, book title and book author) to be shown in
                                    the menu
        """
        self.print_menu_header()
        if book_list:
            for book in book_list.get_books:
                book_id = book.id
                title = book.title
                author = book.author
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

    def print_statistics_entry(self, book: Book, /):
        """
        Prints a statistics entry for a given book statistics.

        Args:
            book_statistics (dict): book statistics
        """
        if book and book.has_statistics:
            stats = book.get_statistics
            print(f"{'Buch-Id':<20}{book.id}")
            print(f"{'Datei':<20}{book.file}")
            print(f"{'Titel':<20}{book.title}")
            print(f"{'Autor':<20}{book.author}")
            print(f"{'Anzahl Zeilen':<20}{stats.line_count}")
            print(f"{'Anzahl Leerzeichen':<20}{stats.space_count}")
            print(f"{'Anzahl Wörter':<20}{stats.word_count}")
            if stats.has_pattern:
                print(f"{'Anzahl Pattern':<20}{stats.pattern_count}")
            self.print_separator()
