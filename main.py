import sys
from modules import bookbrowser


"""
Program entry point (starts the BookBrowser).
"""
if __name__ == "__main__":
    my_bookbrowser = bookbrowser.BookBrowser()
    my_bookbrowser.execute(sys.path[0] + "\\books")
