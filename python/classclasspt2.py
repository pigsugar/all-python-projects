from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("900x600")
root.title("class classpt2")
root.configure(background="lightblue")

class Createlements:
    def __init__(self):
        print("this is a test for creating element class")

    def createnewelements(self):
        label=Label(root, text="a new label has been created", fg="red")
        label.pack()
        btn = Button(root, text="Button", command=self.message)
        btn.pack(padx=20, pady=10)
    
    def message(self):
        messagebox.showinfo("alert","Wrong button!")
        
obj = Createlements()

btn = Button(root, text="click to create a label and a button", command = obj.createnewelements)
btn.pack(padx=20, pady=10)      
root.mainloop()