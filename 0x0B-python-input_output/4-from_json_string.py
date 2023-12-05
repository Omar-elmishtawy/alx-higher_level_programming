#!/usr/bin/python3
"""Read file module"""
import json


def from_json_string(my_str):
    """read file and print it to stdout"""
    return json.loads(my_str)
