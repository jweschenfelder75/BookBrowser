import sys
from modules import bookbrowser


"""
Program entry point (starts the BookBrowser).
"""
if __name__ == "__main__":
    my_bookbrowser = bookbrowser.BookBrowser(sys.path[0] + "\\books")
    my_bookbrowser.execute()
