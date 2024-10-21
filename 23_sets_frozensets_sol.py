set1 = frozenset({1, 2, 3, 4, 5})
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))
print(set2.difference(set1))
print(set1 - set2)