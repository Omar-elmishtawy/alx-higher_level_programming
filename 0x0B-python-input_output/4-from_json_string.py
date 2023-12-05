#!/usr/bin/python3
"""Read file module"""
import json


def from_json_String(my_str):
    """read file and print it to stdout"""
    return json.loads(my_str)
