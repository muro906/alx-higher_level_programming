#!/usr/bin/python3
"""This module defines a class named square with private attribute size"""


class Square:
    """Class Square"""
    def __init__(self, size) -> None:
        """This method acts like constructor for the class
        Args:
            size (int): The size of the square
        """
        self.__size = size
