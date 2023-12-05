#!/usr/bin/python3
"""Read file module"""
import json


def save_to_json_file(filename):
    """read file and print it to stdout"""
    with open(filename, "w") as f:
        json.load(f)
