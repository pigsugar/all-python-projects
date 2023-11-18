from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("600x600")
root.title("timezones")

clockimage = ImageTk.PhotoImage(Image.open("clock.jpg"))

india = Label(root, text="australia")
india.place(relx=0.2, rely=0.05, anchor=CENTER)

indiaclock = Label(root)
indiaclock["image"]=clockimage
indiaclock.place(relx=0.2, rely=0.35, anchor=CENTER)

indiatime = Label(root)
indiatime.place(relx=0.2, rely=0.65, anchor=CENTER)


usa = Label(root, text="japan")
usa.place(relx=0.7, rely=0.05, anchor=CENTER)

usaclock = Label(root)
usaclock["image"]=clockimage
usaclock.place(relx=0.7, rely=0.35, anchor=CENTER)

usatime = Label(root)
usatime.place(relx=0.7, rely=0.65, anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone("Australia/ACT")
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%H:%M:%S")
        indiatime ["text"]="the time in australia is: "+currenttime
        indiatime.after(200,self.times)
        
class usa():
    def times(self):
        home=pytz.timezone("Japan")
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%H:%M:%S")
        usatime ["text"]="the time in Japan is: "+currenttime
        usatime.after(200,self.times)        
        
obj_usa = usa()
obj_india = India()

indiabtn = Button(root, text="show time", command=obj_india.times)   
indiabtn.place(relx=0.2, rely=0.8, anchor=CENTER)     

usabtn = Button(root, text="show time", command=obj_usa.times)   
usabtn.place(relx=0.7, rely=0.8, anchor=CENTER)     

root.mainloop()