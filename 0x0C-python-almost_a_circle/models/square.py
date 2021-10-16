#!/usr/bin/python3
"""In this module it create a Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a Class Square that inherits from Class Rectangle
        Args:
            Rectangle (Class): This is a Parent Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """This is a method initializer
        Args:
            size (int): width/height of the square
            x (int, optional): position x of the square. Defaults to 0.
            y (int, optional): position y of the square. Defaults to 0.
            id ([type], optional): id of the square . Defaults to None.
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter method to size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method to size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the argument of Square"""
        list_attr = ["id", "size", "x", "y"]
        if args is not None and args is not ():
            for index, var in enumerate(args):
                if index == 0:
                    self.id = var
                if index == 1:
                    self.size = var
                if index == 2:
                    self.x = var
                if index == 3:
                    self.y = var
        """ key and value for dictionary attributes"""
        if kwargs is not None and kwargs is not ():
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        # change this method for something escalable
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
