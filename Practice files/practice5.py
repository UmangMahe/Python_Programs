#Reverse of List

val=int(input("Enter the list length: "))
lst=[]
for i in range(val):
    num=int(input("Enter the number : "))
    lst.append(num)
print(lst)
print("Reversed list is: ")
lst.reverse()
print(lst)

