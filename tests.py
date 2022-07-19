from itertools import product

allCombinations = list(product('LRUD',repeat = 3))

filtered = []

for comb in allCombinations:
    combString = ''.join(comb)
    if 'LR' not in combString and 'DU' not in combString and 'UD' not in combString:
        filtered.append(comb)

print(filtered)