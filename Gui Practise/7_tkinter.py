from tkinter import *

def user():
    print(f"the user name is {userentry.get()}")
    print(f"the password name is {passentry.get()}")

a = Tk()

a.geometry("700x600")

b = Label(a, text="Username")

c = Label(a, text="Password")
b.grid()
c.grid(row=1)

userentry = StringVar()
passentry = StringVar()

d = Entry(a, textvariable=userentry).grid(row=0,column=1)
e = Entry(a, textvariable=passentry).grid(row=1,column=1)

f= Button( text="Submit", command=user).grid()

a.mainloop()