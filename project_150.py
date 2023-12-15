from tkinter import *
import random

root = Tk()
root.title("Countries and Capitals")
root.geometry("500x500")

Country_name = Entry(root)
Capital_name = Entry(root)
Country_name.place(relx= 0.5, rely= 0.2, anchor=CENTER)
Capital_name.place(relx= 0.5, rely= 0.3, anchor=CENTER)

country_label = Label(root)
capital_label = Label(root)
random_number_generated_country = Label(root)
random_number_generated_capital = Label(root)

list1 = []
list2 = []
def country_capital():
    country = Country_name.get()
    list1.append(country)
    country_label["text"] = "Country Name:- " + str(list1)
    capital = Capital_name.get()
    list2.append(capital)
    capital_label["text"] = "Capital Name:- " + str(list2)
    
def random_country_capitals():
    length = len(list1)
    random_no = random.randint(0, length-1)
    index = list1[random_no]
    random_number_generated_country["text"] = "Random Country:- " + str(index)
    length1 = len(list2)
    random_no2 = random.randint(0, length1-1)
    index1 = list2[random_no2]
    random_number_generated_capital["text"] = "Random Capital:- " + str(index1)
    
btn = Button(root, text = "Display Countries and Cities name", command = country_capital, bg = "blue", fg = "white")
btn.place(relx= 0.5, rely=0.4, anchor=CENTER)

country_label.place(relx= 0.5, rely= 0.5, anchor=CENTER)
capital_label.place(relx= 0.5, rely= 0.6, anchor=CENTER)

btn1 = Button(root, text = "Dispaly Random countrys and capitals", command = random_country_capitals, bg = "blue", fg = "white")
btn1.place(relx= 0.5, rely= 0.7, anchor=CENTER)

random_number_generated_country.place(relx= 0.5, rely= 0.8, anchor=CENTER)
random_number_generated_capital.place(relx= 0.5, rely= 0.9, anchor=CENTER)

root.mainloop()