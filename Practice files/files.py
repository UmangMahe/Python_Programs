file=open("filename.txt","r")
acount=0
ecount=0
icount=0
ocount=0
ucount=0
for x in file:
    for i in range(len(x)):
        if(x[i]=="A" or x[i]=="a"):
            acount=acount+1
        if(x[i]=="E" or x[i]=="e"):
            ecount=ecount+1
        if(x[i]=="I" or x[i]=="i"):
            icount=icount+1
        if(x[i]=="O" or x[i]=="o"):
            ocount=ocount+1
        if(x[i]=="U" or x[i]=="u"):
            ucount=ucount+1

file.close()
print("A occurs %d times"%acount)
print("E occurs %d times"%ecount)
print("I occurs %d times"%icount)
print("O occurs %d times"%ocount)
print("U occurs %d times"%ucount)
