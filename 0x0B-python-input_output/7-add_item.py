#!/usr/bin/python3
"""
A module that works with JSON
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    jslist = []
    if len(sys.argv) == 1:
        try:
            l_json = load_from_json_file('add_item.json')
            jslist += l_json
        except Exception:
            pass
        save_to_json_file(jslist, 'add_item.json')
    elif len(sys.argv) > 1:
        try:
            l_json = load_from_json_file('add_item.json')
            jslist += l_json
        except Exception:
            pass
        for i in range(1, len(sys.argv)):
            jslist.append(sys.argv[i])
        save_to_json_file(jslist, 'add_item.json')
