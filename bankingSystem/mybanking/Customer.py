from mybanking.Account import Account


class Customer(Account):
    def __init__(self, initBalance, fname, lname):
        Account.__init__(self, initBalance)
        self.fname = fname
        self.lname = lname

    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname

