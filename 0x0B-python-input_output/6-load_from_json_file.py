#!/usr/bin/python3
"""Read file module"""
import json


def load_from_json_file(filename):
    """read file and print it to stdout"""
    with open(filename, "r") as f:
        obj = json.load(f)
        return obj
