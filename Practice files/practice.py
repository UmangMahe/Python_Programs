file= open("hello.txt","r")
a=[]
ans=int(input("Enter line number to be displayed? "))

for line in file:
    a.append(line)
    
print(a[ans-1])

