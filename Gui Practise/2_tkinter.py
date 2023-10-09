from tkinter import *

a = Tk()

#Define the size of the Tk box
a.geometry("550x450")

#Min size of the box
a.minsize(400,200)

#Max size of the tk box
#a_root.maxsize(400,200)

b = Label(text= "Hello my name is Hassan")

b.pack()

a.mainloop()
