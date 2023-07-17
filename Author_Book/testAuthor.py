from Author import Author

ahTeck = Author("Tan Ah Teck", "susovan.pan@gmail.com", 'm')
print(ahTeck)  # Test
ahTeck.setEmail("paulTan@nowhere.com")  # Test setter
print("name is: " + ahTeck.getName())  # Test getter
print("email is: " + ahTeck.getEmail())  # Test getter
print("gender is: " + ahTeck.getGender())
