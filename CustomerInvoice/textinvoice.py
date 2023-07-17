from essentialClass.Customer import Customer
from essentialClass.Invoice import Invoice

c1 = Customer(88, "Susovan Kumar Pan", 20)
print(c1)  # Customer's __str__()
c1.setDiscount(10)
print(c1)
print("id is: ", c1.getID())
print("name is: ", c1.getName())
print("discount is: ", c1.getDiscount())
# Test Invoice class
inv1 = Invoice(101, c1, 800)
print(inv1)

inv1.setAmount(1000)
print(inv1)
print("id is: ", inv1.getID())
print("customer is: ", inv1.getCustomer())  # Customer's __str__()
print("amount is: ", inv1.getAmount())
print("customer's id is: ", inv1.getCustomerID())
print("customer's name is: ", inv1.getCustomerName())
print("customer's discount is: ", inv1.getCustomerDiscount())
print("amount after discount is: ", inv1.getAmountAfterDiscount())
