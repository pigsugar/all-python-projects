from tkinter import *
root = Tk()

root.title("idk")
root.geometry("600x600")

question_1_radiobutton = StringVar(value="0")
question_1_label = Label(root, text="Do you experience shortness of breath during routine activities?")
question_1_label.pack()
question_1_r1 = Radiobutton(root, text="yes", variable=question_1_radiobutton, value="yes")
question_1_r1.pack()
question_1_r2 = Radiobutton(root, text="no", variable=question_1_radiobutton, value="no")
question_1_r2.pack()

question_2_radiobutton = StringVar(value="0")
question_2_label = Label(root, text="Do you have swelling in the feet/ ankes/ legs (shoes feel tighter) or abdomen?")
question_2_label.pack()
question_2_r1 = Radiobutton(root, text="yes", variable=question_2_radiobutton, value="yes")
question_2_r1.pack()
question_2_r2 = Radiobutton(root, text="no", variable=question_2_radiobutton, value="no")
question_2_r2.pack()

question_3_radiobutton = StringVar(value="0")
question_3_label = Label(root, text="Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
question_3_label.pack()
question_3_r1 = Radiobutton(root, text="yes", variable=question_3_radiobutton, value="yes")
question_3_r1.pack()
question_3_r2 = Radiobutton(root, text="no", variable=question_3_radiobutton, value="no")
question_3_r2.pack()

question_4_radiobutton = StringVar(value="0")
question_4_label = Label(root, text="Do you experience shortness of breath while at rest/lying down?")
question_4_label.pack()
question_4_r1 = Radiobutton(root, text="yes", variable=question_4_radiobutton, value="yes")
question_4_r1.pack()
question_4_r2 = Radiobutton(root, text="no", variable=question_4_radiobutton, value="no")
question_4_r2.pack()

question_5_radiobutton = StringVar(value="0")
question_5_label = Label(root, text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?")
question_5_label.pack()
question_5_r1 = Radiobutton(root, text="yes", variable=question_5_radiobutton, value="yes")
question_5_r1.pack()
question_5_r2 = Radiobutton(root, text="no", variable=question_5_radiobutton, value="no")
question_5_r2.pack()

def fever_score():
    score = 0
    if question_1_radiobutton.get() == "yes":
         score = score + 10
         print(score)
        
    if question_2_radiobutton.get() == "yes":
        score = score + 10
        print(score)
        
    if question_3_radiobutton.get() == "yes":
        score = score + 10
        print(score)
        
    if question_4_radiobutton.get() == "yes":
        score = score + 10
        print(score)
        
    if question_5_radiobutton.get() == "yes":
        score = score + 10
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Report", "You don't need to visit a doctor")
    elif score > 10 and score <= 30:
        messagebox.showinfo("Report", "You may have to visit a doctor")
    else:
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor")
        
btn = Button(root, text="check", command=fever_score)
btn.pack()

root.mainloop()
