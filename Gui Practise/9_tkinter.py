from tkinter import *

def hello():
    print("Submitted Successfully")

    with open("demo.txt","a") as f:
        f.write(f"{userentry.get(),passentry.get()}\n")

a = Tk()

a.geometry("800x500")

b = Label(a, text="Welcome").grid(column=3)

c = Label(a, text="Username :").grid(row=1,column=2)

d = Label(a, text="Password :").grid(row=2,column=2)

userentry = StringVar()
passentry = StringVar()
checkout = IntVar()

e = Entry(a , textvariable=userentry).grid(row=1,column=3)
f = Entry(a , textvariable=passentry).grid(row=2,column=3)
g = Checkbutton(a , text="check out",variable=checkout).grid(row=3,column=3)

f = Button(text="Submit", command=hello).grid(column=3)


a.mainloop()