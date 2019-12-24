#Number has Factorial in List

val=int(input("Enter the list length: "))
lst=[]
for i in range(val):
    num=int(input("Enter the number : "))
    lst.append(num)
print(lst)
for j in range(val):
    count=0
    tmp=lst[j]
    for i in range(1,tmp):
        if(tmp%i==0):
            tmp=tmp/i
            count=count+1
        else:
            break
    if(tmp==1):
        print(count)
    else:
        print("The number doesn't has factorial")
