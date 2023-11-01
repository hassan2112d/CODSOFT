from tkinter import *

import tkinter.messagebox as tmsg

def rangee():
    a = f"Yes you achieved it {myslider.get()}"
    tmsg.showinfo(f"Achievement" , a)

a = Tk()

a.title("Slider")
a.geometry("600x700")

Label(a, text="Hello! Mark your CS marks").pack()

myslider = Scale(a, from_=0 , to=100 , orient=HORIZONTAL)
myslider.pack()

Button(a , text="Click on me" ,  command=rangee ).pack()

a.mainloop()