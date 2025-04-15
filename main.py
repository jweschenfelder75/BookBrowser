import sys
from modules import bookbrowser


"""
Program entry point (starts the BookBrowser).
"""
if __name__ == "__main__":
    bookbrowser.execute(sys.path[0] + "\\books")
