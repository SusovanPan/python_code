from mybanking.Customer import Customer

customer = Customer(100, "Susovan", "Pan")
print("Customer Name: " + customer.getFirstName() + " " + customer.getLastName())
# print(customer.getFirstName())
customer.deposite(20)
if customer.withdraw(0):
    print("Your current Balance is: ", customer.initBalance)
else:
    print("Insuffient Balance")
