# Lists methods and supported operators
a = [1, 2, 3, 4, 5]

# append: appends a new element to the end of the list

a.append(6)
a.append(7)
a.append(7)
print(a)

# Another list
b = [8, 9]
a.append(b)
print(a)

my_string = "Hello world"
a.append(my_string)
print(a)

# extend(enumerable): extends the list by appending elements from another
# enumerable
a = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7]
b = [8, 9, 10]

a.extend(b)
print(a)

a.extend(range(3))
print(a)

# list can also be concatenated with + operator
a = [1, 2, 3, 4, 5, 6, 7] + [8, 8] + b
print(a)

# index(value, [startIndex])  gets the index of the first occurrence of the input value
print(a.index(7))

# insert(index, value)  inserts value just before the specified index. Thus after the insertion the new element occupies position index.
a.insert(2, 50)
print(a)

# pop([index])  removes and returns the item at index.
print("Deleting index: 2:", a.pop(2))

# remove(value)  removes the first occurrence of the specified value.
a.remove(10)
print(a)

# reverse()  reverses the list in-place and returns None.
a.reverse()
print("Reversing:", a)

# count(value) counts the number of ocurrences of some value in the list
c = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
counted = c.count(3)
print("Counting:", counted)

# sort(): sorts the list in numerical and lexicographical order and returns None.
c.sort()
print("Sorting:", c)

# Lists can also be reversed when sorted using the reverse=True argument
c.sort(reverse=True)
print("Sorting in reverse order:", c)

# Element deletion
d = list(range(10))
del d[::2]
print(d)

del d[-1]
print(d)

del d[:]
print("Deleting all:", d)

# Copying lists
import copy

my_list = [1, 2, 3, 4, 5]
new_list = copy.copy(my_list)

print("Copying 1:", new_list)
second_new_list = copy.deepcopy(my_list)
print("Copying 2:", new_list)

aa = new_list.copy()
print("Copying 3:", aa)

"""
Accesing list values
"""
numbers = [10, 20, 30, 40, 60, 100, 234, 442]
numbers[0]
numbers[1]
print(numbers)

# Attempting to access an index outside the bounds of the list
# will raise an IndexError
# print(numbers[5]) ❌

"""
Negative indices are interpreted as counting from the END of the list
"""
print(numbers[-1])
print(numbers[-2])
# print(numbers[-10])  # ❌
print(numbers[len(numbers) - 1])

"""
Extracting sublists
"""
print(numbers[0:3])
print(numbers[:4])
print(numbers[4:])
print(numbers[::2])
print(numbers[-1:0:-1])

# With this in mind, you can print a reversed list
print(numbers[::-1])

"""
Advanced slicing
"""
data = "chandan purohit 22 2000"  # assuming data fields of fixed length
name_slice = slice(0, 19)
age_slice = slice(19, 21)
salary_slice = slice(22, None)

# We can have more readable slices
print(data[name_slice])
print(data[age_slice])
print(data[salary_slice])

# CHECKING IF LIST IS EMPTY
lst = []
if not lst:
    print("List is empty")

# ITERING OVER A LIST
my_list = ["foo", "bar", "baz"]

for item in my_list:
    print(item)

# You can also get the position of each item at the same time
for index, item in enumerate(my_list):
    print(f"The item in position {index} is {item}")
    # print("The index is {} and the item is {}".format(index, item))

# The other way of iterating a list a based on the index value
for i in range(0, len(my_list)):
    print(my_list[i])

# Note that changing items in a list while iterating on it may have
# unexpected results
for item in my_list:
    if item == "foo":
        del my_list[0]  # delete the first item
    print(my_list)

# CHECKING WHETHER AN ITEM IS IN A LIST
LST = ["test", "twest", "tweast", "treast"]
print("test" in LST)  # True
print("toast" in LST)  # False

"""
ANY AND ALL

- You can use all() to determine if all the values in an iterable evaluate to True
- You can use any() determines if one or more values in an iterable evaluate to True
"""
nums = [1, 1, 0, 1]
print(all(nums))

chars = ["a", "b", "c", "d"]
print(all(chars))

nums = [1, 1, 0, 1]
print(any(nums))

vals = [None, None, None, False]
print(any(chars))

vals1 = [1, 2, 3, 4]
any(val > 12 for val in vals1)

print(vals1)

any((val * 2) > 6 for val in vals1)
print(vals1)

"""
CONCATENATE AND MERGE LIST
"""
# The simplest way to concatenate
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2

# zip() returns a list of tuples
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]

for a, b in zip(alist, blist):
    print(a, b)

# if the lists have different lengths then the result will include only as
# many elements as the shortest one:
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3", "b4"]

for a, b in zip(alist, blist):
    print(a, b)

alist = []
len(list(zip(alist, blist)))

"""
For padding list of unequal length to the longest one with None use itertools.zip_longest => Import itertools
"""
alist = ["a1", "a2", "a3"]
blist = ["b1"]
clist = ["c1", "c2", "c3", "c4"]

import itertools

for a, b, c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)

# Insert to a specific index values
alist = [123, "xyz", "zara", "abc"]
alist.insert(2, [2009])
print(f"Final list: {alist}")

# Length of a list
# use len() to get the one-dimensional length of a list

print(len(["one", "two"]))
print(len(["one", [2, 3], "four"]))

# Remove duplicate values in list
"""
Removing duplicate values in a list can be done by converting the list to a set (that is an unordered collection of unique elements) and then converting it back to a list.
"""
names = ["aixk", "duke", "edik", "tofp", "duke"]
print(set(names))

## Accesing values in nested list
alist = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
print(alist[0][0][1])
print(alist[1][1][2])

## using nested for loops to print the list
for row in alist:
    for col in row:
        print(col)
# you can be used in a list comprehension
print([col for row in alist for col in row])
listc = alist[1].insert(2, 15)
print(listc)

"""
another way to use nested for loops. The other way is better but i have need to use this occasion
"""
for row in range(len(alist)):
    for col in range(len(alist[row])):
        print(alist[row][col])

## Using slices in nested list
print(alist[1][1:])
print(alist)

## INITIALIZING A LIST TO A FIXED NUMBER OF ELEMENTS

# For immutable elements (None, strings literals, etc)
my_lsit = [None] * 10
my_list = ["test"] * 10

# For mutable elements (lists, dicts, sets, etc)
my_list = [{1}] * 10
print(my_list)
my_list[0].add(2)
print(my_list)

# Instead, to initialize the list with a fixed number
# of different mutables, use
my_list = [{1} for _ in range(10)]
print(my_list)
