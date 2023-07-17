class Author:
    __name = None
    __email = None
    __gender = None

    def __init__(self, name=None, email=None, gender=None):
        if name is not None and email is not None and gender is not None:
            self.__name = name
            self.__email = email
            self.__gender = gender

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email

    def getGender(self):
        return self.__gender

    def __str__(self):
        return "Author [ name = {} email = {}  gender = {}]".format(self.__name, self.__email, self.__gender)
