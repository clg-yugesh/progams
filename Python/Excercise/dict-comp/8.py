vowels = ['a','e','i','o','u']

fruit = ['apple', 'banana', 'cherry']

x = {a : sum(1 for letter in a if letter in vowels) for a in fruit }

print(x)