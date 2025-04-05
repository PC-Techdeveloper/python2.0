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
