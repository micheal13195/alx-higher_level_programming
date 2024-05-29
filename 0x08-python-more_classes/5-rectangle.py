#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance
        Args:
            width: rectangle width
            height: rectangle height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of the width
        Returns:
            rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height
        Returns:
            rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Method that calculates the Rectangle area
            Returns: the result of the calculated perimeter
        """

        return (self.width * self.height)

    def perimeter(self):
        """
            this method calculates the perimeter of a rectangle
            Returns: the result of the calculated perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """
            this method returns a rectangle build with width and
            height consisting of "#"
            Return: it returns a string representation of the
            the rectangle
        """

        if self.width == 0:
            return ""
        if self.height == 0:
            return ""
        string = ""
        for k in range(self.height - 1):
            string = string + '#' * self.width + '\n'
        string = string + '#' * self.width
        return string

    def __repr__(self):
        """ Method that returns the string represantion of the instance
        Returns:
            string represenation of the object
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted
        """

        print("Bye rectangle...")
