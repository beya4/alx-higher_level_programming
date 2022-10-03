#!/usr/bin/python3
"""
new class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    new class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args and len(args) != 0:
            x = 0
            a_list = ["id", "size", "x", "y"]
            for x in range(len(args)):
                setattr(self, a_list[x], args[x])
        else:
            for key, v in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, v)

    def to_dictionary(self):
        """
        to_dictionary method
        """
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y, }
