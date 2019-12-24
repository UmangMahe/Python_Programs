count=0
num=int(input("Enter a Number: "))
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print("Prime")
    rev=0
    tmp=num
    while(num>0):
        div=num%10
        rev=(rev*10)+div
        num=num//10
    count=0
    for i in range(1,rev+1):
        if(rev%i==0):
            count+=1
    if(count==2):
        print("Circular Prime")
else:
    print("Not Circular Prime")
