#!/usr/bin/python3
"""
Check if the object is an instance inherited from a class
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance inherited from a class
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
