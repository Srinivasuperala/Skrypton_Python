n=int(input("Enter Number : "))
fact=0
for i in range(2,n):
    if (n%2==0):
        fact=fact+1
if fact==0:
    print("Prime numbers")
else:
    print("not a prime number")