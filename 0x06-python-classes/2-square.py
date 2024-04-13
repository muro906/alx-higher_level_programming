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
