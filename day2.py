# i = 1
# while i <= 5: # what follows while must be boolean expression
#     print(i)
#     i = i + 1 # necessary to eventually terminate loop
# print("Done")
#
# adjective = "great"
# person = "Jeff"
# print(f""" Can I do multiline formatted strings?
# That is a {adjective} question. Please ask
# {person}""")

# names = ['Jeff', 'Samantha', 'Monica', 'Brooke']
# print(names)
# print(type(names))
# print(names[0])
# names[2] = 'Isabel'  # change an item
# print(names)
#
# scores = [92, 93.5, 89, 93]
# print(scores[-1])
# print(scores[1:4])
# print(len(scores))
#
# mixed_list = ["Jeff", 52, "Brooke", 19]

# names = ['Jeff', 'Samantha', 'Monica', 'Brooke'] # iterable
# for name in names: # iterate over list, name is next element
#     print(name)

# # this is a handy loop format
# # a loop that you can run a specific number of times
# for i in range(10):
#     print(i)

# total = 0
# for num in range (5, 100, 5):
#     total += num
# print(total)

# nested loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# # defining a function
# def print_stuff():
#     print("Hello World!")
#     print("Mr. V. is awesome.")
#
#
# print("This will print first.")
# print_stuff()
# print("Program execution continues here.")

# import math
#
#
# def quadratic_formula(a, b, c):
#     x1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
#     x2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
#     print(f"x = {x1} or x = {x2}")
#
#
# quadratic_formula(1, -1, -6)

# # Default parameters -- must come after non-default parameters
# def greet_user(first_name, middle_name="John", last_name="Doe"):
#     print(f"Hello {first_name} {middle_name} {last_name}!")
#
#
# greet_user("Jeff", "Alan", "VanArnhem")
# greet_user("Jeff", "Alan")
# greet_user("Jeff")
# greet_user("Jeff", last_name="VanArnhem")

def square1(num):
    print(num * num)


def square2(num):
    return num * num


print(square1(3)) # By default functions return 'None'
print(square2(3))
