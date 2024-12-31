#armstrong number

no = int(input("Enter a number : "))
ans = 0

c = len(str(no))

og_no = no
while no > 0:
    rem = no % 10
    ans = ans + rem**c
    no //= 10
if ans == og_no:
    print("The given number is armstrong.")
else:
    print("The given number is not armstrong")
