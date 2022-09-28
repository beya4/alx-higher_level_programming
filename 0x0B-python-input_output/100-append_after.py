#!/usr/bin/python3
"""
 inserts a line of text to a file,
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    """
    text = ""
    with open(filename, encoding='utf-8') as m_file:
        for x in m_file:
            text += x
            if search_string in x:
                text += new_string

    with open(filename, mode='w', encoding='utf-8') as m_file:
        m_file.write(text)
