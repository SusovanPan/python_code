class Rectangle:
    __length: float = None
    __width: float = None

    def __init__(self, length=None, width=None):
        if length is not None and width is not None:
            self.__length = length
            self.__width = width
        else:
            self.__length = 1.0
            self.__width = 1.0

    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getArea(self):
        return self.__width * self.__length

    def getPerimeter(self):
        return 2 * (self.__length + self.__width)

    def __str__(self):
        return "Rectangle [ length = {} width = {} ]".format(self.__length, self.__width)
