import math
from abc import ABC, abstractmethod

from Vector import MyVector


class MyFigure(ABC):
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def square(self):
        pass


class MyRectangle(MyFigure):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        if w > 0:
            self._width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        if h > 0:
            self._height = h
        else:
            raise ValueError

    def type(self):
        return "Rectangle"

    def square(self):
        return self._width * self._height


class MyTriangle(MyFigure):
    def __init__(self, vec1: MyVector, vec2: MyVector):
        self._vector_1 = vec1
        self._vector_2 = vec2

    @property
    def vector1(self):
        return self._vector_1

    @vector1.setter
    def vector1(self, vec1):
        self._vector_1 = vec1

    @property
    def vector2(self):
        return self._vector_2

    @vector2.setter
    def vector2(self, vec2):
        self._vector_2 = vec2

    def type(self):
        return "Triangle"

    def square(self):
        return math.fabs(self._vector_1.x * self._vector_2.y - self._vector_1.y * self._vector_2.x) / 2


class MyCircle(MyFigure):
    def __init__(self, r):
        self._radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r

    def type(self):
        return "Circle"

    def square(self):
        return math.pi * (self._radius**2)
