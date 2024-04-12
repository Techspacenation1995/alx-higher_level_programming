#!/usr/bin/python3

"""A class Rectangle that define a rectangle """

class Rectangle:
    """A class to represent a rectangle object.

    Attributes:
        width(int): The width of the rectangle.
        height(int): The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object.

        Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to zero.
        """
        self.width = width
        self.height = height

    @getters
    def width(self):
        """int: returns the widht if the rectangle"""
        return self.__width

    def height(self):
        """int: returns the height of the rectangle"""
        return self.__height

    @width.setters
    def width(self, value):
        """Set the width of the rectangle to a new value"""
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        if isnotinstance (self.__width, int):
            raise TypeError("width must be an integer")
        self.__width = value


