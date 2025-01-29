words = ['apple','banana','cherry','date']

x = {a : len(a) for a in words if len(a) > 5}

print(x)