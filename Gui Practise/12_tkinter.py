#Quiz 

from tkinter import *



def hello():
    
    a = input("Enter the height")
    b = input("Enter the width")
    c.geometry(f"{a}x{b}")
    

c = Tk()

c.geometry("500x600")

c.title("Pycharm")

d = Button(text="Click On Me",command=hello).pack()

c.mainloop()