import prettytable
from functions import *

print("Enter the coefficients of the polynomial: ", end='')
data = input().split()
odds = [int(data[i]) for i in range(len(data))]

roots = []
possible_roots = []
odd0_dividers = find_dividers(odds[0])
oddN_dividers = find_dividers(odds[-1])

for x in oddN_dividers:
    for y in odd0_dividers:
        r = x / y
        if possible_roots.count(r) == 0:
            possible_roots.append(r)
        if possible_roots.count(-r) == 0:
            possible_roots.append(-r)

print("Possible roots of the polynomial:", possible_roots, end="\n\n")

print("Horner's scheme.")

head = ["Possible roots \\ Odds"]
for i in range(len(data)):
    data[i] = data[i] + " (k" + str(i) + ")"
data += [ "Is root?" ]
head.extend(data)
table = prettytable.PrettyTable(head)

for x in possible_roots:
    row = [x, odds[0]]
    for i in range(len(odds) - 1):
        row.append((row[i + 1] * x + odds[i + 1]))
        print(float(row[i + 1] * x + odds[i + 1]).as_integer_ratio(), end=' ')
    print()
    row.append(is_root(odds, x))
    table.add_row(row)
    if row[-1] == True:
        roots.append(x)

print(table, end="\n\n")
print("Roots:", roots)
