from tkinter import *

def func():
    global i 
    list.insert(ACTIVE,f"{i}")
    i+=1
i = 0
a = Tk()
a.geometry("600x800")
a.title("Py")

list = Listbox(a)
list.pack()

list.insert(END, "First item of our listbox")

Button(a ,text="Add on" , command= func).pack()

a.mainloop()