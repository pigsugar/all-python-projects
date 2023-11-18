from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.geometry("900x500")

image = ImageTk.PhotoImage(Image.open("image1.png")) 


place_image=Label(root)

place_image['image'] = image

place_image.place(relx=0.7, rely=0.5,anchor=CENTER)

label = Label(root, text="Assigning Jobs", font=("French Script Mt", 20 , "bold"), fg=("dark olive green"))

label.place(relx=0.01, rely=0.06,anchor=W)

label_doctor=Label(root,text="Doctor : ")
#place the label label_doctor at 0.04 and 0.15 relx and rely values respectively and set anchor to center.
label_doctor.place(relx=0.04, rely=0.15, ancho=CENTER)


#------------------Label for string IT professional-------------
label_IT=Label(root,text="IT professional : ")
#place the label label_IT at 0.06 and 0.45 relx and rely values respectively and set anchor to center.
label_IT.place(relx=0.06, rely=0.45, anchor=CENTER)


#------------------Label for string "Chemical Engineer ------------
label_chemical=Label(root,text="Chemical Engineer : ")
#place the label label_chemical at 0.07 and 0.75 relx and rely values respectively and set anchor to center.
label_chemical.place(relx=0.07, rely=0.75, anchor=CENTER)

#---------------------entry elements--------------------------------
entry_doctor = Entry(root)
entry_doctor.place(relx=0.25, rely=0.15,anchor=CENTER)

entry_IT = Entry(root)
entry_IT.place(relx=0.25, rely=0.45,anchor=CENTER)

entry_chemical = Entry(root)
entry_chemical.place(relx=0.25, rely=0.75,anchor=CENTER)
#------------------------Labels selected--------------------------
label_selected_doctor=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_doctor.place(relx=0.01, rely=0.3,anchor=W)

label_selected_IT=Label(root,font=("times",12,"bold"),fg="dark olive green")
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)

label_selected_chemical=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)

class parent():
    def __init__(self):
        print("This is parent class")
        
    def doctor(doctor_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor['text'] = doctor_name+" has been allotted to "+hospital_list[random_hospital]
        
    def softwareEngineer(it_professional_name):
        IT_company_list = ["I code", "Web Access", "Dotcom Services", "ATOS"]
        random_IT_company = random.randint(0,3)
        label_selected_IT['text'] = it_professional_name+" has been allotted to "+IT_company_list[random_IT_company]
        
    def chemicalEngineer(chemical_engineer_name):
        company_list = ["Air Liquide", "BASF", "Albemarle Corporation", "DuPont"]
        random_company = random.randint(0,3)
        label_selected_chemical['text'] = chemical_engineer_name+" has been allotted to "+company_list[random_company]
        
class child1(parent):
    def __init__(self):
        print("This is child1 class")
    def getDoctor(self):
        name = entry_doctor.get()
        parent.doctor(name)
        
class child2(parent):
    def __init__(self):
        print("This is child2 class")
    def getIT(self):
        name = entry_IT.get()
        parent.softwareEngineer(name)