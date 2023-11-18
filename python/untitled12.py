from tkinter import *
from tkinter import ttk

root=Tk()
root.title("classes project")
root.geometry("900x900")

list_of_elements = ['label','button','dropdown']
selected_val = StringVar()
dropdown = ttk.Combobox(root, values=list_of_elements, textvariable=selected_val)
dropdown.pack()

class CreateElements():
    def __init__(self):
        print("This is CreateElements class")
    def createLabel(self):
        label = Label(root, text="A new label has been created using class", fg="blue")
        label.pack()
    def createButton(self):
        btn = Button(root, text=" Button ", command=self.message)
        btn.pack(padx=20, pady=10)
    def createDropDown(self):
        list_of_elements1 = [1,2,3,4]
        selected_val1 = StringVar()
        dropdown1 = ttk.Combobox(root, values=list_of_elements1, textvariable=selected_val1)
        dropdown1.pack()
    def message(self):
        messagebox.showinfo("showinfo","You clicked the button created using class")
    def choose(self):
        global dropdown
        element = dropdown.get()
        if (element == "label"):
            self.createLabel()
        elif (element == "button"):
            self.createButton()
        elif (element == "dropdown"):
            self.createDropDown()
        

obj_of_createelements = CreateElements()

btn1 = Button(root, text=" Create Elements ", command=obj_of_createelements.choose)
btn1.pack()
        

root.mainloop()
