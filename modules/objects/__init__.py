import sys

sys.path.append(sys.path[0] + "\\modules\\objects")
# PyCharm fix: https://stackoverflow.com/questions/36827962/pep8-import-not-at-top-of-file-with-sys-path
from modules.objects.book import *   # noqa: E402
from modules.objects.bookshelf import *   # noqa: E402
from modules.objects.book_statistics import *   # noqa: E402
