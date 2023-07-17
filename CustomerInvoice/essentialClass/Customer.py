class Customer:
    __id :int
    __name = None
    __discount :float

    def __init__(self, id=None, name=None, discount=None):
        if id is not None and name is not None and discount is not None:
            self.__id = id
            self.__name = name
            self.__discount = discount

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDiscount(self):
        return self.__discount

    def setDiscount(self, discount):
        self.__discount = discount

    def __str__(self):
        return "{}({})({}%)".format(self.__name, self.__id, self.__discount)
