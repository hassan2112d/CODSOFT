from tkinter import *
import tkinter.messagebox as tmsg

def rate():
    print("rate it")
    tmsg.showinfo("Rating box","How was your experiencd")
    

def faq():
    print("Exist")
    a =tmsg.askquestion("help" , "Was your experience good?")
    if a == "yes":
        tmsg.showinfo("Feedback","Thank you for your feedback")
    else:
        tmsg.showinfo("Feedback" , "You will be contacted by Team")

def func():
    print("hello")


a = Tk()

a.geometry("500x700")
a.title("pycharm")

    
b = Menu(a , tearoff=0)
c = Menu(b)
c.add_command(label="New", command=func)
c.add_command(label="Save as", command=func)
c.add_command(label="Save", command=func)

b.add_cascade(label="File",menu=c)
a.config(menu=b)


e = Menu(b)
e.add_command(label="OPEN",command=func)
e.add_command(label="aDD",command=func)
e.add_command(label="HELLO",command=func)
b.add_cascade(label="EDIT", menu=e)
a.config(menu=b)

submenu = Menu(b)
submenu.add_command(label="Help",command=faq)
submenu.add_command(label="rate",command=rate)
b.add_cascade(label="Help us" , menu=submenu)
a.config(menu=b)

a.mainloop()