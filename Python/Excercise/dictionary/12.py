#to delete a list of keys from a dictonary

dictt = {"name":"Kelly","age":25,"salary":8000,"city":"newyork"}

keys = ["name","salary"]

for key in keys:
    if key in dictt:
        del dictt[key]
print(dictt)