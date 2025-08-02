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


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print(f"dx = {dx}")
    print(f"dy = {dy}")
    return 0.0


# To test the new function, call it with sample arguments
distance(1, 2, 3, 4)
