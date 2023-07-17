from Author import Author
from Book import Book

ahTeck = Author("Tan Ah Teck", "ahteck@nowhere.com", 'm');
print(ahTeck)  # Author's toString()

dummyBook = Book("Java for dummy", ahTeck, 19.95, 99)  # Test Book's Constructor
print(dummyBook)  # Test Book's toString()

# Test Getters and Setters
dummyBook.setPrice(29.95)
dummyBook.setQty(28)
print("name is: ", dummyBook.getName())
print("price is: ", dummyBook.getPrice())
print("qty is: ", dummyBook.getQty())
print("Author is: ", dummyBook.getAuthor())  # Author's toString()
print("Author's name is: ", dummyBook.getAuthor().getName())
print("Author's email is: ", dummyBook.getAuthor().getEmail())

# Use an anonymous instance of Author to construct a Book instance
anotherBook = Book("more Java", Author("Paul Tan", "paul@somewhere.com", 'm'), 29.95)
print(anotherBook)  # toString()
