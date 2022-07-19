from itertools import combinations

l = ['L','R','D','U']

# Movemos el resto del cuerpo
allcombinations = combinations(l,2)

for combination in allcombinations:
    print(list(combination))
