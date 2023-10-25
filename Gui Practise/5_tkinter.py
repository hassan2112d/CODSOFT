from tkinter import *

a = Tk()
a.geometry("700x500")
b = Frame(a , bg="gray" , borderwidth=10 , relief= SUNKEN)
d = Frame(a, bg="gray" , borderwidth=20 , relief = SUNKEN)


b.pack(side=LEFT , fill=Y)

d.pack(side=TOP , fill=X)

c = Label(b , text="Hello_World")
e = Label(d , text="Welcome to Calculator" , fg="blue")

c.pack(pady=200) 
e.pack(padx=200)

a.mainloop()