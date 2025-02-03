#!/usr/bin/python3
"""This module finds the area and perimeter of a square"""


class Square:
    """Class representing a square"""

    def __init__(self, size):
        """Initialize the square with size"""
        self.size = size  # A square should have equal width and height

    def area_of_my_square(self):
        """Calculate the area of the square"""
        return self.size * self.size

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square"""
        return 4 * self.size

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":
    s = Square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
