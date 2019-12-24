#Addition of two numbers

class Add:
    def addition(root):
        a=int(input("Enter number: "))
        b=int(input("Enter number: "))
        p.Process(a,b)
    def Process(root,a,b):
        c=a+b
        p.Out(c)
    def Out(root,c):
        print(c)
p=Add()
p.addition()
