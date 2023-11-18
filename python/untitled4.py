from tkinter import *
root=Tk()
root.title("Encapsulation")
root.geometry("450x500")

name_label = Label(root, text="Name: ")
name_label.place(relx=0.3, rely=0.1,anchor=CENTER)
password_label = Label(root, text="Password: ")
password_label.place(relx=0.3,rely=0.2,anchor=CENTER)
captcha_label = Label(root, text="Password: ")
captcha_label.place(relx=0.3,rely=0.3,anchor=CENTER)

name_input = Entry(root)
name_input.place(relx=0.6,rely=0.1,anchor=CENTER)
password_input = Entry(root)
password_input.place(relx=0.6,rely=0.2,anchor=CENTER)
captcha_input = Entry(root)
captcha_input.place(relx=0.6,rely=0.3,anchor=CENTER)

username_label = Label(root)
username_label.place(relx=0.5,rely=0.6,anchor=CENTER)
display_password_label = Label(root)
display_password_label.place(relx=0.5,rely=0.7,anchor=CENTER)
captcha_display_label = Label(root)
captcha_display_label.place(relx=0.5,rely=0.8,anchor=CENTER)

class userDB():
    def __init__(self):
        self.__username = "James"
        self.__password = "James76*"
        self.__captcha = "28j"
    def showUser(self):
        username_label['text'] = "Name : "+self.__username
        display_password_label['text'] = "Password : " + self.__password
        captcha_display_label['text'] = "Captcha : " + self.__captcha
    def addUser(self):
        global userDB_obj
        userDB_obj.username = name_input.get()
        userDB_obj.password = password_input.get()
        userDB_obj.captcha = captcha_input.get()
        print("Details Updated")
    
        
    
userDB_obj = userDB()
btn_ulg = Button(root, text="Update Login Details", command=userDB_obj.addUser)
btn_ulg.place(relx=0.35,rely=0.45,anchor=CENTER)
btn_sp = Button(root, text="Show profile", command=userDB_obj.showUser)
btn_sp.place(relx=0.65,rely=0.45,anchor=CENTER)


root.mainloop()