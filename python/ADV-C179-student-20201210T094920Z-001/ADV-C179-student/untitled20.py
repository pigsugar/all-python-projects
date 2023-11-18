from tkinter import *
from tkinter import ttk
root= Tk()
root.title("yipee")
root.geometry("500x500")
root.config(bg="lightblue")

title = Label(root, text="LANGUAGE TRANSLATOR", bg="lightblue", font=("cambridge",15,"bold","italic"))
title.place(relx=0.5, rely=0.2, anchor=CENTER)

lbl = Label(root, text="enter text", bg="lightblue",font=("cambridge",15,"bold","italic"))
lbl.place(relx=0.5, rely=0.29, anchor=W)

textarea = Text(root,bg="white", font=("cambridge",15,"bold","italic"), height=10, width=45)
textarea.place(relx=0.5, rely=0.39, anchor=W)
root.mainloop()