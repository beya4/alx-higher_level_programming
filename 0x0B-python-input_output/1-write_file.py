#!/usr/bin/python3
"""
Writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    """
    with open(filename, mode="w", encoding="utf-8") as m_file:
        char = m_file.write(text)
        return char
