import math


class Circle:
    __radius: float = None

    def __init__(self, radius=None):
        if radius is not None:
            self.__radius = radius
        else:
            self.__radius = 1.0

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def getArea(self):
        return math.pi * (self.__radius * self.__radius)

    def getCircumference(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return "Circle[radius={}]".format(self.__radius)
