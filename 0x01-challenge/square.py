#!/usr/bin/python3
"""This class find the area and perimeter of a square"""


class Square():
    """Class representing a square"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize the square with width and height"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """Calculate the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
