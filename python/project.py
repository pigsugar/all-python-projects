from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("project")
root.geometry("600x600")
root.configure(background = "lightblue")

lbl_choose_colour = Label(root,text="Choose Color: ")
lbl_choose_colour.place(relx=0.6, rely=0.9, anchor=CENTER)

lbl1 = Label(root, text="startx")
lbl2= Label(root, text="starty")
lbl3= Label(root, text="endx")
lbl4= Label(root, text="endy")

fillcolour = ['blue','black','gray','green','yellow',"pink","red",'orange','purple']
selectedval = StringVar()
dropdown1 = ttk.Combobox(root, state="readonly", values=fillcolour, textvariable=selectedval, width=10)
dropdownmenu = [10,50,100,200,300,400,500,600,700,800,900]
selectedval1 = StringVar()
dropdown2 = ttk.Combobox(root, state="readonly", values=dropdownmenu, textvariable=selectedval1, width=10)
dropdownmenu1 = [10,50,100,200,300,400,500,600,700,800,900]
selectedval2 = StringVar()
dropdown3 = ttk.Combobox(root, state="readonly", values=dropdownmenu1, textvariable=selectedval2, width=10)
dropdownmenu2 = [10,50,100,200,300,400,500,600,700,800,900]
selectedval3 = StringVar()
dropdown4 = ttk.Combobox(root, state="readonly", values=dropdownmenu2, textvariable=selectedval3, width=10)
dropdownmenu3 = [10,50,100,200,300,400,500,600,700,800,900]
selectedval4 = StringVar()
dropdown5 = ttk.Combobox(root, state="readonly", values=dropdownmenu3, textvariable=selectedval4, width=10)

canvas = Canvas(root, width=990, height=490, bg="white", highlightbackground="lightgray")
canvas.pack()
lbl1.place(relx=0.1, rely=0.85, anchor=CENTER)
lbl2.place(relx=0.3,rely=0.85, anchor=CENTER)
lbl3.place(relx=0.5,rely=0.85,anchor=CENTER)
lbl4.place(relx=0.7,rely=0.85,anchor=CENTER)

dropdown1.place(relx=0.8,rely=0.9,anchor=CENTER)
dropdown2.place(relx=0.2,rely=0.85,anchor=CENTER)
dropdown3.place(relx=0.4,rely=0.85,anchor=CENTER)
dropdown4.place(relx=0.6,rely=0.85,anchor=CENTER)
dropdown5.place(relx=0.8,rely=0.85,anchor=CENTER)

direction=""
startx=50
starty=50
endx=50
endy=50

root.mainloop()
