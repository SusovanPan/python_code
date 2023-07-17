class myclass:
    def __init__(self):
        self.name = "Raj"
        self.age = 21

    def __str__(self):
        return "name : {} age : {}".format(self.name, self.age)


obj = myclass()
print(obj.__str__())
print(str(obj))
