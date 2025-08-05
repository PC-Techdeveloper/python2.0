"""
A dictionary contains a collection of indices, which are called keys, and a collection of values. Each key is associated with a single value. The association of a key and a value is called a key-value pair or sometimes an item.
"""

# The squiggly-brackets, {}, represent an empty dictionary.
# The function dict() creates an empty dictionary.

eng2sp = dict()
print(eng2sp)

# This output format is also an input format.
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

print(eng2sp['two'])

# The len() function returns the number of items in a dictionary.
print(len(eng2sp))

# if the key isn't in the dictionary, you get an exception
# print(eng2sp['four'])

# test if a key is in the dictionary
print('one' in eng2sp)
print('uno' in eng2sp)

"""
LOOPING AND DICTIONARIES
"""


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('a')
print(h)
# Dictionaries have a method called get() that takes a key and default value.
print(h.get('a', 0))
print(h.get('c', 0  ))


def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)
