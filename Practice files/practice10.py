val=int(input("Enter the size of matrix: "))
lst2=[]
for i in range(val):
    lst=[]
    for j in range(val):
        num=int(input("Enter number: "))
        lst.append(num)
    lst2.append(lst)
print(lst2)
maxi=lst2[0][0]
for i in range(val):
    for j in range(val):
        if(lst2[i][j]>maxi):
            maxi=lst2[i][j]
            row=i+1
            column=j+1
print(maxi)
print("Row is %d and Column is %d"%(row,column))

