import string

from Author import Author


class Book:
    __name = None
    __author = Author()
    __price = 0.0
    __qty = 0.0

    def __init__(self, name: string, author, price, qty=None):
        if qty is not None:
            self.__name = name
            self.author = author
            self.__price = price
            self.__qty = qty
        else:
            self.__name = name
            self.author = author
            self.__price = price

    def getName(self):
        return self.__name

    def getAuthor(self):
        return self.author

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getQty(self):
        return self.__qty

    def setQty(self, qty):
        self.__qty = qty

    def __str__(self):
        return "Book[name= {}, Author [ name= {}, email= {}, gender= {} ], price= {}, qty={} ]".format(self.__name,
                                                                                                       self.getAuthor().getName(),
                                                                                                       self.author.getEmail(),
                                                                                                       self.author.getGender(),
                                                                                                       self.__price,
                                                                                                       self.__qty)
