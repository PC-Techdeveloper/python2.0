# RETURN VALUES
# Calling the function generates a return value
import math

radius = 5
radians = math.pi / 2

e = math.exp(1)
height = radius * math.sin(radians)

# Create a fruitful function


def area(radius):
    a = math.pi * radius ** 2
    return a


print(f"{area(radius):.2f}")


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


print(absolute_value(-5))

""" INCREMENT DEVELOPMENT """
