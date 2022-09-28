#!/usr/bin/python3
"""
add attribute method
"""


def add_attribute(obj, name, value):
    """
    add_attribute method
    raise TypeError
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
