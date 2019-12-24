#Square of Diagonals

val=int(input("Enter the size of matrix: "))
lst2=[]
for i in range(val):
    lst=[]
    for j in range(val):
        num=int(input("Enter number: "))
        lst.append(num)
    lst2.append(lst)
print(lst2)

for i in range(val):
    for j in range(val):
        if(i==j):
            sqr=lst2[i][j]**2
            print(sqr)
