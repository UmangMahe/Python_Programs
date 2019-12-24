#Multiple Functions of List

amt=int(input("Enter the number of values: "))
num=[]
for i in range(amt):
    number=int(input("Enter number: "))
    num.append(number)
print("This is the Append Function")
print(num)
que=str(input("Do you want to sort the list (Y/N)"))
if(que=="Y"):
    num.sort()
    print(num)
else:
    print("OK")
ins=int(input("Enter the value to be removed:"))
num.remove(ins)
print(num)
que1=str(input("Do you want to clear the list (Y/N)"))
if(que1=="Y"):
    num.clear()
    print(num)
