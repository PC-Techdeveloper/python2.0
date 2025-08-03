# Reassignment
# A new reassignment makes an existing variable refer to a new value
x = 5
print(x)

x = 7
print(x)

a = 5
b = a
a = 3
print(b)

# Updating variables
x = 0
x = x + 1

print(x)

"""
THE WHILE STATEMENT
"""


def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print("Blastoff! 🚀")


countdown(10)


def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:  # n is even
            n = n / 2
        else:
            n = n * 3 + 1  # n is odd


sequence(3)

# break: Exits the loop
while True:
    line = input('Enter a word: ')
    if line == 'done':
        break
    print(line)

print('** Done **')

""" SQUARE ROOTS"""
