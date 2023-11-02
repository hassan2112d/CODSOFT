from tkinter import *
import tkinter.messagebox as tmsg

def func():
    tmsg.showinfo(f"Order ",f"Thank you for your order{var.get()}")
a = Tk()

a.geometry("700x800")

a.title("Pycharm")

var = StringVar()
var.set(var)

Label(text="What would you like to order?" , justify=LEFT , font="bold 19").pack()

radio = Radiobutton(text="Paratha" , variable=var , value="Paratha").pack(anchor=W)
radio = Radiobutton(text="Biryani" , variable=var , value="Biryani").pack(anchor=W)
radio = Radiobutton(text="Pilawo" , variable=var , value="Pilawo").pack(anchor=W)
radio = Radiobutton(text="Chai" , variable=var , value="Chai").pack(anchor=W)

Button(text="Submit",command=func).pack()

a.mainloop()