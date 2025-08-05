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
print(h.get('c', 0))


def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram('parrot')

print_hist(h)

# To traverse the keys in sorted order, use the sorted() method.
for key in sorted(h):
    print(key, h[key])

"""
DICTIONARIES AND LISTS
"""

# Function that inverts a dictionary


def invert_dictionary(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


hist = histogram('parrot')
print(hist)

inverse = invert_dictionary(hist)
print(f"Invert dictionary: {inverse}")

# List can be values in a dictionary
t = [1, 2, 3]
d = dict()

"""
GLOBAL VARIABLES
"""

# They can be accessed from any function
verbose = True


def example1():
    if verbose:
        print('Running example1')


example1()

been_called = False


def example2():
    global been_called
    been_called = True


count = 0


def example3():
    global count
    count += 1


# if a global variable refers to a mutable value, you can modify the value
# without declaring the variable
known = {0.0, 1.1}


def example4():
    known[2] = 1


def example5():
    global known
    known = dict()


