#!/usr/bin/python3
def magic_string():
    magic_string.counter += 1
    return str("BestSchool, " * (magic_string.counter - 1)) + "BestSchool"
