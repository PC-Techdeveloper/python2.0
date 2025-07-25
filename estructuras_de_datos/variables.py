""" A variable is a name that refers to a value. To create a varaible, we can't write a assignment statement like this. """
# from diagram import diagram, adjust
# from diagram import make_binding, Frame
# import math

n = 17

pi = 3.141664565464

message = "And now for something completely different"
print(message)

# You can also use a variable as part of an expression
# with arithmetic operators
print(n + 25)
print(2 * pi)

# And you can use a variable when you call a function
print(round(pi))
print(len(message))

# STATE DIAGRAMS

# bindingOne = make_binding('message', 'And now for something completely different')
# bindingSecond = make_binding('n', 17)
# bindingThird = make_binding('pi', 3.141664565464)

# frame = Frame([bindingSecond, bindingThird, bindingOne])

# width, height, x, y = {3.62, 1.01, 0.6, 0.76}
# ax = diagram(width, height)
# bbox = frame.draw(ax, x, y, dy=-0.5)
# adjust(ax, bbox)

""" EXPRESSIONS AND STATEMENTS """
""" An expressions is a combination of values, variables, and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions. """

print(42)
print(n + 25)

""" An statement is a unit of code that has an effect, like creating a variable or displaying a value. """
# Assignment statement
n = 13
# print assignment
print(n)

""" SCRIPT MODE """
miles = 26.2
miles_calculator = miles * 1.61
print(miles_calculator)

print(miles * 1.61)

x = 5
print(x + 1)

"""
ORDER OF OPERATIONS
"""

# Parentheses
option_one = 2 * (3-1)
option_two = (1+1)**(6-2)

minutes = 20
option_three = (minutes * 100) / 60

print(f"One: {option_one}\nTwo: {option_two}\nThree: {option_three:.2f}")

# Exponentiation
print(1+2**3)
print(2*3**2)

# Multiplication and division
print(2*3-1)
print(6+4/2)

# Operators the same precedence are evaluated from left to right
degress = 180
operator = degress / 6 * pi
print(f"The result is: {operator:.2f}")

""" STRINGS OPERATORS """

# the + operator performs string concatenation
first = 'throat'
second = 'wabier'
print(first + second)

""" DEBUGGING """
# Compute the percentage of the hour that has elapsed
minutes = 10
percentage = (minutes * 100) / 60
