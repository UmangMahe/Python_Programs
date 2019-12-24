file=open("file2.txt","w")
for i in range(3):
    num=int(input("Enter Number :"))
    file.write(str(num))
    file.write("\n")
file.close()
file=open("file2.txt","r")
a=[]
for x in file:
    a.append(int(x))
maxi=max(a)
print(maxi)
print(a)
file.close()
file=open("file3.txt","w")
file.write(str(a))
file.write("\n")
file.write(str(maxi))
file.close()
