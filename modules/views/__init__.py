import sys

sys.path.append(sys.path[0] + "\\modules\\views")
# PyCharm fix: https://stackoverflow.com/questions/36827962/pep8-import-not-at-top-of-file-with-sys-path
from modules.views.menu import *  # noqa: E402
