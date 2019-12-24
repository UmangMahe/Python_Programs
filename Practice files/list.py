amt=int(input("Enter number of values"))
l=[]
maxi=0
for i in range(amt):
    num=int(input("Enter value :"))
    l.append(num)
    if (num>maxi):
        maxi=num
print(l)
print(maxi)  
