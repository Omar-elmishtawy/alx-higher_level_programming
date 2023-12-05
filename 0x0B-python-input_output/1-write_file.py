#!/usr/bin/python3
"""Read file module"""


def write_file(filename="", text=""):
    """read file and print it to stdout"""
    with open(filename, "w") as f:
        return f.write(text)
