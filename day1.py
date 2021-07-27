# print('Hello World!') # You may use double/single quotes
# print('Hello World!' * 3) # What does the * 3 do?
#
# age = 16
# gpa = 3.9
# name = 'John Doe'
# bus_rider = False   # notice the naming convention

# # notice the difference between these 2 statements
# print('age')
# print(age) # age variable must already be defined

# # old way - can get unruly
# first_name = 'Jeff'
# print('My name is ' + first_name)  # the + sign concatenates strings
#
# # new (cool) way - formatted strings
# last_name = 'VanArnhem'
# print(f'My last name is {last_name}') # notice the f before quotes
#
# score = 50
# print('Score = ' + score) # this should cause an error… why?

# # fix 1 -- use built in function str(arg) to convert arg to a string
# score = 50
# print('Score = ' + str(score))
#
# # fix 2 -- formatted strings take care of this automatically
# score = 50
# print(f'Score = {score}')

# name = input('What is your name? ')
# print(f'Your name is {name}')

#
# age = input('What is your age? ')
# age = age * 7
# print('Your age in dog years is ' + age)

# age = input('What is your age? ')
# age = int(age) * 7
# print('Your age in dog years is ' + str(age))
# # this could be helpful
# print(type(age)) # type returns the type of the passed argument


# # problem
# print('Jeff's code')
#
# # solution 1
# print("Jeff's code") # mixing single/double quotes
#
# #solution 2
# print('Jeff\'s code') # use the backslash \ escape character

#
#
# print("""This
# is
# a
# multi-line
# string""")


# # Use bracket notation to grab character at a specific index
# course = 'Bulldog Python Bootcamp'
# print(course[1]) # Can you guess what this prints?


# # Use bracket notation to grab character at a specific index
# course = 'Bulldog Python Bootcamp'
# print(course[0:4]) # Can you guess what this prints?
# print(course[4:])
# print(course[:5])
# print(course[-1])

#
# course = 'Bulldog Python Bootcamp'
# print(len(course))

# # Use the dot . operator to access the methods of an object
# course = 'Bulldog Python Bootcamp'
# print(course.lower()) # creates a new string - original unchanged
# print(course)
#
# print(course.find('P'))
# print(course.find('camp'))
# print(course.find('Camp'))
#
# print(course.replace('Bulldog', 'OFHS'))
#
# # there are many more string methods

# course = 'Bulldog Python Bootcamp'
# print('Python' in course)

# # multiplication, addition, subtraction
# print(4 * 2)
# print(3 * 2.1) # my computer gave me an interesting answer. Why?
# print(8 + 3)
# print(8 + 3.0)
#
# # Let's say we want to add a value to our variable
# x_coord = 10
#
# x_coord = x_coord + 2  # adds 2 and reassigns
# x_coord += 2  # does the same thing

# all arithmetic operators have a corresponding shortcut


# #built in functions
# x, y = 2.9, -2.9  # notice this notation to define multiple variables at once
# print(round(x))
# print(abs(y))
#
# import math # by convention we usually put imports at top of file
# print(math.sqrt(16))
# print(math.floor(2.9)) # could be helpful

#
# import random
# print(random.randint(1,6)) # integers between 1 and 6
# print(random.random()) # floats between 0 and 1
# print(random.randrange(5, 100, 5)) # last argument is the step

# is_thirsty = True
#
# # reserved word if
# # followed by boolean expression (True or False)
# # followed by colon:
# # block of code to run conditionally is indented
# if is_thirsty:
#     print('Get a drink.')
#
# print('Have a good day!') # this will run regardless of is_thirsty


# my_age = 18
# # the result of each line of code below is a boolean value
# print(my_age == 18)  # True
# print(my_age > 21) # False
# print(my_age != 16)  # True

# num = 100
# if num % 2 == 0:
#     print("Divisible by 2")
# if num % 5 == 0:
#     print("Divisible by 5")

# num = 100
# if num % 3 == 0:
#     print("Divisible by 3")
# else:
#     print("Not divisible by 3")

# num = 100
# if num % 3 == 0:
#     print("Divisible by 3")
# elif num % 20:
#     print("Divisible by 20")
# else:
#     print("Not divisible by 3 or 20")

num = 100
if num % 2 == 0 and num > 50:
    print("Big even number")
if num % 3 == 0 or num > 50:
    print("Divisible by 3 or a bigger number")
if not num > 50:
    print("Not a big number")