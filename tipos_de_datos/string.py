"""
strings are not like integers, floats, and booleans. A string is a sequence, which means it is an ordered collection of other values.
"""

# A string is a sequence
fruit = 'banana'
letter = fruit[1]  # The expression in brackets is called an INDEX
print(letter)

# Accessing a character in a string
letter = fruit[0]
print(letter)

# LEN: Len is a built-in function that returns the length of a string
fruit = 'banana'
print(len(fruit))

# To get the last letter of a string
length = len(fruit)
last = fruit[length - 1]
print(f"Last letter is: {last}")

"""
TRAVERSAL WITH A FOR LOOP
"""
print("Traversal with a for loop:")
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# FOR STATEMENTS
print("For loop:")
for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

"""
STRING SLICES: A segment of a string is called a slice. Selecting a slice is similar to selecting a character.
"""

s = 'Monty Python'
one = s[0:5]
two = s[6:12]

print(one)
print(two)

fruit = 'manzana'
fruit = 'banana'
print(fruit[0:3])
print(fruit[:3])
print(fruit[3:])
print(fruit[:])
print(fruit[3:3])

"""
STRING METHODS
"""
word = 'pera'
new_word = word.upper()
print(new_word)

word = 'banana'
index = word.find('a')
indexSecond = word.find('na', 3)
print(index)
print(indexSecond)

"""
THE 'IN' OPERATOR: Is an a boolean operator that takes two strings and returns True if the first string is a substring of the second string.
"""

print('a' in 'banana')


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


in_both('apple', 'orange')

"""
STRING COMPARATIONS: The relational operators work on strings. (>, >=, <, <=, ==, !=)
"""

word = 'apple'

if word == 'cherry':
    print('All right, cherrys.')

if word < 'cherry':
    print(f'Your word, {word}, comes before cherry.')
elif word > 'cherry':
    print(f'Your word, {word}, comes after cherry.')
else:
    print('All right, cherrys.')
