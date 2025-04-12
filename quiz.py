# Importando biblioteca math y utilizando la función pi
from math import pi

operation = [str(round(pi, i)) for i in range(0, 5)]
print(operation)

set1 = {50, 30, 70}
set2 = {80, 50, 20}

# Intersección
print(set1 & set2)

list = ['Python', 'Developers']

result = [i for i in list if len(i) > 6]

print(result)


def addToList(listContainer):
    listContainer += [10]  # Add to the end of the list


myListContainer = [10, 20, 30, 40]

addToList(myListContainer)

print(myListContainer)

print(len(myListContainer))

# Part 2

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

result = s1.intersection(s2)
result2 = s1 & s2

print(result)
print(result2)

num = 10
num = num * 2
num += num - 5

print(num)
