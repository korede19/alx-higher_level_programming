#!/usr/bin/python3
"""This is a module for a Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """This is a Class Rectangle that inherits from Class Base
    Args:
        Base (Class): This is a Parent Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a method initalizer
        Args:
            width (int): This is a value to width
            height (int): This is a value to height
            x (int, optional): This is a value to x. Defaults to 0.
            y (int, optional): This is a value to y. Defaults to 0.
            id (int, optional): This is a value to id. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method to width"""
        return self.__width

    @width.setter
    def width(self, var):
        """Setter method to width"""
        if type(var) != int:
            raise TypeError("width must be an integer")
        if var <= 0:
            raise ValueError("width must be > 0")
        self.__width = var

    @property
    def height(self):
        """Getter method to height"""
        return self.__height

    @height.setter
    def height(self, var):
        """Setter method to height"""
        if type(var) != int:
            raise TypeError("height must be an integer")
        if var <= 0:
            raise ValueError("height must be > 0")
        self.__height = var

    @property
    def x(self):
        """Getter method to x"""
        return self.__x

    @x.setter
    def x(self, var):
        """Setter method to x"""
        if type(var) != int:
            raise TypeError("x must be an integer")
        if var < 0:
            raise ValueError("x must be >= 0")
        self.__x = var

    @property
    def y(self):
        """Getter method to y"""
        return self.__y

    @y.setter
    def y(self, var):
        """Setter method to y"""
        if type(var) != int:
            raise TypeError("y must be an integer")
        if var < 0:
            raise ValueError("y must be >= 0")
        self.__y = var

    def area(self):
        """ In this method it compute the area value"""
        return self.__width * self.__height

    def display(self):
        """This method prints in stdout the Rectangle
        instance with the character #
        """
        if self.__width is 0 or self.__height is 0:
                print()
                return
        else:
            if self.__y:
                print('\n' * (self.__y - 1))
            for i in range(self.__height):
                    print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """This method returns the string representation
           of the object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update the argument of Rectangle"""
        list_attr = ["id", "widht", "height", "x", "y"]
        if args is not None and args is not ():
            for index, var in enumerate(args):
                if index == 0:
                    self.id = var
                if index == 1:
                    self.width = var
                if index == 2:
                    self.height = var
                if index == 3:
                    self.x = var
                if index == 4:
                    self.y = var
        """no-keyword argument"""
        if kwargs is not None and kwargs is not ():
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
