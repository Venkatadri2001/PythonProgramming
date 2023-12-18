n=input("Enter the word:")
n1=[]
for i in n:
    if i not in n1:
        n1.append(i)
print("The origional value is:",n1)