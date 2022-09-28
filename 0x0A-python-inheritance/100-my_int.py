#!/usr/bin/python3
"""
MyInt module
"""


class MyInt(int):
    """subclass MyInt from class int"""
    def __eq__(self, other):
        """Compare equal / different to other"""
        return (int(self) != int(other))

    def __ne__(self, other):
        """Compare equal / different to other"""
        return (int(self) == int(other))
