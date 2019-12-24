amt=int(input("Enter the values: "))
lst2=[]
for i in range(amt):
    lst=[]
    for j in range(amt):
        num=int(input("Enter the numbers: "))
        lst.append(num)
    lst2.append(lst)
print(lst2)
sqr=[]
import math
for i in range(amt):
    for j in range(amt):
        if(i==j):
            sqr.append(math.pow(lst2[i][j],2))
print(sqr)
