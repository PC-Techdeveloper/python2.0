# A list is a sequence of values. The values in a list are called
# elements or sometimes items.
cheeses = ['Cheddar', 'Edam', 'Gouda']

numbers = [42, 143]

empty = []

print(cheeses, numbers, empty)

"""
LIST ARE MUTABLE: You can change the values in a list.
"""

numbers[1] = 5
print(numbers)

print('Edam' in cheeses)
print('Brie' in cheeses)

""" TRAVERSING A LIST """
for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

# A for loop over an empty list never runs the body
for x in []:
    print('This never happens! ❌')

# A list can contain another list (nested)
list_nested = ['spam', 1, ['eggs', 'ham'], [34, 324, 5]]
print(list_nested)

"""
LIST OPERATORS
"""
print("--- list operators ---")
# The + operator concatenates lists:
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)

# the * operator repeats a list a given number of times
print([1, 2, 3] * 4)

"""
LIST SLICES
"""

print("--- list slices ---")

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[-1: -3: -1])
print(t[:])

t[1:3] = ['x', 'y']
print(t)

"""
LIST METHODS
"""

# Append: adds a new element to the end of the list.
t = ['a', 'b', 'c']
t.append('d')
print(t)

# Extend: takes a list as an argument and appends all of the elements.
t1 = ['a', 'b', 'c']
t2 = ['d', 'e', 'f']

t1.extend(t2)
print(t1)

# Sort: arranges the elements of the list from low to high.
t = ['c', 'b', 'a']
t.sort()
print(t)

"""
MAP, FILTER AND REDUCE
"""
print("--- map, filter and reduce ---")
# sum: adding up the elements of a list (built-function)
t = [4, 5, 6]
print(sum(t))

# an operation like this that combines a sequence of elements into a
# single value is called a "reduce".


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


# Map: applies a function to each element of a list.
print(capitalize_all(['a', 'b', 'c']))

"""
DELETING ELEMENTS
"""

# pop: removes and returns the last element of a list.
t = ['a', 'b', 'c', 'd']
x1 = t.pop()
x2 = t.pop(0)
print(x1, x2)

# del: removes the element at a given index.
t = ['a', 'b', 'c']
del t[1]
print(t)

# remove: removes the first occurrence of a given element.
# if not found, returns None
t = ['a', 'b', 'c', 'a', 'b', 'c']
t.remove('a')
print(t)

# to remove more than one element, you can use del with a slice index
remove_items = ['apple', 'banana', 'orange', 'cherry', 'pear']
del remove_items[1:3]
print(remove_items)

"""
LIST AND STRINGS
"""

# To convert from a string to a list, you can list()
s = 'hello'
t = list(s)
print(t)

# break a string into words, you can use split()
s = 'pining for the fjords'
t = s.split()
print(t)

# Join: joins a list of strings into a single string
t = ['a', 'b', 'c']
delimiter = '-'
s = delimiter.join(t)
print(s)

"""
OBJECTS AND VALUES:
"""
a = 'banana'
b = 'banana'
print(a is b)
# get two different objects
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

"""
ALIASING
"""

a = [1, 2, 3]
b = a
b[0] = 42
print(b is a)
print(a)

"""
LIST ARGUMENTS: When you pass a list to a function, the function gets a reference to the list.
"""


def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c', 'd']
delete_head(letters)

print(letters)

# Here, an example using append:
t1 = [1, 2]
t2 = t1.append(3)
print(t1)

# Using + operator
t1 = [1, 2]
t2 = t1 + [3]
print(t2)
