#!/usr/bin/python3
"""add item"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    items = load_from_json_file("add_item.json")
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_items.json")
