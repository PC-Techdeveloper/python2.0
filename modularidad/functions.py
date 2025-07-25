""" FUNCTIONS"""
"""
A function is a named sequence of statements that performs a computation.
"""

# Function calls
# Argument of the function
# The result is also called the return value
import math
print(type(42))
print(int('32'))

# int can convert floating-point values to integers, but it doesn't
# round off, it chops off the function part
print(int(3.9999999))
print(int(-2.3))

# Float converts integers and strings to floating-point numbers
print(float(32))
print(float('3.141516'))

# strings converts its arguments to strings
print(str(32))
print(str(3.141516))

""" MATH FUNCTIONS """
# A module is a file that contains a collection of related functions
signal_power = math.pow(2, 3)
noise_power = math.pow(2, 4)
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

degrees = 46
radians = degrees / 180.0 * math.pi
print(radians)
print(decibels)
print(height)

sqrt = math.sqrt(2) / 2.0
print(sqrt)

""" ADDING NEW FUNCTIONS """
# header


def print_lyrics():
    # body
    # indented
    print("I'm a lumberjack and I'm okay")
    print("I sleep all night and I work all day")


# defining a function creates a function object
print(print_lyrics)

# we could write a function called repeat_lyrics


def repeat_lyrics():
    # Calling the new function
    print_lyrics()
    print_lyrics()


# and then call it
repeat_lyrics()

""" PARAMETERS AND ARGUMENTS """

# Parameters


def print_twice(bruce):
    print(bruce)
    print(bruce)


# Arguments
print(print_twice('Span' * 4))
print(print_twice(42))
print(print_twice(math.cos(math.pi)))

# you can also use a variable as an argument
michael = 'Eric, the half a bee'
print_twice(michael)

""" VARAIABLES AND PARAMETERS ARE LOCAL """
