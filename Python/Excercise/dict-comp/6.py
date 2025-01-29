from sympy import isprime

x = {a : isprime(a) for a in range(1,11)}

print(x)