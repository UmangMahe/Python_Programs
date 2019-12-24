#Square of Values of list

val=int(input("Enter the number of values: "))
lst=[]
sqr=[]
for i in range(val):
    num=int(input("Enter number "))
    lst.append(num)
    sqr.append(num**2)
print(lst)
print(sqr)
