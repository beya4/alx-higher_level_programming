#!/usr/bin/python3
"""
Class Student that defines a student
"""


class Student:
    """
    Class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Variables and instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the attribute of a object
        """
        if (isinstance(attrs, list) and
                all(isinstance(i, str) for i in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
