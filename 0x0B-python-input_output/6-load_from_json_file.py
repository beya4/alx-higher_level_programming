#!/usr/bin/python3
"""
Creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename) as m_file:
        m_json = json.load(m_file)
    return m_json
