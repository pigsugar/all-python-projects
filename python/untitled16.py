from tkinter import *
import random

root=Tk()
root.title("Country Capitals")
root.geometry("400x400")

enter_country = Entry(root)
enter_country.place(relx=0.5, rely=0.2, anchor=CENTER)
enter_capital = Entry(root)
enter_capital.place(relx=0.5, rely=0.3, anchor=CENTER)

country_label = Label(root)
capital_label = Label(root)
random_country_label = Label(root)
random_capital_label = Label(root)

country_list = []
capital_list = []
                                                      
def addCountryAndCapital():
    country_name = enter_country.get()
    capital_name = enter_capital.get()
    country_list.append(country_name)
    capital_list.append(capital_name)
    country_label["text"] = "Country Name : " + str(country_list)
    capital_label["text"] = "Capital Name : " + str(capital_list)

def random_number():
    length_country = len(country_list)
    length_capital = len(capital_list)
    random_no_country = random.randint(0, length_country-1)
    random_no_capital = random.randint(0, length_capital-1)
    random_country_label["text"] = "Random Country : " + str(country_list[random_no_country])
    random_capital_label["text"] = "Random Capital : " + str(capital_list[random_no_capital])
    
btn = Button(root, text="Display Country And City Name", bg='blue', fg='white', command=addCountryAndCapital)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

country_label.place(relx=0.5, rely=0.5, anchor=CENTER)
capital_label.place(relx=0.5, rely=0.6, anchor=CENTER)

btn1 = Button(root, text="Display Country And City Name Randomly",bg='blue', fg='white', command=random_number)
btn1.place(relx=0.5, rely=0.7, anchor=CENTER)

random_country_label.place(relx=0.5, rely=0.8, anchor=CENTER)
random_capital_label.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
