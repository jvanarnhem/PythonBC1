# Define a dictionary
# "key": value
# commas separate multiple key-value pairs
my_contact = {
    "name": "John Doe",
    "email": "jdoe@gmail.com",
    "phone": "555-555-5555",
    "age": 42
}

# Access key-value pairs
print(my_contact["name"])
print(my_contact.get("age"))

# Easily add key-value pairs
my_contact["birthday"] = "Jan 27, 1980"
print(my_contact["birthday"])