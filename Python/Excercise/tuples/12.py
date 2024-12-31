tup = (0, 1, 2, 3, 4, 3, 5)

print("Tuple before removing : ",tup)

tup_list = list(tup)

num = int(input("Enter an index number to remove :"))

tup_list.remove(num)

tup = tuple(tup_list)

print("Tuple after removing an element:", tup)