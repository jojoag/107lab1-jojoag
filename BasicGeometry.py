# Lab 1: Python program to check if rectangles overlap using object oriented paradigm
# CS107, Haverford College
# <replace with your name>
# Creating a class rectangle
# https://en.wikipedia.org/wiki/Rectangle
#
# This program is intended to find whether two rectangles overlap (or intersect) each other or not.
# In the Euclidean space, a rectangle can be represented by two coordinates. Let the first co-ordinate is for the
# top-left corner and the second co-ordinated is for the bottom-right corner of the rectangle.
# A point in two dimensional Euclidean space can be represented by a pair say (x,y).
# Thus, a sample representation of a rectangle can be given as class with two member objects of another class named Point


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    # A recangle defined by two points bottom-left (bleft), and upper-right(uright)
    def __init__(self, bleft, uright):
        self.bleft = bleft
        self.uright = uright

    def doesIntersect(self, other):
        """
        First draw and check for the conditions when two rectangles can or cannot overlap with each other
        Note down the ordinated and write test suit for the same as follows
        Then add your logic to find overlap
        >>> Rect1 = Rectangle(Point(0, 0), Point(3, 3))
        >>> Rect2 = Rectangle(Point(1, 1), Point(4, 4))
        >>> Rect1.doesIntersect(Rect2)
        True
        >>> Rect1 = Rectangle(Point(1, 1), Point(3, 3))
        >>> Rect2 = Rectangle(Point(4, 4), Point(5, 5))
        >>> Rect1.doesIntersect(Rect2)
        False

        >>> Rect1 = Rectangle(Point(0, 0), Point(2, 2))
        >>> Rect2 = Rectangle(Point(-1, -1), Point(1, 1))
        >>> Rect1.doesIntersect(Rect2)
        True
        >>> Rect1 = Rectangle(Point(0, 0), Point(2, 2))
        >>> Rect2 = Rectangle(Point(1, 0), Point(3, 2))
        >>> Rect1.doesIntersect(Rect2)
        True
        >>> Rect1 = Rectangle(Point(-1, -2), Point(1, 2))
        >>> Rect2 = Rectangle(Point(-2, -1), Point(2, 1))
        >>> Rect1.doesIntersect(Rect2)
        True
        >>> Rect1 = Rectangle(Point(0, 0), Point(3, 3))
        >>> Rect2 = Rectangle(Point(1, 1), Point(2, 2))
        >>> Rect1.doesIntersect(Rect2)
        True

        >>> Rect1 = Rectangle(Point(0, 0), Point(1, 1))
        >>> Rect2 = Rectangle(Point(2, 0), Point(3, 1))
        >>> Rect1.doesIntersect(Rect2)
        False
          >>> Rect1 = Rectangle(Point(1, 1), Point(3, 3))
        >>> Rect2 = Rectangle(Point(4, 4), Point(5, 5))
        >>> Rect1.doesIntersect(Rect2)
        False
        >>> Rect1 = Rectangle(Point(0, 0), Point(2, 2))
        >>> Rect2 = Rectangle(Point(1, 3), Point(3, 10))
        >>> Rect1.doesIntersect(Rect2)
        False
        >>> Rect1 = Rectangle(Point(0, 0), Point(1, 1))
        >>> Rect2 = Rectangle(Point(-1, 2), Point(2, 4))
        >>> Rect1.doesIntersect(Rect2)
        False



        Bonus Test Cases Below
        >>> Rect2 = Rectangle(Point(-1, -2), Point(1, 2))
        >>> Rect1 = Rectangle(Point(-2, -1), Point(2, 1))
        >>> Rect1.doesIntersect(Rect2)
        True
        >>> Rect2 = Rectangle(Point(0, 0), Point(3, 3))
        >>> Rect1 = Rectangle(Point(1, 1), Point(2, 2))
        >>> Rect1.doesIntersect(Rect2)
        True
        >>> Rect1 = Rectangle(Point(-1, -2), Point(1, 2))
        >>> Rect2 = Rectangle(Point(-2, -5), Point(2, 1))
        >>> Rect1.doesIntersect(Rect2)
        True
          >>> Rect1 = Rectangle(Point("Hello", 1), Point(3, 3))
        >>> Rect2 = Rectangle(Point(4, 4), Point(5, 5))
        >>> Rect1.doesIntersect(Rect2)
        Traceback (most recent call last):
        TypeError: Self bleft's x value should be either an integer or a float
          >>> Rect1 = Rectangle(Point(1, 1), Point(0, 0))
        >>> Rect2 = Rectangle(Point(4, 4), Point(5, 5))
        >>> Rect1.doesIntersect(Rect2)
        Traceback (most recent call last):
        ValueError: Self bleft is not below or left of uright

        -----Add your test cases here similar to the above test cases
        """
        # <------- Add your logic for checking preconditions ---->
        if not (isinstance(self.bleft.x, float) or isinstance(self.bleft.x, int)):
            raise TypeError("Self bleft's x value should be either an integer or a float")
        if not (isinstance(self.bleft.y, float) or isinstance(self.bleft.y, int)):
            raise TypeError("Self bleft's y value should be either an integer or a float")
        if not (isinstance(self.uright.x, float) or isinstance(self.uright.x, int)):
            raise TypeError("Self uright's x value should be either an integer or a float")
        if not (isinstance(self.uright.y, float) or isinstance(self.uright.y, int)):
            raise TypeError("Self uright's y value should be either an integer or a float")
        if not (isinstance(other.bleft.x, float) or isinstance(other.bleft.x, int)):
            raise TypeError("Other bleft's x value should be either an integer or a float")
        if not (isinstance(other.bleft.y, float) or isinstance(other.bleft.y, int)):
            raise TypeError("Other bleft's y value should be either an integer or a float")
        if not (isinstance(other.uright.x, float) or isinstance(other.uright.x, int)):
            raise TypeError("Other uright's x value should be either an integer or a float")
        if not (isinstance(other.uright.y, float) or isinstance(other.uright.y, int)):
            raise TypeError("Other uright's y value should be either an integer or a float")
        if not (self.bleft.x < self.uright.x and self.bleft.y < self.uright.y):
            raise ValueError("Self bleft is not below or left of uright")
        if not (other.bleft.x < other.uright.x and other.bleft.y < other.uright.y):
            raise ValueError("Other bleft is not below or left of uright")

        # In this case, you will be testing the validity of the input points
        # The x and y parts of all the coordinates should be numbers (int or float)
        # The bottom-left point should be below to the upper-right point
        # If preconditions are not met, throw exceptions with appropriate message
        # To learn how to raise exceptions, I encourage you to refer to the file named UsefulCodeBase.py
        # UsefulCodeBase.py contains code that checks types, values and raises helpful exceptions
        # <------- Add your logic for overlap here ------>

        # Checks if a point in the "other" rectangle is located within the "self" rectangle, in the case the "other" rectangle is completely enclosed -- and vice versa
        if self.bleft.x <= other.bleft.x <= self.uright.x and self.uright.y >= other.bleft.y >= self.bleft.y:
            return True
        if other.bleft.x <= self.bleft.x <= other.uright.x and other.uright.y >= self.bleft.y >= other.bleft.y:
            return True
        # Checks if any of the self points are between the y coordinates of the other rectangle, then checks if the self.uright/bleft points are on opposite sides of one of other's vertical sides
        if ((other.uright.y >= self.uright.y >= other.bleft.y) or (
                other.uright.y > self.bleft.y >= other.bleft.y)) and (
                (self.uright.x >= other.uright.x >= self.bleft.x) or (self.uright.x >= other.bleft.x >= self.bleft.x)):
            return True
        # Same as above, except checks if the self points are between the x coordinates of the other rectangle, then verifies the points are on opposite sides of one of the other's horizontal sides
        if ((other.uright.x >= self.uright.x >= other.bleft.x) or (
                other.uright.x > self.bleft.x >= other.bleft.x)) and (
                (self.uright.y >= other.uright.y >= self.bleft.y) or (self.uright.y >= other.bleft.y >= self.bleft.y)):
            return True
        return False

        # Test for the post condition i.e. correctness of the output.


def test_intersect():
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    print("Trying out tests given at the beginning of this script")
    doctest.testmod()


# Program execution starts here
# I copied this from http://docs.python.org/lib/module-doctest.html
if __name__ == "__main__":
    test_intersect()
