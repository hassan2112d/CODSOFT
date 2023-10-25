from tkinter import *

def hello():
    print("Hello World")

def world():
    print("Hiii")

def hii():
    print("Hello")
    
a = Tk()

a.geometry("700x600")

b = Frame(a,borderwidth=6,relief=SUNKEN)

b.pack()

c = Button(b,text="Print out", fg="white" , bg="black",command=hello)
c.pack()

d = Button(b,text="Print out", fg="white" , bg="black",command=world)
d.pack()

e = Button(b,text="Print out", fg="white" , bg="black", command=hii)
e.pack()

a.mainloop()


