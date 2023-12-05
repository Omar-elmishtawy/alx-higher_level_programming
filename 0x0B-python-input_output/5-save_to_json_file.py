#!/usr/bin/python3
"""Read file module"""
import json


def save_to_json_file(my_obj, filename):
    """read file and print it to stdout"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
