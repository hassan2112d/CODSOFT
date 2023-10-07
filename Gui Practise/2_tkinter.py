from tkinter import *

a_root = Tk()

#Define the size of the Tk box
a_root.geometry("550x450")

#Min size of the box
a_root.minsize(400,200)

#Max size of the tk box
#a_root.maxsize(400,200)

b = Label(text= "Hello my name is Hassan")

b.pack()

a_root.mainloop()
