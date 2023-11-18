# Basic tkinter template
import random, os

from tkinter import *
root = Tk()
root.title("Driving License")
root.geometry("400x250")
root.resizable(height=False, width=False)

monthes = ['January', 'February','March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']
names = ['Winnie The Pooh', 'Walter White', 'Mr. Goodman', 'Jeffy Jeffy', 'H. H. Heisenberg', 'Willis Foe', 'Spongebob Squarepants']

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_id = Label(root, text='')
label_name = Label(root, text='')
label_dob = Label(root, text='')
label_pin = Label(root, text='')
label_address = Label(root, text='')
label_vehicle_type = Label(root, text='')



# Define the function
def update_labels():
    os.system('cls')
    ID_value = random.randint(1000000000,9999999999)
    name = random.choice(names)
    dob = str(random.randint(1,30)) + " " + str(random.choice(monthes)) + " " + str(random.randint(1921, 2000))
    pin = random.randint(100000,999999)
    address = "Disney Land, Hong Kong" 
    vehicle_type = 'Two Four'
    print(type(ID_value))
    print(type(name))
    print(type(dob))
    print(type(pin))
    print(type(address))
    print(type(vehicle_type))
    label_id['text'] = ID_value
    label_name['text'] = name
    label_dob['text'] = dob
    label_pin['text'] = pin
    label_address['text'] = address
    label_vehicle_type['text'] = vehicle_type

    
    
# Create a button
button1 = Button(root, text="Show My Driving License", command=update_labels)
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
root.mainloop()