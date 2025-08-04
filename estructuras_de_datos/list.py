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
