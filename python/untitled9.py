from tkinter import *

root=Tk()
root.title("thing")
root.geometry("500x500")

percentage_grade3 = Label(root)
percentage_grade5 = Label(root)
percentage_grade10 = Label(root)

class grade3():
    def __init__(self, language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
    def percentage(self):
        total_marks = self.language_arts + self.mathematics
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100 / 200
        percentage_grade3['text'] = grade_3_percentage
        
class grade5():
    def __init__(self, language_arts, mathematics,social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100 / 200
        percentage_grade5['text'] = grade_5_percentage

class grade10():
    def __init__(self, language_arts, mathematics,social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_10_percentage = total_marks_with_100 / 200
        percentage_grade10['text'] = grade_10_percentage
        
object_grade_3 = grade3(40,50)
grade_3_btn = Button(root, text="Grade 3", command=object_grade_3.percentage)
grade_3_btn.pack()
percentage_grade3.pack()

object_grade_5 = grade5(40,50,90)
grade_5_btn = Button(root, text="Grade 5", command=object_grade_5.percentage)
grade_5_btn.pack()
percentage_grade5.pack()

object_grade_10 = grade10(40,50,90)
grade_10_btn = Button(root, text="Grade 10", command=object_grade_10.percentage)
grade_10_btn.pack()
percentage_grade10.pack()
        
root.mainloop()
