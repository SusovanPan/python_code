from essentialClass.Customer import Customer


class Invoice:
    __id: int
    __customer: Customer = Customer()
    __amount: float

    def __init__(self, id, customer, amount):
        self.__id = id
        self.__customer = customer
        self.__amount = amount

    def getID(self):
        return self.__id

    def getCustomer(self):
        return self.__customer

    def setCustomer(self, customer):
        self.__customer = customer

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount

    def getCustomerID(self):
        return self.__customer.getID()

    def getCustomerName(self):
        return self.__customer.getName()

    def getCustomerDiscount(self):
        return self.__customer.getDiscount()

    def getAmountAfterDiscount(self):
        self.__amount = self.__amount - self.getCustomerDiscount()
        return self.__amount

    def __str__(self):
        return "Invoice[id={},customer={}({})({}%),amount={}]".format(self.__id, self.getCustomerName(),
                                                                      self.getCustomerID(), self.getCustomerDiscount(),
                                                                      self.getAmountAfterDiscount())
