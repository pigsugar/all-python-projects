from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title("tk")
root.geometry("500x500")
root.configure(bg="lightblue")

label_img = Label(root, bg="white")


img_path = ""
def Open_Image():
    global img_path
    img_path = filedialog.askopenfilename(title=" Open Text File", filetypes=[("Image Files","*.jpg;*.gif;*.png;*.jpeg;*.txt")])
    print(img_path)
    img_e = ImageTk.PhotoImage(Image.open(img_path))
    label_img['image'] = img_e
    img_e.close()
    

def Rotate_Image():
    global img_path
    im = Image.open(img_path)
    Rotated_Img= im.rotate(180)
    image = ImageTk.PhotoImage(Rotated_Img)
    label_img["image"] = image
    print(img_path)
    image.close()
    
    
btn = Button(root, text="open Image", command=Open_Image)
btn.place(relx=0.5, rely=0.1, anchor=CENTER)

btn1 = Button(root, text="rotate Image",command=Rotate_Image)
btn1.place(relx=0.5, rely=0.7, anchor=CENTER)

    
label_img.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()