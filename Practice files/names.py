amt=int(input("Enter number of Values: "))
lst=[]
for i in range(amt):
    name=input("Enter Names: ")
    lst.append(name)
print(lst)
maxi=len(lst[0])
for i in range(amt):
    if(len(lst[i])>maxi):
        maxi=len(lst[i])

for i in range(amt):
    if(len(lst[i])==maxi):
        print(lst[i])
