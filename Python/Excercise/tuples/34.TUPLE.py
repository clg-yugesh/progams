tuple1 = (45, 45, 45, 45)

# Check if all items are the same by comparing the first item with all others
same = tuple1.count(tuple1[0]) == len(tuple1)

# Print the result
print("Are all items the same?:", same)
