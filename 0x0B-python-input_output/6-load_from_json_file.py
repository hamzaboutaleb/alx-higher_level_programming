#!/usr/bin/python3
""" laod object from json"""

import json


def load_from_json_file(filename):
    """create obj from json file
        Args:
            filename: filename
        """

    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
