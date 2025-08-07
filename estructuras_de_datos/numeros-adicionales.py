"""
The random function returns a random float between 0.0 and 1.0 (including 0.0 and excluding 1.0).
"""
import random

for i in range(10):
    x = random.random()
    print(x)

"""
The function randint() takes parameters low and high and returns an integer between low and high (including low and excluding high).
"""

print(random.randint(5, 10))
print(random.randint(5, 10))

# To choose an element from a sequence at random, use random.choice().
list_numbers = [1, 2, 3]
print(random.choice(list_numbers))

"""
DICTIONARY AND SUBTRACTION
"""


def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

