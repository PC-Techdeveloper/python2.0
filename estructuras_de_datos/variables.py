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
