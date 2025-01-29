words = ['python', 'programming', 'language']

x = {a : ''.join(sorted(a)) for a in words}

print(x)