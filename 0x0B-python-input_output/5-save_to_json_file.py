#!/usr/bin/python3
""" write obj tp text file"""

import json


def save_to_json_file(my_obj, filename):
    """save to file json
        Args:
            my_obj: object
            filename: file nmae
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
