n1=int(input("Enter a number: "))
st=""
while(n1>0):
    rem=n1%2
    st=str(rem)+st
    n1=n1//2

print(st)
