num = int(input("Enter the Num:"))
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")
  
# for i in range(1,100):
#     for j in range(2,i):
#         if(i%j)==0:
#             break
#     else:
#         print(i,end=",")