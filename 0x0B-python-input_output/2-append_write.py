#!/usr/bin/python3
"""file append module"""

def append_write(filename="", text=""):
    """append to file
        Args:
            filename: filne name
            text: text to append
     """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
