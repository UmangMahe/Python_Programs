#31st august assignment
#PROGRAM - 1
#to accept a number and print in words

n=int(input("Enter any Number between 0 to 99: "))
a,b,c,d,e,f,g,h,i="Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"
un=n%10
tn=int(n/10)
if(tn==0 and un==0):
    print("Zero")
elif(tn==1):
    if(un==1):
        print(a)
    if(un==2):
        print(b)
    if(un==3):
        print(c)
    if(un==4):
        print(d)
    if(un==5):
        print(e)
    if(un==6):
        print(f)
    if(un==7):
        print(g)
    if(un==8):
        print(h)
    if(un==9):
        print(i)
if(un==1):
    nn="One"
elif(un==2):
    nn="Two"
elif(un==3):
    nn="Three"
elif(un==4):
    nn="Four"
elif(un==5):
    nn="Five"
elif(un==6):
    nn="Six"
elif(un==7):
    nn="Seven"
elif(un==8):
    nn="Eight"
elif(un==9):
    nn="Nine"
else:
    nn=""

if(tn==1):
    nn1="Ten"
elif(tn==2):
    nn1="Twenty"
elif(tn==3):
    nn1="Thirty"
elif(tn==4):
    nn1="Forty"
elif(tn==5):
    nn1="Fifty"
elif(tn==6):
    nn1="Sixty"
elif(tn==7):
    nn1="Seventy"
elif(tn==8):
    nn1="Eighty"
elif(tn==9):
    nn1="Ninety"
else:
    nn1=""

if(tn==0):
    print(nn)
elif(un==0):
    print(nn1)
elif(tn!=1):
    print(nn1,nn)
    

    
