class Account:
    def __init__(self, initBalance):
        self.initBalance = initBalance

    def getBalance(self):
        return self.initBalance

    def deposite(self, amt):
        self.initBalance += amt
        return True

    def withdraw(self, amt):
        if amt >= self.initBalance:
            return False
        else:
            self.initBalance -= amt
            return True
