#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """read file and print it to stdout"""
    with open(filename) as f:
        read_data = f.read()
        print(read_data)
