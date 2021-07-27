# try-except
try:
    age = int(input("Age: "))
except ValueError:
    age = 0
    print("Bad entry.")

print(f"Your age is {age}")