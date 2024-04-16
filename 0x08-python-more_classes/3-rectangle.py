#!/usr/bin/python3
"""This module contains info on class Rectangle"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0) -> None:
        """Intializes the base attributes
        Args:
            width (int): width of rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Acts as setter for the width
        Args:
            value (int): New width

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height property
        Args:
            value (int): New height

        Raises:
            TypeError: Value is not an int
            ValueError: Value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height + 2 * self.__width)

    def __str__(self):
        """Print str representation of the object"""
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    print('#', end="")
                print()
