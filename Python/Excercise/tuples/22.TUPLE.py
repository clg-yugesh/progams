tup = (1, 2, 2, 3, 2, 4, 2)

freq = {}

for element in tup:
    if element in freq:
        freq[element] += 1 
    else:
        freq[element] = 1
print(freq)