import tkinter as tk
from tkinter import *

expression=""
def press(num):
    global expression
    expression = expression+str(num)
    Result.delete(0.0, END)
    Result.insert(0.0, expression)

def percentage():
    global expression
    express = int(expression)/100
    Result.insert(0.0, express)
    expression=""
    
def equalpress():
    global expression
    try:
        result = eval(expression)
        total = round(result,5)
        Result.delete(0.0, END)
        Result.insert(0.0, total)
        expression=""
    except:
        Result.delete(0.0, END)
        err="Error"
        Result.insert(0.0, err)
        expression=""

def clear():
    global expression
    expression=""
    Result.delete(0.0, END)

def delete():
    global expression
    expression = expression[0:-1]
    Result.delete(0.0, END)
    Result.insert(0.0, expression)
    
        
root = tk.Tk()

root.title("Calculator")
root.geometry("320x550")

Result = tk.Text(root, height=5, width=40)
Result.grid(row=0, column=0)
Result.config(background='Grey', foreground='white')
Result.config(font=('helvetica', 40, 'bold'))
C = tk.Button(root, width=7, height=3, text="C", command=clear)
C.config(bd=1, bg="red")
C.grid(row=2, sticky=W, padx=10, pady=10)
perc = tk.Button(root, width=7, height=3, text="%", command=percentage)
perc.grid(row=2, sticky=W, padx=80, pady=10)
perc.config(bd=1, bg="red")
delete = tk.Button(root, width=7, height=3, text="del", command=delete)
delete.grid(row=2, sticky=E, padx=115, pady=10)
delete.config(bd=1, bg="red")
div = tk.Button(root, width=7, height=3, text="/", command=lambda: press("/"))
div.grid(row=2, sticky=E, padx=20, pady=10)
div.config(bd=1, bg="red")
num7 = tk.Button(root, width=7, height=3, text="7", command=lambda: press(7))
num7.grid(row=3, sticky=W, padx=10, pady=10)
num7.config(bd=1, bg="red")
num8 = tk.Button(root, width=7, height=3, text="8", command=lambda: press(8))
num8.grid(row=3, sticky=W, padx=80, pady=10)
num8.config(bd=1, bg="red")
num9 = tk.Button(root, width=7, height=3, text="9", command=lambda: press(9))
num9.config(bd=1, bg="red")
num9.grid(row=3, sticky=E, padx=115, pady=10)
mul = tk.Button(root, width=7, height=3, text="*", command=lambda: press("*"))
mul.config(bd=1, bg="red")
mul.grid(row=3, sticky=E, padx=20, pady=10)
num4 = tk.Button(root, width=7, height=3, text="4", command=lambda: press(4))
num4.config(bd=1, bg="red")
num4.grid(row=4, sticky=W, padx=10, pady=10)
num5 = tk.Button(root, width=7, height=3, text="5", command=lambda: press(5))
num5.config(bd=1, bg="red")
num5.grid(row=4, sticky=W, padx=80, pady=10)
num6 = tk.Button(root, width=7, height=3, text="6", command=lambda: press(6))
num6.config(bd=1, bg="red")
num6.grid(row=4, sticky=E, padx=115, pady=10)
sub = tk.Button(root, width=7, height=3, text="-", command=lambda: press("-"))
sub.config(bd=1, bg="red")
sub.grid(row=4, sticky=E, padx=20, pady=10)
num1 = tk.Button(root, width=7, height=3, text="1", command=lambda: press(1))
num1.config(bd=1, bg="red")
num1.grid(row=5, sticky=W, padx=10, pady=10)
num2 = tk.Button(root, width=7, height=3, text="2", command=lambda: press(2))
num2.config(bd=1, bg="red")
num2.grid(row=5, sticky=W, padx=80, pady=10)
num3 = tk.Button(root, width=7, height=3, text="3", command=lambda: press(3))
num3.config(bd=1, bg="red")
num3.grid(row=5, sticky=E, padx=115, pady=10)
add = tk.Button(root, width=7, height=3, text="+", command=lambda: press("+"))
add.config(bd=1, bg="red")
add.grid(row=5, sticky=E, padx=20, pady=10)
zero = tk.Button(root, width=17, height=3, text="0", command=lambda: press(0))
zero.config(bd=1, bg="red")
zero.grid(row=6, sticky=W, columnspan=2, padx=10, pady=10)
point = tk.Button(root, width=7, height=3, text=".", command=lambda: press("."))
point.config(bd=1, bg="red")
point.grid(row=6, sticky=E, padx=115, pady=10)
equal = tk.Button(root, width=7, height=3, text="=", command=equalpress)
equal.config(bd=1, bg="red")
equal.grid(row=6, sticky=E, padx=20, pady=10)
root.rowconfigure((0,1), weight=1)
root.columnconfigure((0,0), weight=1)



root.mainloop()
