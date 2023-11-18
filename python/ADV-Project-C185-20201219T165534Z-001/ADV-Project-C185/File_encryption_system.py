from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")
root.title("cacao")
root.config(bg="lightblue")

file_name_entry = ""
encryption_text_data=""

def savedata():
    global file_name_entry
    global encryption_text_data
    filename =""
    file = open(filename+".txt","w")
    data = encryption_text_data.get("1.0", END)
    ciphercode = encrypt('XYZ', data)
    file_name_entry.delete()
    encryption_text_data.delete()
 

def apply_md5():
    print("MD5 function")
    
    
def apply_sha256():
    print("SHA function")   
    
    
btn=Button(root, text="Apply MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()