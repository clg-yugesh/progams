tup = (1,2,3,4,5,6,7,8,9)

even = odd = int()

for elemnent in tup:
    if elemnent % 2 == 0:
        even += 1
    else:
        odd += 1

print("Count of odd number : ",odd)
print("Count of even number :",even)
