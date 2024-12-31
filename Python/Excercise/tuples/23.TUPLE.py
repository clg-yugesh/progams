tup1 = (1, 2, 3, 4, 5)
tup2 = (3, 4, 5, 6)

set1 = set(tup1)
set2 = set(tup2)

# Find the difference between the two sets
diff = set1 - set2

result = tuple(diff)
