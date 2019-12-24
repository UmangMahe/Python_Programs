#Addition of Matrices

val=int(input("Enter the size of matrix: "))
lst2=[]
for i in range(val):
    lst=[]
    for j in range(val):
        num=int(input("Enter number: "))
        lst.append(num)
    lst2.append(lst)
print(lst2)
lst4=[]
for i in range(val):
    lst3=[]
    for j in range(val):
        num2=int(input("Enter number: "))
        lst3.append(num2)
    lst4.append(lst3)
print(lst4)
final=[]
for i in range(val):
    lst5=[]
    for j in range(val):
        lst5.append(lst2[i][j]+lst4[i][j])
    final.append(lst5)
print(final)
