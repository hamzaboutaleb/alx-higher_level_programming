#!/usr/bin/python3
"""Write to file"""


def write_file(filename="", text=""):
    """write to file
        Args:
            filename: filename
            text: text to write
    """
    with open(filename, "w") as f:
        return f.write(text)
