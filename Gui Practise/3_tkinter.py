from tkinter import *
from PIL import Image , ImageTk


a = Tk()

a.geometry("1200x759")

b = PhotoImage(file="Gui Practise/spider.png")

c = Label(image=b)

c.pack()


a.mainloop()