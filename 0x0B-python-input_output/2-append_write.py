#!/usr/bin/python3
"""Read file module"""


def write_file(filename="", text=""):
    """read file and print it to stdout"""
    with open(filename, "a") as f:
        return f.write(text)
