"""
A list comprehension creates a new list by applying an expression to each element of an iterable.
"""

squares = [x * x for x in (1, 2, 3, 4)]
print(squares)

squares = []

for x in (1, 2, 3, 4):
    squares.append(x * x)

# The expression applied to each element can be as complex as needed
print([s.upper() for s in "Hello World"])

## strip off any commas from the end of string in a list
print([s.rstrip(",") for s in ["Hello,", "World,"]])

## organize letters in words more neatly
sentence = "Beautiful is better than ugly."
print(["".join(sorted(word, key=lambda x: x.lower())) for word in sentence.split()])

## else can be added to the comprehension
print([x if x % 2 == 0 else -x for x in range(10)])
print([x if x in "aeiou" else "*" for x in "apple"])

"""
Double iteration:
"""
