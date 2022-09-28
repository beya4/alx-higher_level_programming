#!/usr/bin/python3
"""
Function that reads a text file (UTF8)
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8)
    """
    with open(filename, encoding="utf-8") as m_file:
        print(m_file.read(), end="")
