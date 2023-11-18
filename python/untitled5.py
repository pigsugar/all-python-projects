from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.title ("encapsulation")
root.geometry("800x600")

heading = Label(root, text="juice center", bg="orange2", font=("Sylfaen",18,"bold","italic"))
heading.place(relx=0.05, rely=0.1, anchor=W)

juice = ImageTk.PhotoImage(show.image("logo.png"))
juicelabel = Label(root, image=juice, bg="orange2")
juicelabel.place(relx=0.2, rely=0.4, anchor=W)

apple = ImageTk.PhotoImage(show.image("apple_img.png"))
mango = ImageTk.PhotoImage(show.image("mango_img.png"))
orange = ImageTk.PhotoImage(show.image("orange.png"))

fruitlabel=Label(root, bg="orange2")
fruitlabel.place(relx=0.75, rely=0.8, anchor=CENTER)

fruit_list ["apple","mango","orange"]
fruitdropdown = ttk.Combobox(root, state="readonly", values=fruit_list, justify="right")
fruitdropdown (relx=0.95, rely=0.25, anchor=E)

quantitylabel = Label(root, text="enter quantity", bg="orange2",font=("bahnschrift light",12))
quantitylabel.place(relx=0.96, rely=0.35, anchor= E)

inputquantity = Entry(root)
inputquantity.place(relx=0.95, rely=0.4, anchor=E)

showamount = Label(root, bg="orange2",font=("bahnschrift light",12))
showamount.place(relx=0.95, rely=0.7, anchor= E)

showquantity = Label(root, bg="orange2",font=("bahnschrift light",12))
showquantity.place(relx=0.95, rely=0.8, anchor= E)
class Juice:
    def __init__(self, fruit_name, quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 250
       
    def calculatecost(self):
        total_cost = self.quantity * self.__cost
        showamount["text"]="you have to pay: "+str(total_cost)+" USD"
        if(self.fruit == "apple"):
            calorie = self.quantity * 52347
            fruitlabel["image"]="apple"
        elif(self.fruit == "orange"):
            calorie = self.quantity * 1223221
            fruitlabel["image"]="orange"
        elif(self.fruit == "mango"):
            calorie = self.quantity * 2172010
            fruitlabel["image"]="mango"
        showquantity["text"]="x"+str(self.quantity)+ " =" +str(calorie)+ " calories"
    def get_cost(self):
        self.__calculatecost()  
   
def orderjuice():
    fruit = fruitdropdown.get()
    quantity = inputquantity.get()
    obj1 = Juice(fruit, quantity)
    obj1.calculatecost()
   
btn = Button(root, text="TOTAL", command=orderjuice)    
btn.pack()
root.mainloop()


