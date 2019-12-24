from tkinter import *

class Application(Frame):
     def __init__(self,master):
         """Initializes a Frame"""
         Frame.__init__(self,master)
         self.grid()
         self.widgets()
     def widgets(self):
         """Create buttons"""
         Label(self,text="Hello Name").grid(row=0,column=0,sticky=W)
         
         Label(self,text="Select the one").grid(row=1,column=0,sticky=W)

         self.fav=StringVar()
         self.fav.set(0)
         
         Radiobutton(self, text="Umang Maheshwari",variable=self.fav, command=self.update_text, value="Umang, Age - 19, SICSR").grid(row=2,column=0,sticky=W)

         Radiobutton(self, text="Mohd Altaf",variable=self.fav, command=self.update_text, value="Altaf, Age - 19, SICSR").grid(row=3,column=0,sticky=W)

         Radiobutton(self, text="Yash Jha",variable=self.fav, command=self.update_text, value="Yash, Age - 20, SICSR").grid(row=4,column=0,sticky=W)

         self.result=Text(self,width=40,height=5,wrap=WORD)
         self.result.grid(row=5,column=0,columnspan=3)
 
     def update_text(self):
         message="Hello "
         message+=self.fav.get()
         
         self.result.delete(0.0, END)
         self.result.insert(0.0, message)
                              

#Create window
root = Tk()
#Configure Window
root.title("Hello Name")

app=Application(root)
root.mainloop()
