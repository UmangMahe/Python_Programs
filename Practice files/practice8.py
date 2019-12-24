#Factorial of a number using class

class Fact:
    def input(root):
        num=int(input("Enter a number for factorial: "))
        p.process(num)
    def process(root,num):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        p.out(fact)
    def out(root,fact):
        print(fact)

p=Fact()
p.input()
