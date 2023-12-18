n=int(input("Enter a num:"))
fact=1
if n < 0:
    print("negatives not have fact")
elif n == 0:
    print("The fact of 0 is 1")
else:
    for i in range(1,n+1):
        fact = fact*i
    print("The fact of n is:",fact)