#!/usr/bin/python3
'''This is  a script that adds all arguments to a Python list,
   and then save them to a file
'''
import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.exists("add_item.json"):
    existing_data = load_file("add_item.json")
else:
    existing_data = []

existing_data.extend(sys.argv[1:])
save_file(existing_data, "add_item.json")
