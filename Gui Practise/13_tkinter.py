def file():
    print("hello world")

def exit():
    print("Exist")

def func():
    print("hello")


from tkinter import *

a = Tk()

a.geometry("700x899")
a.title("Pycharm")

# b = Menu(a , tearoff=0)
# b.add_command(label="File" , command=file)
# b.add_command(label="exit" , command=quit)

# a.config(menu=b)

    
b = Menu(a , tearoff=0)
c = Menu(b)
c.add_command(label="New", command=func)
c.add_command(label="Save as", command=func)
c.add_command(label="Save", command=func)

b.add_cascade(label="File",menu=c)
a.config(menu=b)

a.mainloop()


