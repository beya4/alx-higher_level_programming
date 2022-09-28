#!/usr/bin/python3
"""
Print the items of a list
"""


class MyList(list):
    """
    Print the items of a list
    """
    def print_sorted(self):
        """
        prints the list sorted,
        """
        print(sorted(self))
