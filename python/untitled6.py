from tkinter import *
import random

root=Tk()
root.title("color randomizer")
root.geometry("600x600")
root.configure(bg="snow")

lbl_random_color_name = Label(root, font=("comicsans",28,"bold"), bg="white")
lbl_random_color_name.place(relx=0.5,rely=0.35, anchor=CENTER)
lbl_score = Label(root, text="Score : 0", font=("comicsans",20,"bold"), bg="white")
lbl_score.place(relx=0.1, rely=0.1)
input_value = Entry(root, borderwidth=4, width=25)
input_value.place(relx=0.5,rely=0.45, anchor=CENTER)

class game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ['BLUE','GREEN','YELLOW','BLACK']
        self.random_number_for_text = random.randint(0,3)
        self.color = ['blue','green','yellow','black']
        self.random_number_for_color = random.randint(0,3)
        lbl_random_color_name['text'] = self.text[self.random_number_for_text]
        lbl_random_color_name['fg'] = self.color[self.random_number_for_color]
    def __updateScore(self,input_value):
        if input_value == self.color[self.random_number_for_color]:
            print(self.color[self.random_number_for_color])
            self.__score = self.__score + random.randint(1,10)
            lbl_score['text'] = "Score : " + str(self.__score)
    def get_user_value(self, input_value):
        self.__updateScore(input_value)

def getInput():
    value = input_value.get()
    game_obj.get_user_value(value)
    game_obj.updateGame()
    input_value.delete(0,END)
        
            
        
game_obj = game()
btn = Button(root, text="Start", command=game_obj.updateGame, bg='green', fg="white", relief=FLAT, padx=3, pady=3, font=("comicsans",18,"bold"))
btn.place(relx=0.6, rely=0.6, anchor=CENTER)
btn1 = Button(root, text="Check", command=getInput, bg='red', fg="white", relief=FLAT, padx=3, pady=3, font=("comicsans",18,"bold"))
btn1.place(relx=0.4, rely=0.6, anchor=CENTER)

root.mainloop()