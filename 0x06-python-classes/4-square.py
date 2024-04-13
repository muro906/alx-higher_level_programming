#!/usr/bin/python3
"""This module defines a class named square with private attribute size"""


class Square:
    """Class Square with size validation"""
    def __init__(self, size=0) -> None:
        """This method acts like constructor for the class
        Args:
            size (int): The size of the square

        Raises:
            ValueError: if size <0
            TypeError: if type of size is not int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns current square area
        Returns:
            int: area of square
        """
        return self.__size ** 2

    def size(self):
        """Retrieves the value of size
        Returns:
            int: size of a square
        """
        return self.__size

    def size(self, size):
        """Setter for the size attribute
        Args:
            size(int): size of square
        Raises:
            ValueError: if size < 0
            TypeError: if size is not int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __str__(self) -> str:
        """Print str representation of object
        Returns:
            int: size of the square
        """
        return self.__size
