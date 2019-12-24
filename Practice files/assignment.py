#Combination of a 3 digit number
#Aman Malaiya
#BBA-IT SEM(II)

num=int(input("Enter a Number of 3 digit: "))
lst=[]
lst2=[]
lst3=[]
lst4=[]
if(num>99 and num<1000):
    while(num>0):
        div=num%10
        lst.append(div)
        num=num//10
    for i in range(len(lst)):
        for j in range(len(lst)):
            for k in range(len(lst)):
                if(i!=j and j!=k and i!=k):
                    print(str(lst[i])+str(lst[j])+str(lst[k]))
else:
    print("Enter a 3 digit number")
