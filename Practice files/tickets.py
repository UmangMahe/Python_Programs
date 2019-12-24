file=open("ticket.txt","w")
while True:
    tno=int(input("Enter Ticket Number: "))
    file.write(str(tno))
    file.write("\n")
    source=input("Enter Source Station: ")
    file.write(source)
    file.write("\n")
    destn=input("Enter Destination: ")
    destn=destn.capitalize()
    file.write(destn)
    file.write("\n")
    price=int(input("Enter Price: "))
    file.write(str(price))
    file.write("\n")
    confirm=input("Want to Enter more (Y/N)?")
    if confirm in "Nn":
        break
    else:
        file.write("\n")
file.close()
count=0
file=open("ticket.txt","r")
for x in file.read().split():
    if(x=="Pune"):
        count+=1
file.close()
print(count)
