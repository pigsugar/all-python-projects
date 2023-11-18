from tkinter import *
root= Tk()
root.title("yipee")
root.geometry("500x500")
root.config(bg="lightblue")

lbl1 = Label(root)
lbl1.place(relx=0.5, rely=0.2,anchor=CENTER)

lbl2 = Label(root)
lbl2.place(relx=0.5, rely=0.4,anchor=CENTER)

lbl3 = Label(root)
lbl3.place(relx=0.5, rely=0.6,anchor=CENTER)

def hospital():
    lbl1["text"]="Michael has been alloted to galaxy"
    
def chemical():
    lbl2["text"]="savannah has been alloted to IT company"
    
def company():
    lbl3["text"]="dave has been alloted to chemical company"
    
btn1 = Button(root, text = "show the hospital alloted", command = hospital)
btn1.place(relx=0.5, rely=0.3,anchor=CENTER)


btn2 = Button(root, text = "show the IT company alloted", command = company)
btn2.place(relx=0.5, rely=0.7,anchor=CENTER)

btn3 = Button(root, text = "show the company alloted", command = chemical)
btn3.place(relx=0.5, rely=0.5,anchor=CENTER)

root.mainloop()