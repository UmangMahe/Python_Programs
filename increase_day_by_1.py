dd=int(input("Enter Date in dd format: "))
mm=int(input("Enter Month in mm format: "))
yy=int(input("Enter Year in yyyy format: "))
if yy%4==0 and (yy%100!=0 or yy%400==0):
    
        if(mm==2 and dd>=29):
            nm=mm+1
            nd=1
            print("New Date is ",nd,"/",nm,"/",yy)
        elif(dd==28 and mm==2):
            nd=dd+1
            print("New Date is ",nd,"/",mm,"/",yy)
        elif(dd>=31):
            nd=1
            if(mm>=12):
                ny=yy+1
                nm=1
                print("New Date is ",nd,"/",nm,"/",ny)
            else:
                nm=mm+1
                print("New Date is ",nd,"/",nm,"/",yy)
        else:
            nd=dd+1
            if(mm>12 or mm<=0):
                    print("Ugh!! Month must be between 1-12")
            else:
                print("New Date is ",nd,"/",mm,"/",yy)
else:
        if(mm==2 and dd>=28):
            nm=mm+1
            nd=1
            print("New Date is ",nd,"/",nm,"/",yy)
        elif(dd>=31):
                nd=1
                if(mm>=12):
                    ny=yy+1
                    nm=1
                    print("New Date is ",nd,"/",nm,"/",ny)
                else:
                    nm=mm+1
                    print("New Date is ",nd,"/",nm,"/",yy)
        else:
                nd=dd+1
                if(mm>12 or mm<=0):
                    print("Ugh!! Month must be between 1-12")
                else:
                    print("New Date is ",nd,"/",mm,"/",yy)
