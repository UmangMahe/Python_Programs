#31st aug
#ASSIGNMENT PROGRAM NUMBER - 3
#calculate age using birthdate

dd=int(input("Enter Birthday Date: "))
mm=int(input("Enter Birthday Month: "))
yy=int(input("Enter Birthday Year: "))
dd1=int(input("Enter Current Date: "))
mm1=int(input("Enter Current Month: "))
yy1=int(input("Enter Current Year: "))

if(mm>12 or mm1>12):
    print("Either of the two months are Invalid!!")
if(mm==2 and dd>=30) or (dd>31):
    print("Error in Date, %d is not valid for Month"%(dd),mm)               #Process Invalid Statements
if(mm1==2 and dd1>=30) or (dd1>31):
    print("Error in Date, %d is not valid for Month"%(dd1),mm1)
else:
    if(dd<=31 or dd1<=31):
        if(mm>mm1):
            nm=12-mm
            am=mm1+nm
        else:
            am=(mm1-mm)     #months

        if(dd<dd1):
            nd=dd1-dd       #Days
        else:
            nd=(31-dd)+dd1
            am=am-1         #days

        if(yy>=2000):      #years
            ay=yy1%1000
            ny=yy%1000
            ny=ay-ny
        if(yy<=2000 and mm>mm1): 
            ay=2000-yy
            ny=ay+(yy1%1000)-1 #years
        else:
            ay=2000-yy
            ny=ay+(yy1%1000)
        if(nd==31):           #months
            am=am+1
            print(ny,"Year(s)",am,"Month(s)")
        else:
            print(ny,"Year(s)",am,"Month(s)",nd,"Day(s)")
    else:
        print("Date %d is Invalid"%dd)

    #program finished
