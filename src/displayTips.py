import re

from util import displayTip

# displayTip(location = "", problem = "", description = "", fix = "")
def findWarnings(code, location):
    if not re.search(r"print\(.*\\n.*\)", code) == None:
        displayTip(
            location = location,
            problem = "Use of escaped newline character in print() statement",
            description = "it can lead to worse code legibility and cross platform compatability issues.\n" +
            " e.g. Windows uses as a newline character \\r\\n while Linux and newer MacOS devices use \\n," +
            "and older MacOS devices use \\r for a newline",
            fix = "Consider using empty print() statements for newlines\n"
        )